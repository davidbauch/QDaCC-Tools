import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath
from sys import argv
from math import ceil
import sys
sys.path.append('../../QDLC')
from QDLC.misc.colormaps import get_colormap_string

def plotstring_generate_abitrary(filename = "", shading = "nearest", index_offset = (2,1), cbs = False, colormap = "turbo", delim = " "):
    ranges = {"conc" : ("0","1"), "indist" : ("0","1")}
    if any([a in filename for a in ranges.keys()]):
        r = ranges[ [a for a in ranges.keys() if a in filename ][0] ]
    else:
        r = ("np.min([np.min(m) for m in v])", "np.max([np.max(m) for m in v])")
    return """import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath
from sys import argv
from math import ceil, floor, sqrt
from QDLC.misc.colormaps import get_colormap

if __name__ == "__main__":
    path = dirname(realpath(__file__))

    """+get_colormap_string(colormap)+"""

    with open(path + "/out_"""+filename+"""","r") as f:
        header = f.readline().split()["""+str(index_offset[1])+""":]

    # Data
    data = np.loadtxt(path + "/out_"""+filename+"""", delimiter='"""+delim+"""', unpack=True, comments  = ["#","None","Time","w","Omega","t","x","y","lfc"])
    y = data[0]; 
    x = data[1]; 
    v = data["""+str(index_offset[0])+""":]
    n = len(set(x))
    m = int(len(v[0])/n)
    try:
        p = np.reshape(y,(m,n))
    except:
        m = len(set(y))
        n = int(len(v[0])/m)
    print(f"Matrix Dimensions are {n}x{m}")
    
    # Reshape
    y = np.reshape(y,(m,n))
    x = np.reshape(x,(m,n))
    v = [np.reshape(a,(m,n)) for a in v]

    dimx = floor(sqrt(len(v)))
    dimy = ceil(len(v)/dimx)
    # Figure and Grid
    fig = plt.figure(figsize=(16,9))
    gs = fig.add_gridspec(dimx,dimy,hspace=0.1, wspace=0.1)

    # Axes
    iterator = [(i,j) for i in range(dimx) for j in range(dimy)]
    ax = [fig.add_subplot(gs[i,j]) for (i,j) in iterator]
    
    [a.label_outer() for a in ax]

    total_max = """+(r[1] if cbs else "None")+"""
    total_min = """+(r[0] if cbs else "None")+"""
    # Plots
    plts = [axi.pcolormesh(x,y,a, cmap = cmap, edgecolors='none',shading='"""+shading+"""', vmin=total_min, vmax = total_max) for (a,axi) in zip(v,ax)]
    [p.set_edgecolor('face') for p in plts]
    # Colorbar
    """+("#" if cbs else "")+"""cbs = [fig.colorbar(plti, ax=axi, shrink=1,pad=0.02) for (plti,axi) in zip(plts,ax)]
    """+("#" if not cbs else "")+"""cbs = fig.colorbar(plts[0], ax=ax, shrink=1,pad=0.02)
    #[cb.ax.tick_params(labelsize=5) for cb in cbs]
    #if len(ax) == len(header):
    [axi.text(0.99, 0.99, head , transform=axi.transAxes, fontweight='regular', va='top', ha='right', color='w', fontsize='small') for axi,head in zip(ax,header)]

    if "show" in argv or "-show" in argv or "-s" in argv or "--show" in argv:
        plt.show()
    else:
        print("Saving to " + path + "/"""+filename+""".png")
        plt.savefig(path + "/"""+filename+""".png",dpi = 400)"""