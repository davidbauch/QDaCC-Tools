import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
import matplotlib
import matplotlib.animation as animation
import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath, join
from math import ceil
from sys import argv
from mpl_toolkits.mplot3d import Axes3D
from QDLC.misc.generate_colormaps import generate_colormaps

def getVals(filepath, indices = (0,-1),norm_to_one = False):
    filepath = filepath
    print(f"Opening {filepath}")
    with open(filepath) as f:
        tdata = f.readlines()
        tdata = [d.split("\t")[:-1] for d in tdata]
        outt = []
        outd = []
        names = tdata[0][1:][indices[0]:indices[1]] if indices[1] != -1 else tdata[0][1:][indices[0]:]
        for data in tdata[1:]:
            data = data[indices[0]:indices[1]] if indices[1] != -1 else data[indices[0]:]
            ndata = [float(d) for d in data]
            t = float(data[0]);
            dim = int(np.sqrt(len(ndata)-1))
            outd.append( np.reshape(ndata[1:],( dim,dim )) )
            if norm_to_one:
                outd[-1] = np.where(outd[-1] != 0.0,1,0)
            outt.append(t)
        print("Pulled data from {}".format(names[:-1]))
    return outt,outd,names,dim

if __name__ == "__main__":
    # CONFIGURATION
    fps = 60 if not any(["fps=" in a for a in argv]) else int([a.replace("--fps=","") for a in argv if "--fps=" in a][0])
    iterations_max = 2000
    video_bitrate = 5000 if not any(["bitrate=" in a for a in argv]) else int([a.replace("--bitrate=","") for a in argv if "--bitrate=" in a][0])
    indices = (0,-1) # from,to snytax, first index is always assumed to be time
    fontsize = 15

    if any("--fontsize=" in a for a in argv):
        fontsize = int([a.replace("--fontsize","") for a in argv if "--fontisze" in a][0])

    # REST
    path = dirname(realpath(__file__))
    plt.rcParams.update({'font.size': fontsize})
    
    if any(["--file=" in a for a in argv]):
        path = [a.replace("--file=","") for a in argv if "--file=" in a][0]
    elif len(argv) == 2 and not any("--" in a for a in argv):
        path = argv[-1]
    else:
        path = join(path,"densitymatrix.txt")
    if any(["--indices=" in a for a in argv]):
        indices = tuple(int(b) for b in [a.replace("--indices=","") for a in argv if "--indices=" in a][0].split(","))
        indices = (indices[0],indices[1]+1)

    if any(["--skip=" in a for a in argv]):
        skip = int([a.replace("--skip=","") for a in argv if "--skip=" in a][0])
    else:
        skip = 1

    norm_to_one = "-normToOne" in argv


    print("Filepath is " + path)
    print("Bitrate is {} kbit/s".format(video_bitrate))
    print("FPS is {}".format(fps))
    print("Using index range {}".format(indices))
    print("Plotting every {} ".format(skip))

    # Colormap
    colormap = 'turbo' if not any(["--colormap=" in a for a in argv]) else [ a.replace("--colormap=","") for a in argv if "--colormap=" in a ][0]
    generate_colormaps()
    cmap =  matplotlib.cm.get_cmap(colormap)
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, metadata=dict(artist='Dogwit'), bitrate=video_bitrate)
    t,out,names,dim = getVals(path,indices,norm_to_one)
    
    print("Matrix dimension will be {}".format(dim))

    dim3 = any(["-3d" in a for a in argv])
    if dim3:
        print("Using 3d projection")
    useboth = any(["-both" in a for a in argv])
    if (useboth):
        print("Using both 3d projection and matshow")
        dim3 = True

    fig = plt.figure(figsize=(18 if not useboth else 36,18), constrained_layout = True)
    gs = fig.add_gridspec(1,1 if not useboth else 2,hspace=0.07, wspace=0.05)
    ax1 = fig.add_subplot(gs[0,0], projection='3d') if dim3 else fig.add_subplot(gs[0,0])
    if useboth:
        ax2 = fig.add_subplot(gs[0,1])

    if any(["-names" in a for a in argv]):
        if any(["--names=" in a for a in argv]):
            names = [a.replace("--names=","").split(",") for a in argv if "--names=" in a][0]
        print(f"Using names = {names}")
        ax1.set_xticks(np.linspace(0,len(names),len(names)))
        ax1.set_yticks(np.linspace(0,len(names),len(names)))
        ax1.set_xticklabels(names)
        ax1.set_yticklabels(names)
        if useboth:
            ax2.set_xticks(np.linspace(0,len(names),len(names)))
            ax2.set_yticks(np.linspace(0,len(names),len(names)))
            ax2.set_xticklabels(names)
            ax2.set_yticklabels(names)
    
    mmin, mmax = (np.min( [np.min(a) for a in out] ), np.max( [np.max(a) for a in out] )) if not any(["--mm=" in a for a in argv]) else [(float(b) for b in a.replace("--mm=","").split(",")) for a in argv if "--mm=" in a][0] 
    print("Minimum is {}".format(mmin))
    print("Maximum is {}".format(mmax))

    X,Y = np.meshgrid(np.linspace(0, out[0].shape[0],out[0].shape[0]), np.linspace(0, out[0].shape[1],out[0].shape[1]))
    
    bottom = np.zeros_like(out[0]);
    barcolors = [  cmap(np.array((mat-mmin)/(mmax-mmin)).ravel()) for mat in out ] if dim3 else []
    
    plt1 = ax1.bar3d(X.ravel(),Y.ravel(),bottom.ravel(),1,1,out[0].ravel(), color = barcolors[0], shade=True) if dim3 else ax1.matshow(out[0], cmap = cmap, vmin = mmin, vmax = mmax)
    if useboth:
        plt2 = ax2.matshow(out[0], cmap = cmap, vmin = mmin, vmax = mmax)
    if ("-cb" in argv):
        if useboth:
            cbs = fig.colorbar(plt1, ax=[ax1,ax2], shrink=1,pad=0.02)
        else:
            cbs = fig.colorbar(plt1, ax=ax1, shrink=1,pad=0.02)

    if dim3:
        ax1.set_zlim(mmin, mmax)
    iterations_max = int(np.floor(min(iterations_max, len(out))/skip))

    def animate(i):
        global t,out,plt1,ax1
        ci = min(int(ceil(len(t)/iterations_max*i)),len(t)-1)
        print(" -- Plotting at {:.1f}%".format(100.0*ci/len(out)), end="\r")
        ax1.clear()
        plt1 = ax1.bar3d(X.ravel(),Y.ravel(),bottom.ravel(),1,1,out[ci].ravel(), color = barcolors[ci], shade=True) if dim3 else ax1.matshow(out[ci], cmap = cmap, vmin = mmin, vmax = mmax)
        if useboth:
            ax2.clear()
            plt2 = ax2.matshow(out[ci], cmap = cmap, vmin = mmin, vmax = mmax)
        if dim3:
            ax1.set_zlim(mmin, mmax)
        #plt1.title(f"T = {t[i]}")

    print("Creating animation")
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=iterations_max, repeat=True)
    print("Saving animation")
    ani.save(path.replace(".txt",".mp4"), writer=writer)
    print("Done")
    exit()
