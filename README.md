# Toolset for my quantum simulation tool [QDaCC](https://github.com/davidbauch/QDaCC)

# Evaluation Tools
QDaCC outputs a variety of numerical results, strongly dependent on the input system and the desired output method. Especially when calculating large parameter scans or double parameter sweeps, manually evaluating the results becomes very costly. The Evaluation Tools provide a simple toolset to evaluate these datasets.

- `python3 -m QDLC.eval_tools.get_runtime filepath` Extracts the runtimes of a set of calculations in filepath
- `python3 -m QDLC.eval_tools.get_final_line_for_matrix_plot filepath` Extracts the final line of a file, formats it as a matrix and outputs gnuplot compatible resources
- `python3 -m QDLC.eval_tools.get_files files filepath` Extracts files from a dataset and combines them into a single file for plotting.

# Plot Tools
The Plot Tools provide a simple commandline interface to call the Evaluation Tools and subsequently call a matplotlib plotscript. The Plot Tools include plotting single calculations, scans with endpoint plots, 2D sweeps with endpoint plots, animated matrix plots and animated Bloch sphere plots. On most scripts, `--help` can be called to display a brief summary of the available commandline arguments. The commands include

- `python3 -m QDLC.plot_tools.general_matrix_plot filepath [arguments]`
- `python3 -m QDLC.plot_tools.plot_blochsphere_animated --file=filepath --indices=re,im,z [arguments]`
- `python3 -m QDLC.plot_tools.plot_dm_animated --file=filepath --indices=re,im,z [arguments]`

# GUI
The User Interface is decoupled from the main program for two main reasons:
- To keep dependencies low; QDaCC is build to minimize external dependencies. QDaCC only depdends on Eigen for matrix handling, ALGLIB for interpolation and fmt for output formatting. In the future, QDaCC will drop its dependencies on ALGLIB and fmt. Additionally, QDaCC would need a "execute without UI" mode, which adds additional overhead.
- To keep the GUI implementation simple; QDaCC is part of my PHD, and building a UI in python is 10 times easier than in C++

## What the GUI does
QDaCC is a command line tool. For specific calculations, it requires large user inputs while omitting parameter validation. This means, when the user makes a mistake, QDaCC crashes. While QDaCC provides basic logging to debug these mistakes, correction of the input takes time. Additionally, because QDaCC only oparates in the command line, the user has to change interfaces all the time. The QDaCC GUI introduces simple parameter validation and ensures that the arguments passed to QDaCC are valid. Additionally, it provides simple tools to quickly plot and display the calculated results.

List of available tools in the GUI:
- Prediction of spectral and temporal properties. This is a handy feature for the user when determining the temporal and spectral inputs.
- Basic extrapolation of input parameters: The GUI calculates and provides basic information for the user like the available states and transitions.
- Basic plotting: Plotting everything QDaCC calculated, plotting matrices and Bloch spheres using the evaluation and plot tools.
- Parameter Sweeps: The GUI provides a simple toolbox to generate large parameter sweeps.
- Parameter Optimization: The GUI provides a simple toolbox to optimize the QDaCC results towards a user specified fitness function
- [more to come]

The GUI also invokes the evaluation and plot scripts, making it the only tool one needs to use QDaCC.
