import sys
import os

import style

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QColorDialog, QFrame, QLabel
from PyQt5.QtCore import Qt  # Import Qt
from PyQt5.QtGui import QPixmap

def menuna(window,ui_elements):
    print('menu1')
    frame = QFrame(window)
    frame.setGeometry(350, 50, 600, 500)  # Set the position and size of the frame
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setStyleSheet("background-color: white;")
    frame.show()

    ui_elements.append(frame)
