import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath, join
from sys import argv
from math import ceil, floor, sqrt
from scipy.interpolate import interp2d as interpolator
from QDLC.misc.generate_colormaps import generate_colormaps
import string 

from QDLC.misc.functionality import _reshape_data_set, _get_data_header, _input_to_tuple, _guess_delimiter

"""
todo: 
- seperate line, matrix plot
- make pretty, reuse functionality.py and extend it
- remove interpolator, unnecessary
"""
def plot_matrix(totalpath, cmap = "turbo", delim = "auto", fformat = "pdf", ranges = "auto", indices = "auto", shading = "gouraud", use_cbs = True, logscale = False, colorrepeat = 1, levels = "mesh", mode = "matrix"):
    print(f"Plotting {totalpath}")
    print(f"Colormap used: {cmap}")
    print(f"Format used: {fformat}")

    if not ranges == "auto":
        #ranges_x_min, ranges_x_max, ranges_y_min, ranges_y_max, ranges_z_min, ranges_z_max = _input_to_tuple(ranges, delimiter = ":")
        ranges = ranges.split(",")
        print(f"Ranges used: X from {ranges[0]} to {ranges[1]}; Y from {ranges[2]} to {ranges[3]}; Z from {ranges[4]} to {ranges[5]}")

    if not indices == "auto":
        indices = [int(a) for a in indices.split(",")]
    print(f"Indices = {indices}")

    # Data
    print(f"Reading files...")
    #datapoints = 400.0
    #max_sourcepoints = datapoints*datapoints
    #if interpolate:
    #    print(f"Interpolating the values onto a {int(datapoints)}x{int(datapoints)} Grid first...")

    totaldata = {}
    finalpath = totalpath.split(";")[0]
    for index,path in enumerate(totalpath.split(";")):
        header = _get_data_header(path, delimiter=" ").split()
        if not header[0].isnumeric():
            comments = header
        else:
            comments = ["#"] + list(string.ascii_letters)
        print(comments)
        delim = _guess_delimiter(path)
        if delim == "auto":
            try:
                data = np.loadtxt(path, delimiter="\t", unpack=True, comments = comments)
            except ValueError:
                try:    
                    data = np.loadtxt(path, delimiter=" ", unpack=True, comments = comments)
                except ValueError:
                    print("Could not automatically determine delimiter!")
        else:
            data = np.loadtxt(path, delimiter=delim, unpack=True, comments = comments)
        if mode == "matrix":
            y = data[0]; 
            x = data[1]; 
            v = data[1:] if indices == "auto" else data[2:2+indices[index]]
        else:
            x = data[0]
            y = None
            v = data[1:] if indices == "auto" else data[2:2+indices[index]]

        if logscale:
            v = [np.log10(vv+np.min(vv[np.nonzero(vv)])) for vv in v]
            [print(f"{np.min(vv)} {np.max(vv)}") for vv in v]

        if colorrepeat > 1:
            v = [ np.min(vv) + np.mod((vv-np.min(vv))/(np.max(vv)-np.min(vv))*colorrepeat,1.0)*np.max(vv) for vv in v ]
        #if interpolate:
        #    nv = []
        #    ranges = (np.min(x), np.max(x), np.min(y), np.max(y))
        #    print(f"Interpolation Ranges are: {ranges}")
        #    xnew = np.arange(ranges[0], ranges[1], (ranges[1]-ranges[0])/datapoints)
        #    ynew = np.arange(ranges[2], ranges[3], (ranges[3]-ranges[2])/datapoints)
        #    if len(x) > max_sourcepoints:
        #        cutoff_it = floor(len(x)/max_sourcepoints)
        #        x = x[::cutoff_it]
        #        y = y[::cutoff_it]
        #    for i,vv in enumerate(v):
        #        if len(vv) > max_sourcepoints:
        #            vv = vv[::cutoff_it]
        #        print(f"Interpolating Dataset {i} (length: {len(vv)})... ",end="",flush=True)
        #        f = interpolator(x,y,vv,copy=False)
        #        print("Appending Result...")
        #        nv.append(f(xnew, ynew)).flatten()
        #    v = nv
        n,m = 0,0
        #if mode == "matrix":
        #    n = len(set(x))
        #    m = int(len(v[0])/n)
        #    try:
        #        p = np.reshape(y,(m,n))
        #    except:
        #        m = len(set(y))
        #        n = int(len(v[0])/m)
        #    # Reshape
        #    y = np.reshape(y,(m,n))
        #    x = np.reshape(x,(m,n))
        #    v = [np.reshape(a,(m,n)) for a in v]
        #    print(f"Matrix Dimensions are {n}x{m}")
        totaldata[path] = {"header" : header[-len(v):], "x" : x, "y" : y, "v" : v, "n" : n, "m" : m, "ranges" : ranges }

    if use_cbs and len(ranges) > 4 and any([ranges[4] != "auto", ranges[5] != "auto"]):
        print("Warning! -cbs is used, which will make --ranges=,,,,z0,z1 be ignored!!") 

    totalsize = sum(len(a["v"]) for a in totaldata.values())
    
    dimx = floor(sqrt(totalsize))
    dimy = ceil(totalsize/dimx)
    # Figure and Grid
    fig = plt.figure(figsize=(16,9))
    gs = fig.add_gridspec(dimx,dimy,hspace=0.15, wspace=0.15)

    # Axes
    iterator = [(i,j) for i in range(dimx) for j in range(dimy)]
    ax = [fig.add_subplot(gs[i,j]) for (i,j) in iterator]
    if mode == "matrix":
        [a.label_outer() for a in ax]

    ax_index = 0
    plts = []
    for path,plot in totaldata.items():
        header,x,y,v,n,m,ranges = plot["header"],plot["x"],plot["y"],plot["v"],plot["n"],plot["m"],plot["ranges"]
        if not ranges == "auto" and not ranges[0] == "auto":
            [a.set_xlim(float(ranges[0]) if not ranges[0] == "auto" else None, float(ranges[1]) if not ranges[1] == "auto" else None) for a in ax[ax_index:ax_index+len(v)]]
            [a.set_ylim(float(ranges[2]) if not ranges[2] == "auto" else None, float(ranges[3]) if not ranges[3] == "auto" else None) for a in ax[ax_index:ax_index+len(v)]]


        total_max = (np.max([np.max(m) for m in v]) if (ranges == "auto" or ranges[5] == "auto") else float(ranges[5])) if not use_cbs else None
        total_min = (np.min([np.min(m) for m in v]) if (ranges == "auto" or ranges[4] == "auto") else float(ranges[4])) if not use_cbs else None

        # Plots
        print(f"Plotting, range settings are {total_min},{total_max}..." )
        if mode == "matrix":
            if levels == "mesh":
                plts.extend([axi.tripcolor(x,y,a, cmap = cmap, edgecolors='none',shading=shading, vmin=total_min, vmax = total_max, rasterized=True) for (a,axi) in zip(v,ax[ax_index:ax_index+len(v)])])
                [p.set_edgecolor('face') for p in plts]
            else:
                plts.extend([axi.tricontourf(x,y,a, cmap = cmap, levels = np.linspace(total_min, total_max, levels+1),shading=shading) for (a,axi) in zip(v,ax[ax_index:ax_index+len(v)])])
                [ c.set_rasterized(True) for c in plts[-1].collections ]
        else:
            plts.extend([axi.plot(x,a,'o', linewidth=0, markersize = 0.5) for (a,axi) in zip(v,ax[ax_index:ax_index+len(v)])])            
        annatation_color = 'w' if mode == "matrix" else 'black'
        [axi.text(0.99, 0.99, head , transform=axi.transAxes, fontweight='regular', va='top', ha='right', color=annatation_color, fontsize='small') for axi,head in zip(ax[ax_index:ax_index+len(v)],header)]
        ax_index += len(v)
    print(f"================= mode = {mode}")
    if mode == "matrix":
        # Colorbar
        if use_cbs:
            cbs = [fig.colorbar(plti, ax=axi, shrink=1,pad=0.02) for (plti,axi) in zip(plts,ax)]
        else:
            cbs = fig.colorbar(plts[-1], ax=ax, shrink=1,pad=0.02)
        #[cb.ax.tick_params(labelsize=5) for cb in cbs]

    if "show" in argv or "-show" in argv or "-s" in argv or "--show" in argv:
        plt.show()
    else:
        print("Saving to " + finalpath.replace(".txt","."+fformat))
        plt.savefig(finalpath.replace(".txt","."+fformat),dpi = 400)

