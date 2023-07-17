from typing import overload
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.animation as animation
import matplotlib.colors as colors
import numpy as np
from os.path import dirname, realpath, join
from math import ceil
import sys

from QDLC.misc.torned_bloch import Bloch
from QDLC.misc.generate_colormaps import generate_colormaps
from QDLC.misc.functionality import _guess_delimiter

def parseIndicesForBloch(index_str: str | tuple[str], names: list[str], parse_floats: bool = False):
    if not isinstance(index_str, (tuple,list)):
        index_str = index_str.split(",")
    print(f"Parsing indices {index_str}")
    def parse_index(index: str):
        # Replace Named indices with integer indices
        for key in names[1:]:
            if key in index:
                index = index.replace(key,f"{names.index(key)}") if not parse_floats else index.replace(key,f"float(values[{names.index(key)}])")
        # Returned index should be evaluable. If not, the parser will throw an error
        if not parse_floats:
            index = "float(values["+index.replace("+","])+float(values[").replace("-","])-float(values[").replace("*","])*float(values[").replace("/","])/float(values[")+"])"
        return index 
    indices = [ parse_index(index) for index in index_str ]
    print(f"Resulting index values: {indices}")
    return indices

# indices are re(p), im(p), f
def getValuesForBloch(filepath, indices = "1,2,3", no2f = False, parse_floats: bool = False, norm: bool = False):
    filepath = filepath
    print(f"Opening {filepath}")
    delim = _guess_delimiter(filepath)
    print("Delim is '{}'".format(delim))
    with open(filepath) as f:
        tdata = f.readlines()
        tdata = [d.split(delim)[:-1] for d in tdata if len(d.split(delim)[:-1]) > 0 and d.split(delim)[0] != "\n"]
        outt = []
        outd = []
        names = tdata[0]
        # Hack normalization
        tdata.pop(0)
        if norm:
            # Convert tdata to numpy matrix, normalize it columnwise and convert it back to list of lists
            try:
                tdata = np.array(tdata,dtype=float)
                tdata_normed = (tdata - tdata.min(axis=0)) / tdata.ptp(axis=0)
                tdata = tdata_normed.tolist()
                print("Normalized data.")
            except Exception as e:
                print(e)
                print("Error normalizing data. Skipping normalization.")
        try:
            indices = parseIndicesForBloch(indices, names, parse_floats)
        except ValueError:
            print(f"Error parsing indices {indices} from {names}. Make sure the indices are either integers or names of the columns in the first line of the file.")
            exit()
        for data in tdata:
            re,im,f = (eval(index,{"values": data}) for index in indices)
            if no2f:
                ndata = [re,im,f]
            else:
                ndata = [2.*re,-2.*im,2.*f-1.]
            t = float(data[0])
            outd.append( ndata )
            outt.append(t)
        print("Pulled data from {}".format(names))
    return outt,outd,names

