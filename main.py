import sys
from data_access import DataAccess
from cli import MainWindow
from PyQt5.QtWidgets import QApplication

from ui import Ui_Graph

def main():
	data_access = DataAccess
	data = data_access.get_all_data()
	#show_all_data(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
