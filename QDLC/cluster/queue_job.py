import os
import sys
from time import sleep
from math import floor,ceil
from random import randint
import subprocess

#0d0h0m
def time_to_min(timestr):
    time_d = timestr.split("d")[0]
    time_h = timestr.split("d")[1].split("h")[0]
    time_m = timestr.split("d")[1].split("h")[1].replace("m","")
    return float(time_m) + float(time_h)*60 + float(time_d)*24*60

def autofind_modules():
    all_modules = []
    name = [str(a).replace("b'","").strip().lower() for a in subprocess.Popen("scluster", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()]
    cluster_name = "noctua2" if any(["noctua2" in a for a in name]) else "noctua" if any(["noctua" in a for a in name]) else "oculus"
    prefix = "module load compiler && module load lang && module load math && " if cluster_name == "noctua2" else ""
    for (module, key) in zip(["gcc","python","eigen"],["GCC/","Python/","Eigen/"] if cluster_name == "noctua2" else ["compiler/GCC/","lang/Python/","math/Eigen/"]):
        modules = [str(b).replace("b'","") for a in subprocess.Popen(prefix + "module avail "+module, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines() for b in a.split() if key in str(b)]
        modules_versions = [ sum([int(b.replace("'",""))/10**i for i,b in enumerate(a.replace(key,"").split("-")[0].split("."))]) for a in modules]
        modules_total = [(version, name) for version,name in zip(modules_versions, modules)]
        modules_total.sort( key = lambda t: t[0])
        fmodule = modules_total[-1][-1].replace("'","")
        print("Module chosen for {}: {}".format(module,fmodule))
        all_modules.append(fmodule)
    all_modules.append(cluster_name)
    return tuple(all_modules)

module_gcc, module_python, module_eigen, cluster = autofind_modules()
# Generate run script
def generate_runscript(name = "QDLC", cluster = "oculus", runtime = "7d0h0m", program = "QDLC-3.3.5.out", cores = -1, mem = -1, project = "hpc-prf-pdsm", user = "dbauch@mail.upb.de", cwd = "/scratch/hpc-prf-pdsm/dbauch/", settingfile = "$1", outputfolder = "$2", move_results_to_parent_folder = False, subname = ""):
    configuration = {
        "oculus" : {"command" : "ccsalloc",
                    "modules" : [module_gcc, module_eigen, module_python],
                    "cores" : "30",
                    "mem" : "25g"},
        "noctua" : {"command" : "sbatch",
                    "modules" : [module_gcc, module_eigen, module_python],
                    "cores" : "40",
                    "mem" : "25g"},
        "noctua2" : {"command" : "sbatch",
                    "modules" : ["compiler","lang","math",module_gcc, module_eigen, module_python],
                    "cores" : "128",
                    "mem" : "25g"}
    }

    if cores == -1:
        cores = configuration[cluster]["cores"]
    if mem == -1:
        mem = configuration[cluster]["mem"]
    time_d = runtime.split("d")[0]
    time_h = runtime.split("d")[1].split("h")[0]
    time_m = runtime.split("d")[1].split("h")[1].replace("m","")
    binpath = "/upb/departments/pc2/users/d/dbauch/QDLC-C/"

    if "noctua" in cluster:
        rtm = time_to_min(runtime)
        if cluster == "noctua2":
            jobtype = "normal"
        else:
            jobtype = "short" if rtm <= 30 else ( "batch" if rtm <= 12*60 else "long" )
        ret = """#!/bin/sh
#SBATCH -p """+jobtype+"""
#SBATCH -N 1
#SBATCH --tasks-per-node="""+cores+"""
#SBATCH --mem="""+mem+"""
#SBATCH -t """+time_d+"""-"""+time_h+""":"""+time_m+""":00
#SBATCH -A """+project+"""
#SBATCH --mail-type all
#SBATCH --mail-user """+user+"""
#SBATCH -J """+name+"""
#SBATCH -o """+cwd+"""out/%A.out
#SBATCH -e """+cwd+"""err/%A.err
"""+"\n".join(["module load " + a for a in configuration[cluster]["modules"]])+"""
cd """+binpath+"""
"""+binpath+program+""" --file '"""+settingfile+"""' --Threads -1 '"""+outputfolder+"""' """
    elif cluster == "oculus":
        ret = """#!/bin/sh
#CCS --res=rset=1:ncpus="""+cores+""":mem="""+mem+"""
#CCS -t """+time_d+"""d"""+time_h+"""h"""+time_m+"""m0s
#CCS -o """+cwd+"""%reqid.out
#CCS --stderr """+cwd+"""%reqid.out
#CCS -m abe
#CCS -M """+user+"""
#CCS -N """+name+"""
#CCS -g """+project+"""
"""+"\n".join(["module load " + a for a in configuration[cluster]["modules"]])+"""
cd """+binpath+"""
"""+binpath+program+""" --file '"""+settingfile+"""' --Threads -1 '"""+outputfolder+"""' """
    else:
        print("Cluster not valid")
        return False
    if move_results_to_parent_folder:
        ret += """
mv """+os.path.join(outputfolder,subname,"*")+" "+outputfolder+"""
rm -r """+os.path.join(outputfolder,subname)
    return ret

def split_settingfile(outputpath, settings, anticipated_runtime="7d0h0m", average_runtime=-1):
    if average_runtime == -1:
        return settings
    anticipated_runtime = time_to_min(anticipated_runtime)
    average_runtime = time_to_min(average_runtime)
    #jobtype_length = {"short" : 30, "batch" : 60*12, "long" : 20*24*60}[anticipated_jobtype]
    jobincrement = floor(anticipated_runtime/average_runtime)
    finalsettings = []
    for [file, outputpath, name, fileval, num, d, move_to_parent_folder,_] in settings:
        print("Will split settingfile {} -> {} ({} settings) into {} subsettingfiles.".format(file,name,num,ceil(num/jobincrement)))
        newsettingfile_path = os.path.join(outputpath,name)
        os.makedirs(newsettingfile_path,exist_ok=True)
        print("The new setting files will be saved to and executed from {} as 'subsettings_{}_X.txt'".format(newsettingfile_path,name))
        for i in range(ceil(num/jobincrement)):
            newsettingfile = "subsettings_"+name+"_"+str(i)+".txt"
            newsettingfile_completepath = os.path.join(newsettingfile_path, newsettingfile)
            with open( newsettingfile_completepath, "w" ) as f:
                start = i*jobincrement
                end = min( len(d), jobincrement*(i+1) )
                nn = name+"_"+str(i)
                print("# {}".format(nn),file=f)
                print("".join( d[start:end] ), file=f)
            move_to_parent_folder = True
            finalsettings.append( [ newsettingfile_completepath, outputpath + name + "/", name+"_"+str(i), fileval, end-start, d[start:end], move_to_parent_folder,i ] )
    return finalsettings

n = 1
inputs = []
inputs_files = []
if len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help","help"]]):
    print("Minimum required inputs are: inputpath, outputpath.\nAdditional inputs:")
    print("totalrt=0d0h0m -- Maximum runtime after which the calculation is aborted. Standard if not passed is 7 days. This is the runtime in every script. This will be used to calculate jobtype (short,batch,long) on noctua.")
    print("averagert=0d0h0m -- Predicted average runtime of any single calculation - If this is passed, the settingfile may be split into smaller chunks to ensure the anticipated jobtype can handle the input")
    print("cores=# -- Number of CPU cores to use.\n--ram=#g -- Gigabytes of ram to use" )
    exit()
input_path = (str(sys.argv[n]) if len(sys.argv) > n else input("Path: ")); n+=1
outputpath = str(sys.argv[n]) if len(sys.argv) > n and not sys.argv[n] == "-t" else "/scratch/hpc-prf-pdsm/dbauch/"; n+=1
total_runtime = "7d0h0m" if not any("totalrt=" in a for a in sys.argv) else [a for a in sys.argv if "totalrt=" in a][0].replace("totalrt=","")
average_runtime = -1 if not any("averagert=" in a for a in sys.argv) else [a for a in sys.argv if "averagert=" in a][0].replace("averagert=","")
cores = -1 if not any("cores" in a for a in sys.argv) else [a for a in sys.argv if "cores=" in a][0].replace("cores=","")
memory = -1 if not any("ram" in a for a in sys.argv) else [a for a in sys.argv if "ram=" in a][0].replace("ram=","")

startonly = [] if not any("startonly=" in a for a in sys.argv) else [a for a in sys.argv if "startonly=" in a][0].replace("startonly=","").split(",")

# Test whether we are on oculus or noctua:
#if os.system("squeue > /dev/null") == 0:
#    cluster = "noctua"
print("Using {} cluster...".format(cluster))

call = "ccsalloc" if cluster == "oculus" else "sbatch"

if "-t" in sys.argv:
    call = "echo " + call

# Find all Setting files for calculation
if input_path.endswith(".txt"):
    inputs_files.append(input_path)
else:
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.startswith("settings_") and file.endswith(".txt"):
                inputs_files.append(os.path.join(root, file))

# Extract name, path and eval string
for file in inputs_files:
    with open(file,"r", encoding="utf-8") as f:
        name = f.readline().split()[1]
        d = f.readlines()
        fileval = ""#[i for i in d if not i.startswith(" ")][-1]
        fileval = ""#fileval.split()[-1]
        num = len(d)-1
        move_to_parent_folder = True
        inputs.append([file, outputpath, name, fileval, num, d, move_to_parent_folder, 0])

# Split setting file into smaller ones if needed
inputs = split_settingfile(outputpath, inputs, anticipated_runtime=total_runtime, average_runtime=average_runtime)

if (len(startonly) > 0):
    print("Starting only jobs {}".format(startonly))

# Random Name Suffix:
suffix = str(randint(1000,9999))

# Start setting files
for (file, outputpath, name, fileval, num, d, move_to_parent_folder,i) in inputs:
    try:
        if (len(startonly) > 0 and not str(i) in startonly):
            continue
        ns = "QDLC_"+suffix+"_"+str(i)
        print("Trying to start job {} ({} files), Jobname will be {}... ".format(file,num,ns), flush = True)
        # Generate runscript:
        runscript = generate_runscript(runtime=total_runtime, cluster=cluster, cores=cores, mem=memory, settingfile=file, outputfolder=outputpath, move_results_to_parent_folder=move_to_parent_folder, subname=name,name = ns)
        # Folder Structure
        print("Generating output folder structure at {}".format(outputpath+name), flush=True)
        os.makedirs(os.path.join(outputpath,name),exist_ok=True)
        # Write runscript
        with open(os.path.join(outputpath,name,"run.sh"),"w") as f:
            print(runscript,file=f)
        os.system("chmod +x "+os.path.join(outputpath,name,"run.sh"))
        # Start Job
        fp = os.path.join(outputpath,name,"run.sh")
        print(f"Running {call} {fp} {name} {fileval}")
        os.system("{} {} {} {}".format(call, fp, name, fileval))
        print("Done!. ")
    except Exception as e:
        print("Failed!\n{}".format(e))
    sleep(1)