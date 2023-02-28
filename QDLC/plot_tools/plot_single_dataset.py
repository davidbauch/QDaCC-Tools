from QDLC.misc.functionality import _reshape_data_set, _get_data_header, _input_to_tuple, _guess_delimiter
import numpy as np
from math import ceil, floor, sqrt
import matplotlib.pyplot as plt

def _plot_matrix(x: np.array ,y: np.array ,z: np.array, ax = None, vmin: float | None = None, vmax: float | None = None, cmap: str = "turbo", ranges: str = "auto", indices: str = "auto", shading: str = "nearest", use_cbs: bool = True, logscale: bool = False, colorrepeat: int = 1) -> None:
    """
    Plot data using matrix plots.
    :param data: The data to plot. Shape needs to be [X,Y,V...] where X,Y,V are NxM matrices
    """
    plot = ax.pcolormesh(x,y,z, cmap = cmap, edgecolors='none',shading=shading, vmin=vmin, vmax = vmax, rasterized=True)
    plot.set_edgecolor('face')
    return plot

def _plot_lines(x: np.array, y: np.array, ax = None, ranges: str = "auto", indices: str = "auto", logscale: bool = False) -> None:
    """
    Plot data using line plots.
    :param data: The data to plot. Shape needs to be [X,Y,V...] where X,Y,V are vectors
    """
    plot = ax.plot(x,y,'o', linewidth=0)

def plot_single_dataset(total_path: str, output_path: None, cmap: str = "turbo", delimiter: str = "auto", fformat: str = "pdf", ranges: str = "auto", indices: str = "auto", shading: str = "nearest", use_cbs: bool = True, logscale: bool = False, colorrepeat: int = 1, mode: str = "matrix"):
    from string import ascii_letters
    """
    todo: one plot per file
    """
    # Split paths
    total_path = total_path.split(";")

    # User Output
    print(f"Plotting '{', '.join(total_path)}' in {mode} mode")
    print(f"Format used: {fformat}")
    if mode == "matrix":
        print(f" - Colormap used: {cmap}")
        print(f" - Using {'colorbars' if use_cbs else 'no colorbars'}")
        print(f" - Repeating Colors {colorrepeat} times.")
    [print(f" - Using custom {name}: {var}") for name, var in zip(["Delimiter", "Ranges", "Indices"], [delimiter, ranges, indices]) if var != "auto"]
    print(f" - Using {'logscale' if logscale else 'linear scale'}")
    print(f" - Shading mode: {shading}")

    if output_path is not None:
        print(f"Output path: {output_path}")
    
    # Parse Ranges
    if ranges != "auto":
        input_ranges = _input_to_tuple(ranges, delimiter = ":")
        if len(input_ranges) != 4 and len(input_ranges) != 6:
            raise ValueError(f"Ranges must be of length 4 or 6, but is of length {len(input_ranges)}")
        ranges_x_min, ranges_x_max, ranges_y_min, ranges_y_max = input_ranges[:4]
        if mode == "matrix":
            ranges_z_min, ranges_z_max = input_ranges[4:]

    # Load Data
    data = {}
    for path in total_path:
        header = _get_data_header(total_path, delimiter=" ").split()
        comments = header if not header[0].isnumeric() else list(ascii_letters)
        if delimiter == "auto":
            delimiter = _guess_delimiter(total_path)
        new_data = np.loadtxt(path, comments=comments, delimiter=delimiter, unpack=True)
        if mode == "matrix":
            new_data = _reshape_data_set(data)
        data[path] = {"data": new_data, "header": header}
    
    # Figure out axes dimensions:
    number_of_plots = sum([len(data[path]["data"]) - (2 if mode == "matrix" else 1) for path in total_path])
    ax_dim_x = floor(sqrt(number_of_plots))
    ax_dim_y = ceil(number_of_plots/ax_dim_x)
    
    # Figure and Grid
    fig = plt.figure(figsize=(16,9))
    gs = fig.add_gridspec(ax_dim_x,ax_dim_y,hspace=0.1, wspace=0.1)

    # Create Axes
    iterator = [(i,j) for i in range(ax_dim_x) for j in range(ax_dim_y)]
    ax = [fig.add_subplot(gs[i,j]) for (i,j) in iterator]
    [a.label_outer() for a in ax]

    # Plot Data
    plot_index = 0
    all_plots = []
    for datasets in data.values():
        if mode == "matrix":
            x,y = datasets["data"][:2]
            for z in datasets["data"][2:]:
                all_plots.append( _plot_matrix(x,y,z, ax=ax[plot_index], cmap=cmap, ranges=ranges, indices=indices, shading=shading, use_cbs=use_cbs, logscale=logscale, colorrepeat=colorrepeat) )
                plot_index += 1
        else:
            x = datasets["data"][0]
            for y in datasets["data"][1:]:
                all_plots.append( _plot_lines(x,y, ax=ax[plot_index], ranges=ranges, indices=indices, logscale=logscale) )
                plot_index += 1

    if output_path is None:
        return ax, all_plots
    
    if output_path == "show":
        plt.show()
    else:
        print(f"Saving to {output_path}{fformat}")
        plt.savefig(f"{output_path}{fformat}",dpi = 400)

if __name__ == "__main__":
    print("This file is part of the QDLC evaluation framework and should not be executed on its own.")