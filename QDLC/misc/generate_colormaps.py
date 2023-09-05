from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from math import floor,ceil

def generate_colormaps(inputpath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"colormaps/png"), maxcolors = 100, silent = True, generate_gnuplot = False):
    if not silent:
        print(f"Generating colormaps for input path {inputpath}")
    for file in os.listdir(inputpath):
        file = file.lower()
        if file.endswith(".png") or file.endswith(".svg"):
            if not silent:
                print("Generating " + os.path.join(inputpath, file))
            im = Image.open(os.path.join(inputpath,file)) # Can be many different formats.
            pix = im.load()
            incr = int(max(1.0,floor(im.size[0]/maxcolors)))
            if not silent:
                print("Image size: " + str(im.size) + " -> Color increment is " +str(incr))  # Get the width and hight of the image for iterating over
            
            offset_x, offset_y = [int(a) for a in file.split("offset_")[-1].replace(".png","").split("_")][0] if "offset_" in file else 0,0
            center = int(im.size[1]/2) + offset_y
            c = [[ pix[p,center][0], pix[p,center][1], pix[p,center][2], 255 ] for p in range(offset_x,im.size[0]-offset_x, incr)][1:]
            d = np.array( [ i for s in  [ np.linspace(k[0], k[1], maxcolors) for k in [[k,l] for k,l in zip(c[0:-1], c[1:])] ] for i in s ] )
            d /= np.max([np.max(a) for a in d])
            
            if generate_gnuplot:
                counter = 0
                # Gnuplot Color Palette
                with open(os.path.join(inputpath, file.replace(".png",".pal")),"w") as f:
                    print("set palette defined (",file = f, end = "")
                    last = ""
                    for p in d:
                        pixcolor = "{0:02x}".format(int(255*p[0])) + "{0:02x}".format(int(255*p[1])) + "{0:02x}".format(int(255*p[2]))
                        if (pixcolor != last):
                            if (last != ""):
                                print(" ,\\",file=f)
                            print( str(counter) + " '#" + pixcolor + "'" , file=f, end="")
                            last = pixcolor
                            counter+=1
                    print(" )",file=f)

            # Python Color Palette   
            name = file.replace(".png","")
            if "offset_" in name:
                name = name.split("_offset_")[0]
            if name not in plt.colormaps():
                if not silent:
                    print(f"Registering Colormap {name}")
                cmap = colors.ListedColormap(d, name=name)
                plt.colormaps.register(cmap)
            else:
                if not silent:
                    print(f"Colormap {name} already registered!")
            

# TODO: change to use all of matplotlibs colormaps!
def plot_colormaps(maps, mode, fp):
    print(f"Plotting {fp}")
    print(f"Plotting Colormaps:\n{maps}")
    data = [a.reshape((51,1000)) for a in np.loadtxt(fp, delimiter=' ', unpack=True, comments  = ["#","None","t","Time"])]
    size = [int(np.ceil(np.sqrt(len(maps)))),int(np.ceil(np.sqrt(len(maps))))]
    if size[0]*(size[1]-1) <= len(maps):
        size[1] -= 1
    fig = plt.figure(figsize=(20,10))
    gs = fig.add_gridspec(size[0],size[1],hspace=0.03, wspace=0.03, left=0.105, right=0.99, bottom=0.1, top=0.99)
    for cmap, (i,j) in zip(maps, [(i,j) for i in range(size[0]) for j in range(size[1])]):
        print(f"Adding {cmap}")
        ax = fig.add_subplot(gs[i,j])
        #plt.title(map)
        ax.text(0.01, 0.01, cmap , transform=ax.transAxes, fontsize=10, fontweight="bold", va='bottom', ha='left', color = "black", rotation = 0)
        if mode == "contour":
            plot = ax.contourf(data[1],data[0],data[3], cmap=cmap, levels=np.linspace(0,1,40), vmin=0,  vmax=1)
            [ c.set_rasterized(True) for c in plot.collections ]
        else:
            ax.pcolormesh(data[1],data[0],data[3], cmap=cmap, vmin=0, vmax=1, edgecolors='none', rasterized=True)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    print("Showing")
    plt.show()
        
if __name__ == "__main__":
    # TODO: commandline access, folder richtig übergeben dies das. script soll output immer im pip ordner halten aber input halt nicht.
    pwd = os.path.dirname(os.path.realpath(__file__))
    inputpath = input("Input Path (leave blank to plot all colormaps): ") or ""#os.path.join(pwd,"colormaps/png")#sys.argv[1] if len(sys.argv) > 1 else (input("Path to image: ") or "")
    if inputpath != "":
        generate_colormaps(inputpath, silent=False)
    generate_colormaps(silent=False)
    
    plot_which = [a for a in plt.colormaps() if not a.endswith("_r")]
    file_to_plot = input("File to plot: ") or os.path.join(pwd,"colormaps/data.txt")
    plot_colormaps(plot_which,"contour", file_to_plot)
