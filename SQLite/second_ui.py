# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(685, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setGeometry(QRect(20, 10, 231, 461))
        self.frame_principal.setMinimumSize(QSize(100, 0))
        self.frame_principal.setMaximumSize(QSize(500, 16777215))
        self.frame_principal.setStyleSheet(u"background-color: rgb(205, 217, 255);\n"
"border-radius:10px;\n"
"")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.frame_principal)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 30, 181, 20))
        self.title.setStyleSheet(u"font: 900 18pt \"Segoe UI\";\n"
"color: rgb(117, 135, 0);\n"
"")
        self.textEdit = QTextEdit(self.frame_principal)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 350, 201, 91))
        self.textEdit.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setCursorWidth(2)
        self.label_4 = QLabel(self.frame_principal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-30, 60, 421, 271))
        self.label_4.setStyleSheet(u"border-radius:10px;")
        self.label_4.setPixmap(QPixmap(u"../img/tree3.png"))
        self.label_4.raise_()
        self.title.raise_()
        self.textEdit.raise_()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 10, 411, 461))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.by_genre = QWidget()
        self.by_genre.setObjectName(u"by_genre")
        self.by_genre.setStyleSheet(u"background-color: rgb(205, 217, 255);")
        self.frame_2 = QFrame(self.by_genre)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 391, 51))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.title_3 = QLabel(self.frame_2)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(110, 10, 211, 31))
        self.title_3.setStyleSheet(u"font: 900 16pt \"Segoe UI\";\n"
"color: rgb(117, 135, 0);\n"
"")
        self.stackedWidget.addWidget(self.by_genre)
        self.by_name = QWidget()
        self.by_name.setObjectName(u"by_name")
        self.by_name.setStyleSheet(u"background-color: rgb(205, 217, 255);")
        self.frame_3 = QFrame(self.by_name)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 391, 51))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.title_4 = QLabel(self.frame_3)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(110, 10, 211, 31))
        self.title_4.setStyleSheet(u"font: 900 16pt \"Segoe UI\";\n"
"color: rgb(117, 135, 0);\n"
"")
        self.stackedWidget.addWidget(self.by_name)
        self.a_principal = QWidget()
        self.a_principal.setObjectName(u"a_principal")
        self.frame_byname = QFrame(self.a_principal)
        self.frame_byname.setObjectName(u"frame_byname")
        self.frame_byname.setGeometry(QRect(20, 80, 181, 111))
        self.frame_byname.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_byname.setFrameShape(QFrame.StyledPanel)
        self.frame_byname.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_byname)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 211, 16))
        self.lineEdit = QLineEdit(self.frame_byname)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 40, 113, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_2 = QPushButton(self.frame_byname)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 70, 75, 24))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:9px;")
        self.frame_bygenre = QFrame(self.a_principal)
        self.frame_bygenre.setObjectName(u"frame_bygenre")
        self.frame_bygenre.setGeometry(QRect(210, 80, 181, 111))
        self.frame_bygenre.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_bygenre.setFrameShape(QFrame.StyledPanel)
        self.frame_bygenre.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_bygenre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 121, 16))
        self.lineEdit_2 = QLineEdit(self.frame_bygenre)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 40, 113, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_3 = QPushButton(self.frame_bygenre)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 70, 75, 24))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:9px;")
        self.frame_byauthor = QFrame(self.a_principal)
        self.frame_byauthor.setObjectName(u"frame_byauthor")
        self.frame_byauthor.setGeometry(QRect(20, 200, 181, 111))
        self.frame_byauthor.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_byauthor.setFrameShape(QFrame.StyledPanel)
        self.frame_byauthor.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_byauthor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 141, 16))
        self.lineEdit_3 = QLineEdit(self.frame_byauthor)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 40, 113, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_4 = QPushButton(self.frame_byauthor)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 70, 75, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:9px;")
        self.stackedWidget.addWidget(self.a_principal)
        self.by_author = QWidget()
        self.by_author.setObjectName(u"by_author")
        self.by_author.setStyleSheet(u"background-color: rgb(205, 217, 255);")
        self.frame = QFrame(self.by_author)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 391, 51))
        self.frame.setStyleSheet(u"background-color: rgb(205, 217, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.title_2 = QLabel(self.frame)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(110, 10, 211, 31))
        self.title_2.setStyleSheet(u"font: 900 16pt \"Segoe UI\";\n"
"color: rgb(117, 135, 0);\n"
"")
        self.listView = QListView(self.by_author)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 70, 371, 361))
        self.stackedWidget.addWidget(self.by_author)
        self.frame_close = QFrame(self.centralwidget)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setGeometry(QRect(20, 480, 651, 41))
        self.frame_close.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.frame_close.setFrameShape(QFrame.StyledPanel)
        self.frame_close.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_close)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 10, 75, 24))
        self.pushButton.setCursor(QCursor(Qt.ClosedHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Under The Tree", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Have you been </span><span style=\" font-size:9pt; font-weight:700;\">Under </span><span style=\" font-size:9pt;\">a</span><span style=\" font-size:9pt; font-weight:700;\"> Tree</span><span style=\" font-size:9pt;\"> on a </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:9pt;\">sunny day?</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">This is what it feels like to read a good book</span></p></body></html>", None))
        self.label_4.setText("")
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Books by Genre", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Books by Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter the name of the Book:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Show books by genre:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Show books by Author:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Books by Author", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

