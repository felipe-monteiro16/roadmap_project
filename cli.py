import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from ui import Ui_Graph

class MainWindow(QMainWindow, Ui_Graph):
        def __init__(self):
            super().__init__()

            self.setupUi(self)
            self.setWindowTitle("Graphs")

            self.graphWidget = pg.PlotWidget()

            self.graphWidget.setBackground('w')

            layout = QVBoxLayout(self.GraphWidget)
            layout.addWidget(self.graphWidget)
            self.GraphWidget.setLayout(layout)

            # Receive X and Y from PySUS
            self.graphWidget.plot([1, 2, 3, 4], [5, 6, 7, 8], pen='b', symbol='o', symbolSize=5, symbolBrush=('r'))
            
            self.graphWidget.setTitle("Random Data Plot")
            self.graphWidget.showGrid(x=True, y=True)
