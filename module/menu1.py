import sys
import os
import sqlite3

import style

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QColorDialog, QFrame, QLabel
from PyQt5.QtCore import Qt  # Import Qt
from PyQt5.QtGui import QPixmap, QFont

font = QFont("Arial", 10) 

conn = sqlite3.connect('room.db')
cursor = conn.cursor()

fetch_query_statusroom = "SELECT status_room FROM room"
cursor.execute(fetch_query_statusroom)
status_room_values = cursor.fetchall()

conn.close()

def menu_view(window,ui_elements):

    def create_room_frame(parent, x, y, width, height, room_name, status):
        frame = QFrame(parent)
        frame.setGeometry(x, y, width, height)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: white;")

        frame_layout = QVBoxLayout(frame)
        status_label = QLabel(f"{room_name}\nสถานะ: {status}", frame)
        status_label.setFont(font)
        status_label.setAlignment(Qt.AlignCenter)
        frame_layout.addWidget(status_label)

        return frame

    # Create the first room frame
    room_positions = [
        (350, 50), (350, 130), (350, 210), (350, 290), (350, 370), (350, 450), (350, 530), (350, 610), (350, 690),
        (550, 50), (550, 130), (550, 210), (550, 290), (550, 370), (550, 450), (550, 530), (550, 610), (550, 690),
        (750, 50), (750, 130), (750, 210), (750, 290), (750, 370), (750, 450), (750, 530), (750, 610), (750, 690),
        (950, 50), (950, 130), (950, 210), (950, 290), (950, 370), (950, 450), (950, 530), (950, 610), (950, 690)
    ]

# Create frames using a loop
    for i, (x, y) in enumerate(room_positions):
        room_name = f"ห้องที่{i+1}"
        status_room = status_room_values[i][0]  # ดึงค่าของแถวแรกไปจนถึงแถวสุดท้าย
        frame = create_room_frame(window, x, y, 150, 50, room_name, status_room)
        ui_elements.append(frame)
        frame.show()

