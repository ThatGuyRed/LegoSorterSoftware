import Brickognize_with_Custom_Dictionary as brick
import sys
from src import *

import sys
from PySide6.QtWidgets import *  # debug, change to only relevant modules in 1.0
from PySide6.QtCore import QFile, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPixmap, QImage
from main import Ui_LegoSorterEESS
import requests
import os
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LegoSorterEESS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.execApp)

    def execApp(self):
        # os.system("python Brickognize_with_Custom_Dictionary.py")
        scan = brick.main()
        category_number = scan[0]
        piece_name = scan[1]
        piece_img = scan[2]
        piece_id = scan[3]
        # category_number, piece_name, piece_img, piece_id = brick.main()
        # piece_img = '127.0.0.1'
        # piece_name = 'debugName'
        # piece_id = 'debugID'
        # self.ui.webEngineView.setHtml("")
        # self.ui.webEngineView.setUrl(piece_img)
        # self.ui.webEngineView.page().triggerAction(QWebEnginePage.ReloadAndBypassCache)
        image_data = requests.get(piece_img).content
        image = QPixmap()
        print(piece_img)
        image.loadFromData(image_data)
        self.ui.img.setPixmap(image)
        self.ui.img.setScaledContents(True)
        self.ui.PieceName.setText(piece_name)

        self.ui.PieceID.setText(piece_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
