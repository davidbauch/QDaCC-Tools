# Extracts all runtimes from logfile

import os
import sys

input_path = str(sys.argv[1]) if len(sys.argv) > 1 else input("Path: ")
key = str(sys.argv[2]) if len(sys.argv) > 2 else input("Key: ")
output_name = "time.txt"
input_path = input_path.replace("\\", "/")
use_lfc = "-lfc" in sys.argv
output = []

def time_to_str(time):
    time = time.split(":")
    ret = ""
    for entry in time:
        if not "ms" in entry:
            ret += entry
    h,m,s = "0","0","0"
    print("from " + str(time) + " to " +  ret)
    if "h" in ret:
        h = ret.split("h")[0]
        ret = ret.split("h")[1]
    if "m" in ret:
        m = ret.split("m")[0]
        ret = ret.split("m")[1]
    if "s" in ret:
        s = ret.split("s")[0]
    #ret = h + "h" + m + "m" + s + "s"
    ret = str(60*int(h) + int(m)) + "m" + s + "s"
    return ret, str(60*60*int(h) + 60*int(m) + int(s))

for root, dirs, files in os.walk(input_path):
    for file in files:
        if file == "logfile.log":
            with open(os.path.join(root, file),"r") as f:
                data = f.readlines()
                new = []
                index = ""
                for line in data:
                    if "Walltime" in line and key in line:
                        line = line.split()
                        timestr1, timesec1 = time_to_str(line[3])
                        timestr2, timesec2 = time_to_str(line[5])
                        new.append( [line[0], timestr1, timesec1, timestr2, timesec2] )
                    if "--lfc" in line:
                        index = line.split("--lfc")[-1].split()[0]
                output.append([root[-1] if not use_lfc else index] + new)

output.sort(key = lambda entry : float(entry[0].split(",")[0]))
with open(os.path.join(input_path, output_name),"w") as f:
    for line in output:
        print(line[0] + "\t",end="",file=f)
        for set in line[1:]:
            if set[0] == key:
                print("\t".join(set[1:]),file=f)