from time import time_ns
def plotBlochSphereAnimated( path, index = ("1,2,3",), skip = 1, current_view = [-50,30], deltarot = [0,0], all_arrows = False, no2f = False, skipkind = "merge", iterations_max = 500000, video_bitrate = 5000, fps = 60, fontsize = 16, parse_floats = False, lw = 2, lwt = 2, norm=False, trail_points = None, cm = 'vik', cmsphere = 'Greys_r'):
    generate_colormaps()
    plt.rcParams.update({'font.size': fontsize})
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, metadata=dict(artist='Dogwit'), bitrate=video_bitrate)
    t,ostates,names = [],[],[]
    for indx in index:
        tt,oo,nn = getValuesForBloch(path,indx,no2f,parse_floats,norm)
        t.append(tt)
        ostates.append(oo)
        names.append(nn)

    if skipkind == "cut":
        t = [tt[::skip] for tt in t]
        ostates = [oo[::skip] for oo in ostates]
        iterations_max = min([min(iterations_max,len(oo)) for oo in ostates])
    else:
        iterations_max = min([min(iterations_max,int(1.*len(oo)/skip)) for oo in ostates])
    print("Iteration limit is {}".format(iterations_max))

    fig = plt.figure(figsize=(18,9), constrained_layout = True)
    gs = fig.add_gridspec(1,2,hspace=0.07, wspace=0.05)
    ax1 = fig.add_subplot(gs[0,0],projection='3d')
    ax2 = fig.add_subplot(gs[0,1])

    ax1.view_init(azim=current_view[0], elev=current_view[1])
    b = Bloch(fig=fig,axes=ax1,view=current_view)

    # Pre-Plot line graph
    for k in range(len(index)):
        ax2.plot(t[k],[o[2] for o in ostates[k]])
        ax2.plot(t[k],[o[0] for o in ostates[k]])
        ax2.plot(t[k],[o[1] for o in ostates[k]])
    # Get current Ax Lims
    xlim = ax2.get_xlim()
    ylim = ax2.get_ylim()

    ## customize sphere properties ##
    b.point_size = lw
    b.trail_point_size = lwt
    b.frame_width = max(lw,lwt)*1.25
    b.frame_color = "black"
    b.colormap_data = cm
    b.colormap_sphere = cmsphere
    
    x = [[] for i in range(len(index))]
    f = [[] for i in range(len(index))]
    pol1 = [[] for i in range(len(index))]
    pol2 = [[] for i in range(len(index))]

    def animate(i,ax1=ax1,ax2=ax2,b=b):
        #time = time_ns()
        ax1.clear()
        ax2.clear()
        ax2.set_xlim(*xlim)
        ax2.set_ylim(*ylim)
        b.vectors = []
        for k in range(len(index)):
            if skipkind == "cut":
                print(" -- Plotting at {:.1f}%, cur = {}".format(100.0*i/len(ostates[k]),ostates[k][i]), end="\r")
                b.add_vectors(ostates[k][i])
                if all_arrows:
                    b.add_vectors([ostates[k][i][0],0,0])                
                    b.add_vectors([0,ostates[k][i][1],0])                
                    b.add_vectors([0,0,ostates[k][i][2]])                
                b.add_points(ostates[k][i],current=k)
                x[k].append(t[k][i])
                f[k].append(ostates[k][i][2])
                pol1[k].append(ostates[k][i][0])
                pol2[k].append(ostates[k][i][1])
                if k == 0:
                    current_view[0] += deltarot[0]/len(ostates[0])
                    current_view[1] += deltarot[1]/len(ostates[0])
            elif i > 0:
                print(" -- Plotting at {:.1f}%, cur = {}".format(100.0*i*skip/len(ostates[k]),ostates[k][i]), end="\r")
                b.add_vectors(ostates[k][i*skip])
                if all_arrows:
                    b.add_vectors([ostates[k][i*skip][0],0,0])                
                    b.add_vectors([0,ostates[k][i*skip][1],0])                
                    b.add_vectors([0,0,ostates[k][i*skip][2]])
                for j in range(skip): ## todo: das hier besser haha. plot x[0:iteration] oder so. auf jeden fall slicing, nicht dieses append für 20000 werte kek.
                    l = (i-1)*skip+j
                    b.add_points(ostates[k][l],current=k)
                    x[k].append(t[k][l])
                    f[k].append(ostates[k][l][2])
                    pol1[k].append(ostates[k][l][0])
                    pol2[k].append(ostates[k][l][1])
                if k == 0:
                    current_view[0] += deltarot[0]*skip/len(ostates[k])
                    current_view[1] += deltarot[1]*skip/len(ostates[k])
            ax2.plot(x[k],f[k])
            ax2.plot(x[k],pol1[k])
            ax2.plot(x[k],pol2[k])
        b.render(trail_points)
        ax1.view_init(azim=current_view[0], elev=current_view[1])
        legend = []
        [legend.extend([str(k)+': 2f(t)-1' if not no2f else ": f(t)", str(k)+': 2Re(p)' if not no2f else ": Re(p)", str(k)+': -2Im(p)' if not no2f else ": Im(p)"]) for k in range(len(index))]
        ax2.legend(legend)
        ax2.set_xlim([np.min(t),np.max(t)])
        #print(f"Time took: {(time_ns()-time)/1e9} s")
        
    print("Creating animation")
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=iterations_max, repeat=True)
    print("Saving animation")
    ani.save(path.replace(".txt","_blochsphere.mp4"), writer=writer)
    print("Done")

