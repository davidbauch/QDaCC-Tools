Toolset for my quantum simulation tool [QDaCC](https://github.com/davidbauch/QDaCC)

# Evaluation Tools
todo

# Plot Tools
todo

# GUI
GUI for my quantum simulation program [QDaCC](https://github.com/davidbauch/QDaCC)

The User Interface is decoupled from the main program for two main reasons:
- To keep dependencies low; QDaCC is build to minimize external dependencies. QDaCC only depdends on Eigen for matrix handling, ALGLIB for interpolation and fmt for output formatting. In the future, QDaCC will drop its dependencies on ALGLIB and fmt. Additionally, QDaCC would need a "execute without UI" mode, which adds additional overhead.
- To keep the GUI implementation simple; QDaCC is part of my PHD, and building a UI in python is 10 times easier than in C++

## What the GUI does
todo
