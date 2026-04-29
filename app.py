# import Brickognize_with_Custom_Dictionary as brick
import brickognize_script_v2 as brick
import sys
# import sys
from PySide6.QtWidgets import *  # debug, change to only relevant modules in 1.0
# from PySide6.QtCore import QFile, QUrl
# from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPixmap
from main import Ui_LegoSorterEESS
import requests
import os
# import subprocess
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LegoSorterEESS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.execApp)

    def execApp(self):
        piece = brick.scan_piece()
        if (piece.category_number == 9):
            self.ui.img.setPixmap(QPixmap(u"rick.jpg"))
            self.ui.PieceName.setText(u"ERROR")  # Updates UI -> Name
            self.ui.PieceID.setText(u"ERROR")

        elif (piece.category_number < 10):
            if os.path.exists('brick_img.jpeg'):
                os.remove('brick_img.jpeg')  # Remove if exists

            response = requests.get(piece.piece_img)
            with open('brick_img.webp', 'wb') as file:
                file.write(response.content)

            img = Image.open('brick_img.webp')
            img.convert("RGB")
            img.save('brick_img.jpeg')
            self.ui.img.setPixmap(QPixmap(u"brick_img.jpeg"))
            os.remove('brick_img.webp')  # Cleanup

            self.ui.PieceName.setText(piece.piece_name)  # Updates UI -> Name
            self.ui.PieceID.setText(piece.piece_id)  # Updates UI -> ID

            # placeholder container
            brick.store_data(piece, 1)
            brick.print_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
