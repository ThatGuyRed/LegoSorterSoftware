# import Brickognize_with_Custom_Dictionary.py
import sys
from src import *

import sys
from PySide6.QtWidgets import *  # debug, change to only relevant modules in 1.0
from PySide6.QtCore import QFile
from main import Ui_LegoSorterEESS
import os
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LegoSorterEESS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.execTerm)

    def execTerm(self):
        os.system("python Brickognize_with_Custom_Dictionary.py")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
