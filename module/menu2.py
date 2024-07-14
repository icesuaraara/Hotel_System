import sys
import os
import sqlite3

import style

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QColorDialog, QFrame, QLabel, QComboBox
from PyQt5.QtCore import Qt  # Import Qt
from PyQt5.QtGui import QPixmap, QFont

font = QFont("Arial", 15) 

def menu_edit(window, ui_elements):

    text_dropdown = QLabel('เลือกห้อง',window)
    text_dropdown.move(350,80)
    text_dropdown.setFont(font)
    text_dropdown.show()




    dropdown = QComboBox(window)
    for i in range(1, 37):
        dropdown.addItem(f"ห้องที่ {i}")
    dropdown.move(450, 80)
    dropdown.resize(100, 30)
    dropdown.show()
    
    ui_elements.append(dropdown)
    