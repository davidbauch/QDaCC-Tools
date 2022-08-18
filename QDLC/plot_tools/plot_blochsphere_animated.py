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

import warnings
warnings.filterwarnings("ignore",lineno=0)

# indices are re(p), im(p), f
def getVals(filepath, indices = (1,2,3)):
    filepath = filepath
    print(f"Opening {filepath}")
    with open(filepath) as f:
        tdata = f.readlines()
        tdata = [d.split("\t")[:-1] for d in tdata]
        outt = []
        outd = []
        try:
            int(int(indices[0]))
            names = [tdata[0][int(indices[0])],tdata[0][int(indices[1])],tdata[0][int(indices[2])]]
        except:
            names = [indices[0],indices[1],indices[2]]
            indices = (str(tdata[0].index(indices[0])) if not "-" in indices[0] else str(tdata[0].index(indices[0].split("-")[0]))+"-"+(tdata[0].index(indices[0].split("-")[1])),
            str(tdata[0].index(indices[1])) if not "-" in indices[1] else str(tdata[0].index(indices[1].split("-")[0]))+"-"+str(tdata[0].index(indices[1].split("-")[1])),
            str(tdata[0].index(indices[2])) if not "-" in indices[2] else str(tdata[0].index(indices[2].split("-")[0]))+"-"+str(tdata[0].index(indices[2].split("-")[1])))
            print("Transcripting indices to {}".format(indices))
        for data in tdata[1:]:
            #ndata = [float(d) for i,d in enumerate(data) if i in indices]
            f = float(data[int(indices[2])]) if not "-" in indices[2] else float(data[int(indices[2].split("-")[0])])-float(data[int(indices[2].split("-")[1])])
            re = float(data[int(indices[0])]) if not "-" in indices[0] else float(data[int(indices[0].split("-")[0])])-float(data[int(indices[0].split("-")[1])])
            im = float(data[int(indices[1])]) if not "-" in indices[1] else float(data[int(indices[1].split("-")[0])])-float(data[int(indices[1].split("-")[1])])
            ndata = [2.*re,-2.*im,2.*f-1.]
            t = float(data[0]);
            outd.append( ndata )
            outt.append(t)
        print("Pulled data from {}".format(names))
    return outt,outd,names

from pylab import *
from qutip import *
# Modify the Bloch class to not be retarded with the plots lel
class BBloch(Bloch):
    def __init__(self, fig=None, axes=None, view=None, figsize=None, background=False):
        super().__init__(fig,axes,view,figsize,background)
        self.trajectory = [[[],[],[]]] # [[px,py,pz],[px2,py2,pz2],...]
        self.zlabel = [r'$\left|1\right>$', r'$\left|0\right>$']
    def add_points(self, points, current = 0, meth='s'):
        super().add_points(points,meth)
        if not isinstance(points[0],list):
            points = [points]
        while current >= len(self.trajectory):
            self.trajectory.append( [[],[],[]] )
        for p in points:
            self.trajectory[current][0].append(-real(p[0]))
            self.trajectory[current][1].append(real(p[1]))
            self.trajectory[current][2].append(real(p[2]))
    def plot_points(self):
        for k in range(len(self.trajectory)):
            color = self.point_color[k%len(self.point_color)]
            self.axes.plot(self.trajectory[k][1],self.trajectory[k][0],self.trajectory[k][2],alpha=0.75, zdir='z',linewidth=self.point_size,color=color)
    def plot_back(self):
        # back half of sphere
        u = linspace(0, pi, 75)
        v = linspace(0, pi, 75)
        x = outer(cos(u), sin(v))
        y = outer(sin(u), sin(v))
        z = outer(ones(size(u)), cos(v))
        self.axes.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=self.sphere_color, linewidth=0,
                               alpha=self.sphere_alpha)
        # wireframe
        self.axes.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=self.frame_color,
                                 alpha=self.frame_alpha)
        # equator
        self.axes.plot(1.0 * cos(u), 1.0 * sin(u), zs=0, zdir='z',
                       lw=self.frame_width, color=self.frame_color)
        self.axes.plot(1.0 * cos(u), 1.0 * sin(u), zs=0, zdir='x',
                       lw=self.frame_width, color=self.frame_color)

    def plot_front(self):
        # front half of sphere
        u = linspace(-pi, 0, 75)
        v = linspace(0, pi, 75)
        x = outer(cos(u), sin(v))
        y = outer(sin(u), sin(v))
        z = outer(ones(size(u)), cos(v))
        self.axes.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=self.sphere_color, linewidth=0,
                               alpha=self.sphere_alpha)
        # wireframe
        self.axes.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=self.frame_color,
                                 alpha=self.frame_alpha)
        # equator
        self.axes.plot(1.0 * cos(u), 1.0 * sin(u),
                       zs=0, zdir='z', lw=self.frame_width,
                       color=self.frame_color)
        self.axes.plot(1.0 * cos(u), 1.0 * sin(u),
                       zs=0, zdir='x', lw=self.frame_width,
                       color=self.frame_color)

