from math import isnan
import os
import sys
from shutil import copyfile
from sys import argv
import subprocess
import traceback

from scipy.interpolate import interp1d as interpolator

from QDLC.plot_tools.plotstrings_py import *
from QDLC.misc.colormaps import get_colormap

def get_files(set_filetosort, destiny, index = "", endpoint_only = False, use_max_evaluation = False, endpoint_shift = 0, use_folder = False, interpolate = False, interpolation_points = 500,cbs = False, colormap = "turbo", purge_median = False, delim = " ",clearNaN = False, force_single = False):
    filesfound = 0

    # Cleanup the destiny path for Windows.
    destiny = destiny.replace("\\", "/")
    if not (destiny[-1] == "/"):
        destiny += "/"

    # Generate List of folders to evaluate
    toevaluate = []
    if use_folder:
        for dirs_ in os.listdir(destiny):
            if os.path.isdir(destiny+dirs_):
                toevaluate.append(destiny+dirs_)
    else:
        toevaluate = [destiny]

    # Ugly piece of script to gather all the data. IDK how any of this even works anymore.
    for destiny in toevaluate:
        if "DS_Store" in destiny:
            continue
        if not (destiny[-1] == "/"):
            destiny += "/"
        os.makedirs(os.path.dirname(destiny+"img/"), exist_ok=True)
        
        filestosort = []
        if (set_filetosort == "all"):
            # Look into example folder and evaulate all .txt files. Maybe check for filesize so G1 and G2 matrices are excluded
            for root, dirs, files in os.walk(destiny):
                if "img" in dirs or root.endswith("img"):
                    continue
                for root_, dirs_, files_ in os.walk(root):
                    for file_ in files_:
                        if (file_ == "logfile.log"):
                            continue
                        if (file_.endswith(".txt")):
                            filestosort.append(file_)    
                break
        else:
            filestosort.extend(set_filetosort.split(","))
        print(filestosort)

        print("Input path: " + destiny + " input index = " +
            ", ".join([indx for indx in index]))
        for filetosort in filestosort:
            try:
                print("Evaluating " + filetosort + "... ")
                outputlist = []
                headerline = None
                with open(destiny + "/img/out_"+filetosort, "w") as out:
                    for root, dirs, files in os.walk(destiny):
                        if "img" in dirs:
                            continue
                        for file in files:
                            if file == filetosort and not "_out" in file:
                                filesfound += 1
                                with open(os.path.join(root, file), "r") as src:
                                    data = src.readlines()
                                    lfc = [None]
                                    for root_, dirs_, files_ in os.walk(root):
                                        for file_ in files_:
                                            if (file_ == "logfile.log"):
                                                #print(root+"/"+file_, end="... ")
                                                with open(root+"/"+file_, encoding="utf-8") as logfile:
                                                    lines = logfile.readlines()
                                                    for line in lines:
                                                        if "Logfile ident number 0:" in line:
                                                            lfc[0] = float(line.split("Logfile ident number 0:")[-1])
                                                        if "Logfile ident number 1:" in line:
                                                            lfc.append(float(line.split("Logfile ident number 1:")[-1]))
                                                        if (lfc[0] == None) and "--lfc" in line:
                                                            lfc = [float(a) for a in line.split("--lfc ")[-1].split(" ")[0].split(",")]
                                    if lfc[0] is None:
                                        lfc[0] = float(root.split("_")[-1])
                                    if force_single:
                                        lfc = [lfc[0]]
                                    if not lfc[0] == None:
                                        if not endpoint_only and len(lfc) > 1 and lfc[1] != None:
                                            endpoint_only = True
                                            index = ["lfc", "lfc2"]
                                        if headerline == None:
                                            headerline = data[0]
                                        if len(data) > 0 and not data[0].split()[0] == "#":
                                            data_is_str = True
                                            if (endpoint_only):
                                                if localmaxima is None:
                                                    data = [data[-1-endpoint_shift]]
                                                else:
                                                    maxima = [0.0 for a in data[1].split("\t") if len(a) > 1]
                                                    if (int(localmaxima[1]) != 0):
                                                        for d in data[localmaxima[0]:localmaxima[1]]:
                                                            try:
                                                                dd = [float(a.replace("\n","")) for a in d.split("\t") if len(a) > 1]
                                                                maxima = [max(m,ddd) for m,ddd in zip(maxima,dd)]
                                                            except Exception as e:
                                                                pass
                                                    else:
                                                        for d in data[1:]:
                                                            try:
                                                                dd = [float(a.replace("\n","")) for a in d.split("\t") if len(a) > 1]
                                                                if dd[0] >= localmaxima[0] and dd[0] <= localmaxima[1]:
                                                                    maxima = [max(m,ddd) for m,ddd in zip(maxima,dd)]
                                                                elif dd[0] > localmaxima[1]:
                                                                    break
                                                            except Exception as e:
                                                                pass
                                                    data = [" ".join([str(a) for a in maxima])]
                                            else:
                                                if interpolate:
                                                    vs = []
                                                    for line in data:
                                                        if len(line) < 2:
                                                            pass
                                                        try:
                                                            vss = [float(a) for a in line.split()]
                                                            if len(vs) == 0:
                                                                vs = [ [a] for a in vss ]
                                                            else:
                                                                for i,v in enumerate(vss):
                                                                    vs[i].append(v)
                                                        except:
                                                            pass
                                                    xmin = np.min(vs[0])
                                                    xmax = np.max(vs[0])
                                                    newx = np.linspace(xmin,xmax,int(interpolation_points), endpoint=True)
                                                    data = [newx] + [interpolator(vs[0], v)(newx) for v in vs[1:]]
                                                    data_is_str = False
                                            appended = 0
                                            for line in data if data_is_str else zip(*data):
                                                try:
                                                    if data_is_str:
                                                        outputlist.append( lfc + [float(a) for a in line.split()])
                                                    else:
                                                        outputlist.append( lfc + list(line))
                                                    appended+=1
                                                except Exception as e:
                                                    if headerline is not None:
                                                        headline = line
                                                    else:
                                                        pass
                                            print(f"File {filesfound} processed, appended {appended} lines to the dateset.", end="\r")
                                        else:
                                            filesfound -= 1
                                    else:
                                        print("Failed to evaluate file '" +
                                            os.path.join(root, file)+"'")
                    # Clear NaNs:
                    if clear_nans:
                        for i,row in enumerate(outputlist):
                            #print(row)
                            for j,el in enumerate(row):
                                if isnan(el) and i > 0:
                                    outputlist[i][j] = outputlist[i-1][j]
                    outputlist = [[str(j) for j in i] for i in sorted( outputlist, key=lambda outputlist: (float(outputlist[0]), float(outputlist[1])))]
                    # Purge Median
                    #if purge_median:
                    #    outputlist = [a for a in outputlist]
                    old = outputlist[0][0]
                    print(f"Length of outputlist: {len(outputlist)}")
                    print("".join([str(i) + " " for i in index]) + headerline.replace("\t"," "), file=out)
                    for i,line in enumerate(outputlist):
                        if not (line[0] == old) and i < len(outputlist):
                            print("", file=out)
                            old = line[0]
                        print(" ".join(line), file=out)

                with open(f"{destiny}img/{filetosort.split()[0]}.py", "w") as file:
                    print(plotstring_generate_abitrary(filename=filetosort, index_offset = (1+len(index), len(index)),cbs=cbs,colormap=colormap,delim=delim), file=file, end="")
                print("\nFiles found: " + str(filesfound))

                plotstring = f"python3 \"{destiny}img/{filetosort.split()[0]}.py\""
                print("Running " + plotstring + "... ", end="")
                try:
                    print("\n"+str(subprocess.Popen(plotstring, shell=True, stdout=subprocess.PIPE).stdout.read()))
                except Exception as e:
                    print("Failed!\nError message:\n" + str(e))
                    print(traceback.format_exc())
                print("done!")
            except Exception as e:
                print("Failed, maybe the file doesn't exist or something else went wrong.\nError message: ")
                print(traceback.format_exc())


