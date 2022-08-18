import sys, os
from math import sqrt

def get_line(file, delim = None, indices = ("None", "None"), suffix = "gnuplot"):
    with open(file, "r") as f:
        print(f"Processing {file}...")
        last_line = f.readlines()[-1].replace("\n","").replace("\t"," ").split(delim)
        fr = 0 if indices[0] == "None" else int(indices[0])
        to = len(last_line) if indices[1] == "None" else int(indices[1])
        last_line = last_line[fr:to]
        n = int(sqrt( len(last_line) ))
        print(indices,fr,to,n)
        print(f"Dimensions are {n}x{n}")

        # Matrix, Boxplot
        with open(file.replace(".txt","_"+suffix+"matrix.txt"),"w") as fo:
            with open(file.replace(".txt","_"+suffix+"box.txt"),"w") as fb:
                for i in range(n):
                    for j in range(n):
                        index = i*n+j
                        print(f"{last_line[index]}",end = " ",file=fo)
                        print(f"{i} {j} {last_line[index]}",file=fb)
                    print("",file=fo)


if __name__=="__main__":

    if len(sys.argv) < 2 or any(a in sys.argv for a in ["--help","-h"]):
        print("This Program extracts the final line of a file and outputs two new files formatted for gnuplot's matrix and box plots.")
        print("The first argument of this program is the filepath. Multiple files can be seperated by ';")
        print(" --delim=[delimitor]  -  Delimitor. Standard is ' '")
        print(" --indices=[from,to]  -  From-To indices to extract. Standard is None,None, meaning all values are extracted." )
        print(" --suffix=[suffix]    -  File addon. Standard is '_gnuplot[box/matrix]'." )
        exit()

    files = sys.argv[1].split(";")
    delim = " " if not any(["--delim=" in a for a in sys.argv]) else [a.replace("--delim=","") for a in sys.argv if "--delim=" in a][-1]
    suffix = "gnuplot" if not any(["--suffix=" in a for a in sys.argv]) else [a.replace("--suffix=","") for a in sys.argv if "--suffix=" in a][-1]
    indices = ("None","None") if not any(["--indices=" in a for a in sys.argv]) else [a.replace("--indices=","") for a in sys.argv if "--indices=" in a][-1].split(",")
    for file in files:
        get_line(file, delim, indices, suffix)