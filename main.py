# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_LegoSorterEESS(object):
    def setupUi(self, LegoSorterEESS):
        if not LegoSorterEESS.objectName():
            LegoSorterEESS.setObjectName(u"LegoSorterEESS")
        LegoSorterEESS.resize(553, 600)
        self.centralwidget = QWidget(LegoSorterEESS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 370, 81, 25))
        self.PieceNamepre = QLabel(self.centralwidget)
        self.PieceNamepre.setObjectName(u"PieceNamepre")
        self.PieceNamepre.setGeometry(QRect(160, 310, 54, 17))
        self.PieceIDpre = QLabel(self.centralwidget)
        self.PieceIDpre.setObjectName(u"PieceIDpre")
        self.PieceIDpre.setGeometry(QRect(160, 340, 54, 17))
        self.PieceName = QLabel(self.centralwidget)
        self.PieceName.setObjectName(u"PieceName")
        self.PieceName.setGeometry(QRect(240, 310, 191, 17))
        self.PieceID = QLabel(self.centralwidget)
        self.PieceID.setObjectName(u"PieceID")
        self.PieceID.setGeometry(QRect(240, 340, 211, 17))
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(90, 60, 351, 251))
        LegoSorterEESS.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LegoSorterEESS)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 553, 22))
        LegoSorterEESS.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LegoSorterEESS)
        self.statusbar.setObjectName(u"statusbar")
        LegoSorterEESS.setStatusBar(self.statusbar)

        self.retranslateUi(LegoSorterEESS)

        QMetaObject.connectSlotsByName(LegoSorterEESS)
    # setupUi

    def retranslateUi(self, LegoSorterEESS):
        LegoSorterEESS.setWindowTitle(QCoreApplication.translate("LegoSorterEESS", u"Lego Sorter EESS", None))
        self.pushButton.setText(QCoreApplication.translate("LegoSorterEESS", u"Le Button", None))
        self.PieceNamepre.setText(QCoreApplication.translate("LegoSorterEESS", u"Name:", None))
        self.PieceIDpre.setText(QCoreApplication.translate("LegoSorterEESS", u"ID:", None))
        self.PieceName.setText(QCoreApplication.translate("LegoSorterEESS", u"PieceNameText", None))
        self.PieceID.setText(QCoreApplication.translate("LegoSorterEESS", u"PieceIDText", None))
        self.img.setText(QCoreApplication.translate("LegoSorterEESS", u"Null", None))
    # retranslateUi