if __name__ == "__main__":
    # Help
    if (len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help"]])):
        print("# Parameters:")
        print("#   --file=path            --  Path to File")
        print("#   --indices=re,im,f      --  Column Indices, either integers for column index or name of the column where the names are given in the first line of the File.")
        print("#   --skip=int             --  Only Render every X frame.")
        print("#   --view=Phi,Theta       --  Initial Rotation of the Blochsphere.")
        print("#   --deltarot=Phi,Theta   --  Rotate the view for a total of Phi and Theta over the duration of the video.")
        print("#   -allarrows             --  Also plot (2Re,0,0), (0,-2Im,0) and (0,0,2f-1) vectors.")
        print("# Note that when omitting --file, the first argument is interpreted as the path to the target.")
        exit()

    # FIDEO CONFIGURATION
    fps = 60 if not any(["fps=" in a for a in sys.argv]) else int([a.replace("--fps=","") for a in sys.argv if "--fps=" in a][0])
    iterations_max = 500000
    video_bitrate = 500 if not any(["bitrate=" in a for a in sys.argv]) else int([a.replace("--bitrate=","") for a in sys.argv if "--bitrate=" in a][0])
    fontsize = 15

    if any(["--fontsize=" in a for a in sys.argv]):
        fontsize = int([a.replace("--fontsize","") for a in sys.argv if "--fontisze" in a][0])

    # REST
    path = dirname(realpath(__file__))
    plt.rcParams.update({'font.size': fontsize})
    
    if any(["--file=" in a for a in sys.argv]):
        path = [a.replace("--file=","") for a in sys.argv if "--file=" in a][0]
    elif not sys.argv[1].startswith("--"):
        path = sys.argv[1]
    else:
        path = join(path,"densitymatrix.txt")
    if any(["--indices=" in a for a in sys.argv]):
        index = [tuple(b for b in a.split(",")) for a in [a.replace("--indices=","") for a in sys.argv if "--indices=" in a][0].split("AND")]

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

    print(f"Filepath is {path}")
    print(f"Bitrate is {video_bitrate} kbit/s")
    print(f"FPS is {fps}")
    print(f"Using indices {index} (Re(p), Im(p), f)")
    print(f"Plotting every {skip}")
    print(f"Initial view is {current_view}")
    print(f"Total delta view is {deltarot}")

    # Colormap
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, metadata=dict(artist='Dogwit'), bitrate=video_bitrate)
    t,ostates,names = [],[],[]
    for indx in index:
        tt,oo,nn = getVals(path,indx)
        t.append(tt)
        ostates.append(oo)
        names.append(nn)

    skipkind = "merge" if not "-cut" in sys.argv else "cut"
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
    b = BBloch(fig=fig,axes=ax1,view=current_view)
    #b.vector_color = ['r']

    ## normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0,len(ostates))
    colors = cm.cool(nrm(range(len(ostates)))) # options: cool, summer, winter, autumn etc.

    ## customize sphere properties ##
    b.point_color = list(colors) # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = 2
    b.frame_width = 2
    b.frame_color = "black"
    
    x = [[] for i in range(len(index))]
    f = [[] for i in range(len(index))]
    pol1 = [[] for i in range(len(index))]
    pol2 = [[] for i in range(len(index))]
    def animate(i):
        global t,states,fig,ax1
        ax1.clear()
        ax2.clear()
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
                for j in range(skip):
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
        b.render()
        ax1.view_init(azim=current_view[0], elev=current_view[1])
        legend = []
        [legend.extend([str(k)+': 2f(t)-1', str(k)+':2Re(p)', str(k)+':-2Im(p)']) for k in range(len(index))]
        ax2.legend(legend)
        ax2.set_xlim([np.min(t),np.max(t)])

        
    print("Creating animation")
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=iterations_max, repeat=True)
    print("Saving animation")
    ani.save(path.replace(".txt","_blochsphere.mp4"), writer=writer)
    print("Done")
exit()
