# Extracts all endpoints of a file

import os
import sys
from tokenize import String
import numpy as np
import traceback
from bisect import bisect_left as lower_bound

def get_endpoint(set_filetosort, input_path, localmaxima = None, offset = 0, use_folder = False, use_lfc = False, at_time = False):
    # Input Parameters
    set_filetosort = str(sys.argv[1])
    input_path = str(sys.argv[2])
    
    # Cleanup the destiny path for windows
    input_path = input_path.replace("\\", "/")
    if not (input_path[-1] == "/"):
        input_path += "/"

    # Generate List of folders to evaluate
    toevaluate = []
    if use_folder:
        for dirs_ in os.listdir(input_path):
                toevaluate.append(input_path+dirs_)
    else:
        toevaluate = [input_path]

    # Logfilecounter
    if use_lfc:
        print("Using Logfilecounter")

    filestosort = []
    print(f"Input Path: {input_path}")
    print(f"Files to sort: {set_filetosort}")

    # Find all files to evaluate
    if (set_filetosort == "all"):
        # Look into example folder and evaulate all .txt files. Maybe check for filesize so G1 and G2 matrices are excluded
        for root, dirs, files in os.walk(input_path):
            if "img" in dirs or root.endswith("img"):
                continue
            for root_, dirs_, files_ in os.walk(root):
                found = False
                if not "logfile.log" in files_:
                    continue
                for file_ in files_:
                    if (file_ == "logfile.log"):
                        continue
                    if (file_.endswith(".txt")):
                        filestosort.append(file_)    
                        found = True
                if found:
                    break
            break
        #filestosort.append("atomicinversion.txt")
        #filestosort.append("photonpopulation.txt")
        #filestosort.append("spectrum_H.txt")
        #filestosort.append("spectrum_V.txt")
        #filestosort.append("advanced_photon_statistics.txt")
        #filestosort.append("chirp.txt")
    else:
        filestosort.append(set_filetosort)
    print(filestosort)

    # Ugly piece of script to gather all the data. It's a mystery.
    for input_path in toevaluate:
        for key in filestosort:
            try:
                if "DS_Store" in input_path:
                    continue
                output_name = key.replace(".txt","_endpoints.txt")
                if not (input_path[-1] == "/"):
                    input_path += "/"
                output = []
                have = []
                indx = 0
                prior = None
                for root, dirs, files in os.walk(input_path):
                    for file in files:
                        if file == key:
                            with open(os.path.join(root, file),"r") as f:
                                try:
                                    data = f.readlines()
                                    found_lfc = False
                                    try:
                                        if use_lfc:
                                            with open(os.path.join(root, "logfile.log"),"r") as lf:
                                                lfl = reversed(lf.readlines())
                                                for line in lfl:
                                                    if "--lfc" in line:
                                                        line = line.split()
                                                        indx = line[ line.index("--lfc")+1 ]
                                                        found_lfc = True
                                                        break
                                        else:
                                            indx = float(root.split("_")[-1].split("/")[0])
                                            try:
                                                indxx = float(root.split("_")[-2].split("/")[0])
                                                indx += 10000*indxx
                                            except:
                                                pass
                                        if not use_lfc or (use_lfc and found_lfc):
                                            if at_time is not False:
                                                index = lower_bound(data[1:],at_time,key = lambda x: float(x.replace("\n","").split("\t")[0]) )
                                                output.append((indx, data[index+1]))
                                            elif localmaxima is None:
                                                output.append((indx, data[-1-offset]))
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
                                                output.append((indx, "\t".join([str(a) for a in maxima])+ "\n"))
                                            prior = output[-1][1]
                                            have.append(indx)
                                    except Exception as e:
                                        print("Couldn't append data for index " + str(indx)+ " for file "+os.path.join(root, file)+"\nUsed dummy " + str(indx+1) + ","+prior+" instead -> " + str(e))
                                        output.append((indx+1,prior))
                                        have.append(indx)
                                        indx = indx + 1
                                except Exception as e:
                                    print("Couldn't open/read " + os.path.join(root, file) + ", used dummy " + str(indx+1) + ","+prior+" instead -> " + str(e))
                                    output.append((indx+1,prior))
                                    have.append(indx)
                                    indx = indx + 1
                #print(str(output))
                #tohave = range(0,np.max([np.max(have),indx]))
                #if len(have) < len(tohave):
                #    print("Appending missing indices")
                #    zeroline = ""
                #    for i in range(len(output[1].split())-1):
                #        zeroline += "\t0"
                #    print("Zeroline will be 'indx " + zeroline + "'")
                #    for num in tohave:
                #        if not num in have:
                #            output.append(str(num) + zeroline + "\n")
                #    print(str(len(have)) + " dummy lines added.")
                output.sort(key = lambda entry : float(entry[0].split(",")[0] if isinstance(entry[0],str) else entry[0]))
                with open(os.path.join(input_path, output_name),"w") as f:
                    index = 0;
                    for line in output:
                        print((str(index if not use_lfc else line[0])+"\t"+line[1]).replace("\t\t","\t"),file=f,end="")
                        index += 1
            except Exception as e:
                print("Key "+key+" failed, reason:")
                print(traceback.format_exc())


if __name__ == "__main__":
    # Help
    if (len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help"]])):
        print("# Need at least 2 input arguments: FileToSort, Destiny")
        print("# Additional Parameters:")
        print("#   -folder                --  Evaluates this script in the entire folder, treating every subfolder as a complete dateset")
        print("#   -lfc                   --  Uses the logfilecounter instead of the file number for sorting")
        print("#   --localmaxima=min:max  --  Use a local interval and gather the maximum value of this interval instead of using [-1]")
        print("#   -maxima                --  Uses the max() function on the datasets")
        print("#   --offset=int           --  Use [-offset] instead of [-1] for the final datapoints of the dataset")
        print("#   --atTime=float         --  Use point at time instead of [-1] for the final datapoints of the dataset")
        print("# Note that this script will use the file number instead of the logfilecounter if -lfc is not provided")
        exit()
    
    # Input Parameters
    set_filetosort = str(sys.argv[1])
    destiny = str(sys.argv[2])
    # Use a local interval and gather the maximum value of this interval instead of using [-1]
    localmaxima = None
    if any(["--localmaxima=" in a for a in sys.argv]):
        localmaxima = [[b for b in a.replace("--localmaxima=","").split(":")] for a in sys.argv if "--localmaxima=" in a][0]
        localmaxima = [ float(a) if "." in a or "E" in a or "e" in a else int(a) for a in localmaxima]
        print("Looking for 'endpoint' as a local maxima in interval {}".format(localmaxima))
    if "-maxima" in sys.argv:
        localmaxima = (0,-1)
    offset = [int(a.replace("--offset=","")) for a in sys.argv if "--offset=" in a][0] if any(["--offset=" in a for a in sys.argv]) else (int(input("Offset = ") or 0)) if localmaxima is None else 0
    at_time = [float(a.replace("--atTime=","")) for a in sys.argv if "--atTime=" in a][0] if any(["--atTime=" in a for a in sys.argv]) else False
    use_folder = "-folder" in sys.argv
    use_lfc = "-lfc" in sys.argv

    # Evaluate
    get_endpoint(set_filetosort, destiny,localmaxima, offset,use_folder,use_lfc,at_time)