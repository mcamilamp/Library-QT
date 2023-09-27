# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)
from second_ui import Ui_Form
from module import filter_books_by_author
import sys

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 538)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setGeometry(QRect(10, 60, 231, 451))
        self.frame_principal.setMinimumSize(QSize(100, 0))
        self.frame_principal.setMaximumSize(QSize(500, 16777215))
        self.frame_principal.setStyleSheet(u"background-color: rgb(205, 217, 255);\n"
"border-radius:10px;\n"
"")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.frame_principal)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 20, 181, 20))
        self.title.setStyleSheet(u"font: 900 18pt \"Segoe UI\";\n"
"color: rgb(117, 135, 0);\n"
"")
        self.textEdit = QTextEdit(self.frame_principal)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 330, 201, 81))
        self.textEdit.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setCursorWidth(2)
        self.label_4 = QLabel(self.frame_principal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-30, 0, 591, 371))
        self.label_4.setStyleSheet(u"border-radius:10px;")
        self.label_4.setPixmap(QPixmap(u"img/tree3.png"))
        self.label_4.raise_()
        self.title.raise_()
        self.textEdit.raise_()
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(250, 60, 471, 451))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_option1 = QFrame(self.frame_2)
        self.frame_option1.setObjectName(u"frame_option1")
        self.frame_option1.setGeometry(QRect(30, 40, 201, 121))
        self.frame_option1.setAutoFillBackground(False)
        self.frame_option1.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_option1.setFrameShape(QFrame.NoFrame)
        self.frame_option1.setFrameShadow(QFrame.Plain)
        self.frame_option1.setLineWidth(-1)
        self.frame_option1.setMidLineWidth(4)
        self.label = QLabel(self.frame_option1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 151, 20))
        self.pushButton_2 = QPushButton(self.frame_option1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 80, 75, 24))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:8px;")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        self.lineEdit_1 = QLineEdit(self.frame_option1)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(40, 50, 113, 22))
        self.lineEdit_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_option3 = QFrame(self.frame_2)
        self.frame_option3.setObjectName(u"frame_option3")
        self.frame_option3.setGeometry(QRect(30, 180, 201, 121))
        self.frame_option3.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_option3.setFrameShape(QFrame.StyledPanel)
        self.frame_option3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_option3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 20, 141, 16))
        self.pushButton = QPushButton(self.frame_option3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 80, 75, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:8px;")
        self.lineEdit_2 = QLineEdit(self.frame_option3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 50, 113, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_option2 = QFrame(self.frame_2)
        self.frame_option2.setObjectName(u"frame_option2")
        self.frame_option2.setGeometry(QRect(240, 40, 201, 121))
        self.frame_option2.setStyleSheet(u"background-color: rgb(156, 220, 137);\n"
"border-radius:8px;")
        self.frame_option2.setFrameShape(QFrame.StyledPanel)
        self.frame_option2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_option2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 121, 16))
        self.pushButton_3 = QPushButton(self.frame_option2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 80, 75, 24))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:8px;")
        self.lineEdit_3 = QLineEdit(self.frame_option2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 50, 113, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_close = QFrame(self.centralwidget)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setGeometry(QRect(10, 9, 711, 41))
        self.frame_close.setStyleSheet(u"background-color: rgb(205, 217, 255);\n"
"border-radius:10px;")
        self.frame_close.setFrameShape(QFrame.StyledPanel)
        self.frame_close.setFrameShadow(QFrame.Raised)
        self.button_close = QPushButton(self.frame_close)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(660, 10, 41, 21))
        self.button_close.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u"img/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon)
        self.button_close.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_2.setDefault(False)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter the name of the book:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lineEdit_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Show books by Author:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Show books by genre:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.button_close.setText("")
    # retranslateUi

   