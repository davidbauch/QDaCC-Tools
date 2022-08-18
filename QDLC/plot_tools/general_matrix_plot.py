import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath, join
from sys import argv
from math import ceil, floor, sqrt
from scipy.interpolate import interp2d as interpolator

from QDLC.misc.colormaps import get_colormap

def plot_matrix():
    path = dirname(realpath(__file__))
    colormap = 'turbo' if not any(["--colormap=" in a for a in argv]) else [ a.replace("--colormap=","") for a in argv if "--colormap=" in a ][0]
    cmap = get_colormap(colormap)

    totalpath = argv[1] if not "--" in argv[1] else [ a.replace("--file=","") for a in argv if "--file=" in a ][0]
    delim = '\t' if not any(["--delim=" in a for a in argv])else [ a.replace("--delim=","") for a in argv if "--delim=" in a ][0]
    fformat = ".png" if not any(["--format=" in a for a in argv]) else [ a.replace("--format=","") for a in argv if "--format=" in a ][0]
    ranges = "auto" if not any(["--ranges=" in a for a in argv]) else [ a.replace("--ranges=","") for a in argv if "--ranges=" in a ][0]
    indices = "auto" if not any(["--indices=" in a for a in argv]) else [ a.replace("--indices=","") for a in argv if "--indices=" in a ][0]
    shading = "nearest" if not any(["--shading=" in a for a in argv]) else [ a.replace("--shading=","") for a in argv if "--shading=" in a ][0]
    use_cbs = "-cbs" in argv
    logscale = "-ls" in argv
    colorrepeat = 1 if not any(["--crepeat=" in a for a in argv]) else [ int(a.replace("--crepeat=","")) for a in argv if "--crepeat=" in a ][0]

    print(f"Plotting {totalpath}")
    print(f"Colormap used: {colormap}")
    print(f"Format used: {fformat}")
    if not ranges == "auto":
        ranges = ranges.split(",")
        print(f"Ranges used: X from {ranges[0]} to {ranges[1]}; Y from {ranges[2]} to {ranges[3]}; Z from {ranges[4]} to {ranges[5]}")
    if not indices == "auto":
        indices = [int(a) for a in indices.split(",")]

    # Readin Method. "squared" will use np.loadtxt, "interpolate" will use open() and range through the different blocks, interpolating the results onto an NxN matrix, where N is the maximum dimension of either X or Y
    interpolate = "-interpolate" in argv

    # Data
    print(f"Reading files...")
    datapoints = 400.0
    max_sourcepoints = datapoints*datapoints
    if interpolate:
        print(f"Interpolating the values onto a {int(datapoints)}x{int(datapoints)} Grid first...")

    totaldata = {}
    finalpath = totalpath.split(";")[0]
    for index,path in enumerate(totalpath.split(";")):
        with open(path,"r") as f:
            header = f.readline().split()[1:]
        data = np.loadtxt(path, delimiter=delim, unpack=True, comments  = ["#","None","Time","t","x","y","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
        y = data[0]; 
        x = data[1]; 
        v = data[2:] if indices == "auto" else data[2:2+indices[index]]
        if logscale:
            v = [np.log10(vv+np.min(vv[np.nonzero(vv)])) for vv in v]
            [print(f"{np.min(vv)} {np.max(vv)}") for vv in v]

        if colorrepeat > 1:
            v = [ np.min(vv) + np.mod((vv-np.min(vv))/(np.max(vv)-np.min(vv))*colorrepeat,1.0)*np.max(vv) for vv in v ]
        if interpolate:
            nv = []
            ranges = (np.min(x), np.max(x), np.min(y), np.max(y))
            print(f"Interpolation Ranges are: {ranges}")
            xnew = np.arange(ranges[0], ranges[1], (ranges[1]-ranges[0])/datapoints)
            ynew = np.arange(ranges[2], ranges[3], (ranges[3]-ranges[2])/datapoints)
            if len(x) > max_sourcepoints:
                cutoff_it = floor(len(x)/max_sourcepoints)
                x = x[::cutoff_it]
                y = y[::cutoff_it]
            for i,vv in enumerate(v):
                if len(vv) > max_sourcepoints:
                    vv = vv[::cutoff_it]
                print(f"Interpolating Dataset {i} (length: {len(vv)})... ",end="",flush=True)
                f = interpolator(x,y,vv,copy=False)
                print("Appending Result...")
                nv.append(f(xnew, ynew)).flatten()
            v = nv
        n = len(set(x))
        m = int(len(v[0])/n)
        try:
            p = np.reshape(y,(m,n))
        except:
            m = len(set(y))
            n = int(len(v[0])/m)
        # Reshape
        y = np.reshape(y,(m,n))
        x = np.reshape(x,(m,n))
        v = [np.reshape(a,(m,n)) for a in v]
        print(f"Matrix Dimensions are {n}x{m}")
        totaldata[path] = {"header" : header, "x" : x, "y" : y, "v" : v, "n" : n, "m" : m, "ranges" : ranges }

    totalsize = sum(len(a["v"]) for a in totaldata.values())
    
    dimx = floor(sqrt(totalsize))
    dimy = ceil(totalsize/dimx)
    # Figure and Grid
    fig = plt.figure(figsize=(16,9))
    gs = fig.add_gridspec(dimx,dimy,hspace=0.1, wspace=0.1)

    # Axes
    iterator = [(i,j) for i in range(dimx) for j in range(dimy)]
    ax = [fig.add_subplot(gs[i,j]) for (i,j) in iterator]
    
    [a.label_outer() for a in ax]

    ax_index = 0
    plts = []
    for path,plot in totaldata.items():
        header,x,y,v,n,m,ranges = plot["header"],plot["x"],plot["y"],plot["v"],plot["n"],plot["m"],plot["ranges"]
        if not ranges == "auto" and not ranges[0] == "auto":
            [a.set_xlim(float(ranges[0]) if not ranges[0] == "auto" else None, float(ranges[1]) if not ranges[1] == "auto" else None) for a in ax[ax_index:ax_index+len(v)]]
            [a.set_ylim(float(ranges[2]) if not ranges[2] == "auto" else None, float(ranges[3]) if not ranges[3] == "auto" else None) for a in ax[ax_index:ax_index+len(v)]]


        total_max = np.max([np.max(m) for m in v]) if (ranges == "auto" or ranges[5] == "auto") else float(ranges[5])
        total_min = np.min([np.min(m) for m in v]) if (ranges == "auto" or ranges[4] == "auto") else float(ranges[4])
        # Plots
        print("Plotting...")
        plts.extend([axi.pcolormesh(x,y,a, cmap = cmap, edgecolors='none',shading=shading, vmin=total_min, vmax = total_max) for (a,axi) in zip(v,ax[ax_index:ax_index+len(v)])])
        [p.set_edgecolor('face') for p in plts]
        if len(ax) == len(header):
            [axi.text(0.99, 0.99, head , transform=axi.transAxes, fontweight='regular', va='top', ha='right', color='w', fontsize='small') for axi,head in zip(ax[ax_index:ax_index+len(v)],header)]
        ax_index += len(v)
    # Colorbar
    if use_cbs:
        cbs = [fig.colorbar(plti, ax=axi, shrink=1,pad=0.02) for (plti,axi) in zip(plts,ax)]
    else:
        cbs = fig.colorbar(plts[0], ax=ax, shrink=1,pad=0.02)
    #[cb.ax.tick_params(labelsize=5) for cb in cbs]

    if "show" in argv or "-show" in argv or "-s" in argv or "--show" in argv:
        plt.show()
    else:
        print("Saving to " + finalpath.replace(".txt","."+fformat))
        plt.savefig(finalpath.replace(".txt","."+fformat),dpi = 400)

if __name__ == "__main__":
    plot_matrix()