Toolset for my quantum simulation tool [QDaCC](https://github.com/davidbauch/QDaCC)

# Evaluation Tools
todo

# Plot Tools
Plot Tools include:
- Plotting a QDaCC file using 

# GUI
GUI for my quantum simulation program [QDaCC](https://github.com/davidbauch/QDaCC)

The User Interface is decoupled from the main program for two main reasons:
- To keep dependencies low; QDaCC is build to minimize external dependencies. QDaCC only depdends on Eigen for matrix handling, ALGLIB for interpolation and fmt for output formatting. In the future, QDaCC will drop its dependencies on ALGLIB and fmt. Additionally, QDaCC would need a "execute without UI" mode, which adds additional overhead.
- To keep the GUI implementation simple; QDaCC is part of my PHD, and building a UI in python is 10 times easier than in C++

## What the GUI does
QDaCC is a command line tool. For specific calculations, it requires large user inputs while omitting parameter validation. This means, when the user makes a mistake, QDaCC crashes. While QDaCC provides basic logging to debug these mistakes, correction of the input takes time. Additionally, because QDaCC only oparates in the command line, the user has to change interfaces all the time. The QDaCC GUI introduces simple parameter validation and ensures that the arguments passed to QDaCC are valid. Additionally, it provides simple tools to quickly plot and display the calculated results.

List of available tools in the GUI:
- Prediction of spectral and temporal properties. This is a handy feature for the user when determining the temporal and spectral inputs.
- Basic extrapolation of input parameters: The GUI calculates and provides basic information for the user like the available states and transitions.
- Baisc plotting: Plotting everything QDaCC calculated, plotting matrices and Bloch spheres using the evaluation and plot tools.
- Parameter Sweeps: The GUI provides a simple toolbox to generate large parameter sweeps.
- Parameter Optimization: The GUI provides a simple toolbox to optimize the QDaCC results towards a user specified fitness function
- [more to come]
