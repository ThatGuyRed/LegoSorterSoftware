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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_LegoSorterEESS(object):
    def setupUi(self, LegoSorterEESS):
        if not LegoSorterEESS.objectName():
            LegoSorterEESS.setObjectName(u"LegoSorterEESS")
        LegoSorterEESS.resize(814, 600)
        self.centralwidget = QWidget(LegoSorterEESS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(220, 40, 381, 251))
        self.webEngineView.setUrl(QUrl(u"https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 370, 81, 25))
        LegoSorterEESS.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LegoSorterEESS)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 814, 22))
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
    # retranslateUi

