from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QApplication, QMainWindow
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class PlotWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        #vertical_layout.addWidget(NavigationToolbar(self.canvas, self))
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        
        # Get main widget
        # Set background color of axes
        self.setLayout(vertical_layout)  
    
    def resetPlot(self, mainWindow):
        self.canvas.axes.clear()
        self.figure.set_facecolor(mainWindow.design_colors["background_color"])
        self.canvas.axes.set_facecolor(mainWindow.design_colors["secondary_color"])
        self.canvas.draw()