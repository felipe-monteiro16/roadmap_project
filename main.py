"""Main"""
import sys
from PyQt5.QtWidgets import QApplication
from data_access import DataAccess
from cli import MainWindow


def get_download_data():
    """Get download data from SINAN"""
    data_access = DataAccess()
    return data_access.download_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = get_download_data()
    main_win = MainWindow(data)
    main_win.show()
    sys.exit(app.exec_())
