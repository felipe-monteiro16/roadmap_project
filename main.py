import sys
from data_access import DataAccess
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from ui import Ui_Graph

class MainWindow(QMainWindow, Ui_Graph):
	def __init__(self):
		super().__init__()

		self.setupUi(self)
		self.setWindowTitle("Graphs")

		self.DiseaseComboBox.addItem("Dengue", ["Gênero", "Raça"])
		self.DiseaseComboBox.addItem("AIDS", ["Gênero", "Raça"])

		self.DiseaseComboBox.activated.connect(self.show_demographic)
		self.DiseaseComboBox.setCurrentIndex(-1)

		self.graphWidget = pg.PlotWidget()

		self.graphWidget.setBackground('w')

		layout = QVBoxLayout(self.GraphWidget)
		layout.addWidget(self.graphWidget)
		self.GraphWidget.setLayout(layout)

		self.graphWidget.getViewBox().setMouseEnabled(x=False, y=False)

		self.GeneratePushButton.clicked.connect(self.plot_data)

	def show_demographic(self, index):
		self.DemographicsComboBox.clear()

		self.DemographicsComboBox.addItems(self.DiseaseComboBox.itemData(index))

	def plot_data(self):
		self.graphWidget.clear()

		if self.LineRadioButton.isChecked():

			# Receive X and Y from PySUS
			self.graphWidget.plot([1, 2, 3, 4], [5, 6, 7, 8], pen='b', symbol='o', symbolSize=5, symbolBrush=('r'))
			
			self.graphWidget.setTitle("Random Data Plot")
			self.graphWidget.showGrid(x=True, y=True)
			self.graphWidget.getAxis("bottom").setTicks(None)

		elif self.BarRadioButton.isChecked():

			# Receive categories and heights from PySUS
			categories = ['A', 'B', 'C', 'D', 'E']
			heights = [10, 25, 15, 30, 20]
			x_positions = list(range(len(categories)))

			bar_graph = pg.BarGraphItem(x=x_positions, height=heights, width=0.6, brush='b')
			self.graphWidget.addItem(bar_graph)
			self.graphWidget.showGrid(x=False, y=False)

			axis = self.graphWidget.getAxis("bottom")
			ticks = [list(zip(x_positions, categories))]
			axis.setTicks(ticks)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
