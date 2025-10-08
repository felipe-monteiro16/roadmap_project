"""Display Layer"""
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from ui import Ui_Graph


class MainWindow(QMainWindow, Ui_Graph):
    """Main Window Class"""


    def __init__(self, data):
        super().__init__()
        self.data = data

        self.setupUi(self)
        self.setWindowTitle("Graphs")

        self.DiseaseComboBox.addItem("Dengue", ["Gender", "Age"])

        self.DiseaseComboBox.activated.connect(self.show_demographic)
        self.DiseaseComboBox.setCurrentIndex(-1)

        self.graph_widget = pg.PlotWidget()

        self.graph_widget.setBackground('w')

        layout = QVBoxLayout(self.GraphWidget)
        layout.addWidget(self.graph_widget)
        self.GraphWidget.setLayout(layout)

        # Turn the graph dinammic
        #self.graphWidget.getViewBox().setMouseEnabled(x=False, y=False)

        self.GeneratePushButton.clicked.connect(self.plot_data)

        self.BarRadioButton.setChecked(True)

    def show_demographic(self, index):
        """Show demographic options based on disease selection"""
        self.DemographicsComboBox.clear()

        self.DemographicsComboBox.addItems(self.DiseaseComboBox.itemData(index))

    def plot_data(self):
        """Plot data based on user selection"""

        self.graph_widget.clear()

        demographic = self.DemographicsComboBox.currentText()

        if demographic == "Gender":
            y = self.data["CS_SEXO"].value_counts().sort_index()
        elif demographic == "Age":
            y = self.data["NU_IDADE"].value_counts().sort_index()
        else:
            return

        index = list(y.index)

        if isinstance(index[0], str):
            x = list(range(len(index)))
        else:
            x = index

        if self.LineRadioButton.isChecked():

            self.graph_widget.plot(x, y, pen='b', symbol='o', symbolSize=5, symbolBrush='r')

            self.graph_widget.showGrid(x=True, y=True)

        elif self.BarRadioButton.isChecked():

            bar_graph = pg.BarGraphItem(x=x, height=y, width=0.6, brush='b')
            self.graph_widget.addItem(bar_graph)

            self.graph_widget.showGrid(x=False, y=False)

        if isinstance(index[0], str):
            axis = self.graph_widget.getAxis("bottom")
            ticks = [list(zip(x, index))]
            axis.setTicks(ticks)
        else:
            self.graph_widget.getAxis("bottom").setTicks(None)

        self.graph_widget.setTitle(f"Number of cases X {demographic}")