if __name__ == "__main__":
    # Help
    if (len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help"]])):
        print("# Need at least 2 input arguments: FileToSort, Destiny")
        print("# Additional Parameters:")
        print("#   --localmaxima=min:max  --  Use a local interval and gather the maximum value of this interval instead of using [-1]")
        print("#   -maxima                --  Uses the max() function on the datasets")
        print("#   -interpolate           --  Interpolates the dataset onto 500 points")
        print("#   -folder                --  Evaluates this script in the entire folder, treating every subfolder as a complete dateset")
        print("#   --offset=int           --  Use [-offset] instead of [-1] for the final datapoints of the dataset")
        print("#   --colormap=str         --  Colormap for plots. Default is 'turbo'")
        print("#   --delim=str            --  Delimitor for plots. Default is ' '")
        print("#   -cbs                   --  Plot a single colorbar for all plots. Otherwise, a colorbar for every plot is used.")
        print("#   -forceSingle           --  Force use of only one of the logfile counters.")
        print("# Note that this script will REQUIRE the logfilecounter to be present for sorting.")
        exit()

    # Input Parameters
    set_filetosort = str(sys.argv[1])
    destiny = str(sys.argv[2])
    index = ""#str(sys.argv[3]).split("+")
    endpoint_only = False
    localmaxima = None
    if any(["--localmaxima=" in a for a in sys.argv]):
        localmaxima = [[b for b in a.replace("--localmaxima=","").split(":")] for a in sys.argv if "--localmaxima=" in a][0]
        localmaxima = [ float(a) if "." in a or "E" in a or "e" in a else int(a) for a in localmaxima]
        print("Looking for 'endpoint' as a local maxima in interval {}".format(localmaxima))
    if "-maxima" in sys.argv:
        localmaxima = (0,-1)
    
    endpoint_shift = [int(a.split("=")[-1]) for a in sys.argv if "--offset" in a.split("=")][0] if any( ["--offset" in a.split("=") for a in sys.argv] ) else 0 # The endpoint chosen will shift by this amount
    interpolate = "-interpolate" in sys.argv
    use_folder = "-folder" in sys.argv
    use_cbs = "-cbs" in sys.argv
    clear_nans = "-clearNaN" in sys.argv
    colormap = [a.replace("--colormap=","") for a in sys.argv if "--colormap=" in a ][0] if any(["--colormap=" in a for a in sys.argv]) else "turbo"
    delim = [a.replace("--delim=","") for a in sys.argv if "--delim=" in a ][0] if any(["--delim=" in a for a in sys.argv]) else " "
    force_single = "-forceSingle" in sys.argv

    # Evaluate
    get_files(set_filetosort, destiny, index, endpoint_only, localmaxima, endpoint_shift, use_folder, interpolate, cbs=use_cbs, colormap=colormap, delim=delim, clearNaN = clear_nans, force_single = force_single)