if __name__ == "__main__":
    path = dirname(realpath(__file__))
    colormap = 'turbo' if not any(["--colormap=" in a for a in argv]) else [ a.replace("--colormap=","") for a in argv if "--colormap=" in a ][0]
    generate_colormaps()
    totalpath = argv[1] if not "--" in argv[1] else [ a.replace("--file=","") for a in argv if "--file=" in a ][0]
    delim = 'auto' if not any(["--delim=" in a for a in argv])else [ a.replace("--delim=","") for a in argv if "--delim=" in a ][0]
    fformat = "pdf" if not any(["--format=" in a for a in argv]) else [ a.replace("--format=","") for a in argv if "--format=" in a ][0]
    ranges = "auto" if not any(["--ranges=" in a for a in argv]) else [ a.replace("--ranges=","") for a in argv if "--ranges=" in a ][0]
    indices = "auto" if not any(["--indices=" in a for a in argv]) else [ a.replace("--indices=","") for a in argv if "--indices=" in a ][0]
    shading = "gouraud" if not any(["--shading=" in a for a in argv]) else [ a.replace("--shading=","") for a in argv if "--shading=" in a ][0]
    levels = "mesh" if not any(["--levels=" in a for a in argv]) else [ int(a.replace("--levels=","")) for a in argv if "--levels=" in a ][0]
    use_cbs = "-cbs" in argv
    logscale = "-ls" in argv
    colorrepeat = 1 if not any(["--crepeat=" in a for a in argv]) else [ int(a.replace("--crepeat=","")) for a in argv if "--crepeat=" in a ][0]
    # Readin Method. "squared" will use np.loadtxt, "interpolate" will use open() and range through the different blocks, interpolating the results onto an NxN matrix, where N is the maximum dimension of either X or Y
    interpolate = "-interpolate" in argv

    plot_matrix(totalpath, colormap, delim, fformat, ranges, indices, shading, use_cbs, logscale, colorrepeat, levels, "matrix")