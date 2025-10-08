"""Main"""
import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from data_access import DataAccess
from ui import Ui_Graph

class MainWindow(QMainWindow, Ui_Graph):
    """Main Window Class"""
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Graphs")

        self.DiseaseComboBox.addItem("Dengue", ["Gender", "Age"])
        
        self.DiseaseComboBox.activated.connect(self.show_demographic)
        self.DiseaseComboBox.setCurrentIndex(-1)

        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground('w')

        layout = QVBoxLayout(self.GraphWidget)
        layout.addWidget(self.graphWidget)
        self.GraphWidget.setLayout(layout)

        # Turn the graph dinammic
        #self.graphWidget.getViewBox().setMouseEnabled(x=False, y=False)

        self.GeneratePushButton.clicked.connect(self.plot_data)

    def show_demographic(self, index):
        """Show demographic options based on disease selection"""
        self.DemographicsComboBox.clear()

        self.DemographicsComboBox.addItems(self.DiseaseComboBox.itemData(index))

    def plot_data(self):
        """Plot data based on user selection"""

        self.graphWidget.clear()

        data = get_download_data()
        print(data)

        demographic = self.DemographicsComboBox.currentText()

        if demographic == "Gender":
            Y = data["CS_SEXO"].value_counts().sort_index()
        elif demographic == "Age":
            Y = data["NU_IDADE"].value_counts().sort_index()
        
        index = list(Y.index)

        if type(index[0]) == str:
            X = list(range(len(index)))
        else:
            X = index

        if self.LineRadioButton.isChecked():
            
            self.graphWidget.plot(X, Y, pen='b', symbol='o', symbolSize=5, symbolBrush=('r'))

            self.graphWidget.showGrid(x=True, y=True)

        elif self.BarRadioButton.isChecked():

            bar_graph = pg.BarGraphItem(x=X, height=Y, width=0.6, brush='b')
            self.graphWidget.addItem(bar_graph)

            self.graphWidget.showGrid(x=False, y=False)
        
        if type(index[0]) == str:
            axis = self.graphWidget.getAxis("bottom")
            ticks = [list(zip(X, index))]
            axis.setTicks(ticks)
        else:
            self.graphWidget.getAxis("bottom").setTicks(None)

        self.graphWidget.setTitle(f"Number of cases X {demographic}")


def get_download_data():
    """Get download data from SINAN"""
    data_access = DataAccess()
    data = data_access.download_data()
    return data

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