if __name__ == "__main__":
    from matplotlib.pylab import mpl
    from matplotlib.pyplot import cm
    # Help
    if (len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help"]])):
        print("# Parameters:")
        print("#   --file=path            --  Path to File")
        print("#   --indices=re,im,f      --  Column Indices, either integers for column index or name of the column where the names are given in the first line of the File.")
        print("#   --skip=int             --  Only Render every X frame.")
        print("#   --view=Phi,Theta       --  Initial Rotation of the Blochsphere.")
        print("#   --deltarot=Phi,Theta   --  Rotate the view for a total of Phi and Theta over the duration of the video.")
        print("#   --bitrate=int          --  Bitrate of the video in kbit/s.")
        print("#   --fps=int              --  Frames per second.")
        print("#   --fontsize=int         --  Fontsize of the plot.")
        print("#   --lw[t]=float          --  Linewidth of the lines[trail].")
        print("#   --trail=int            --  Number of points to trail.")
        print("#   --cm=str               --  Colormap to use for data.")
        print("#   --cmsphere=str         --  Colormap to use for the sphere.")
        print("#   -allarrows             --  Also plot (2Re,0,0), (0,-2Im,0) and (0,0,2f-1) vectors.")
        print("#   -no2f                  --  Just bare input instead of 2f-1.")
        print("#   -nofloats              --  Parse floats as indices instead of floats.")
        print("#   -norm                  --  Normalizes the data before processing.")
        print("# Note that when omitting --file, the first argument is interpreted as the path to the target.")
        exit()

    fontsize = 16
    if any(["--fontsize=" in a for a in sys.argv]):
        fontsize = int([a.replace("--fontsize","") for a in sys.argv if "--fontisze" in a][0])
    fps = 60 if not any(["fps=" in a for a in sys.argv]) else int([a.replace("--fps=","") for a in sys.argv if "--fps=" in a][0])
    iterations_max = 500000
    video_bitrate = 500 if not any(["bitrate=" in a for a in sys.argv]) else int([a.replace("--bitrate=","") for a in sys.argv if "--bitrate=" in a][0])

    # REST
    path = dirname(realpath(__file__))
    
    if any(["--file=" in a for a in sys.argv]):
        path = [a.replace("--file=","") for a in sys.argv if "--file=" in a][0]
    elif not sys.argv[1].startswith("--"):
        path = sys.argv[1]
    else:
        path = join(path,"densitymatrix.txt")
    if any(["--indices=" in a for a in sys.argv]):
        index = [tuple(a.split(",")) for a in [a.replace("--indices=","").replace("^","") for a in sys.argv if "--indices=" in a]]
        print(index)
    else:
        print("Error: No indices given.")
        exit()

    if any(["--skip=" in a for a in sys.argv]):
        skip = int([a.replace("--skip=","") for a in sys.argv if "--skip=" in a][0])
    else:
        skip = 1

    if any(["--deltarot=" in a for a in sys.argv]):
        deltarot = [a.replace("--deltarot=","") for a in sys.argv if "--deltarot=" in a][0].split(",")
        deltarot = [float(deltarot[0]),float(deltarot[1])]
    else:
        deltarot = [0,0]
    
    all_arrows = "-allarrows" in sys.argv

    if any(["--view=" in a for a in sys.argv]):
        current_view = [a.replace("--view=","") for a in sys.argv if "--view=" in a][0].split(",")
        current_view = [int(current_view[0]),int(current_view[1])]
    else:
        current_view = [-50,30]

    lw = 2 if not any(["--lw=" in a for a in sys.argv]) else float([a.replace("--lw=","") for a in sys.argv if "--lw=" in a][0])
    lw_trail = 2 if not any(["--lwt=" in a for a in sys.argv]) else float([a.replace("--lwt=","") for a in sys.argv if "--lwt=" in a][0])
    
    trail_points = None if not any(["--trail=" in a for a in sys.argv]) else int([a.replace("--trail=","") for a in sys.argv if "--trail=" in a][0])
    cm = 'vik' if not any(["--cm=" in a for a in sys.argv]) else ([a.replace("--cm=","") for a in sys.argv if "--cm=" in a][0])
    cmsphere = 'Greys_r' if not any(["--cmsphere=" in a for a in sys.argv]) else ([a.replace("--cmsphere=","") for a in sys.argv if "--cmsphere=" in a][0])

    no2f = "-no2f" in sys.argv
    skipkind = "merge" if not "-cut" in sys.argv else "cut"

    parse_floats = not "-nofloats" in sys.argv
    norm = "-norm" in sys.argv

    print(f"Filepath is {path}")
    print(f"Bitrate is {video_bitrate} kbit/s")
    print(f"FPS is {fps}")
    print(f"Using indices {index} (Re(p), Im(p), f)")
    print(f"Plotting every {skip}")
    print(f"Initial view is {current_view}")
    print(f"Total delta view is {deltarot}")
    if trail_points:
        print(f"Trailing {trail_points} points")
    if all_arrows:
        print(f"Plotting all arrows")
    if no2f:
        print(f"Plotting f instead of 2f-1")
    if not parse_floats:
        print(f"Interpreting indices as floats")


    plotBlochSphereAnimated(path, index, skip, current_view, deltarot, all_arrows, no2f, skipkind, iterations_max, video_bitrate, fps, fontsize, parse_floats, lw, lw_trail, norm, trail_points, cm, cmsphere)