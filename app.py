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
# from PIL import Image
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LegoSorterEESS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.execApp)

    def execApp(self):

        # category_number, piece_name, piece_img, piece_id = brick.scan_piece()

        piece = brick.scan_piece()
        if (piece.category_number < 10):
            print("Your mother: ", piece.piece_img)

            response = requests.get(piece.piece_img)
            with open('brick_img.webp', 'wb') as file:
                file.write(response.content)
            img = Image.open('brick_img.webp')
            img.convert("RGB")
            img.save('brick_img.jpeg')
            self.ui.img.setPixmap(QPixmap(u"brick_img.jpeg"))

            self.ui.PieceName.setText(piece.piece_name)  # Updates UI -> Name
            self.ui.PieceID.setText(piece.piece_id)  # Updates UI -> ID


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
