"""""
import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QGraphicsDropShadowEffect)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class EmptyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initialize_UI()

    def initialize_UI(self):
        self.setGeometry(290, 100, 800, 500)
        self.setWindowTitle("Library: Under The Tree")
        self.show()

        main_layout = QVBoxLayout(self)

        title_label = QLabel("Under The Tree")
        title_label.setFont(QFont("Arial", 21, QFont.Weight.ExtraBold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title_label.setStyleSheet("color: #758700;")

        main_layout.addWidget(title_label)

        image_label = QLabel()
        pixmap = QPixmap("img/tree.png")  
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)


        main_layout.addWidget(image_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    window.show()
    sys.exit(app.exec())


"""