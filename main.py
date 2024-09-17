import sys
import os

import style

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QColorDialog, QFrame, QLabel, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSlot   # Import Qt
from PyQt5.QtGui import QPixmap

sys.path.append('module/')
import menu1
import menu2

app = QApplication(sys.argv) #สร้างแอพ
ui_elements = []
window = None

def main():
    global window
    # Function to show message box
    def menu_view():
        clear_ui_elements()
        menu1.menu_view(window, ui_elements)
        
    def menu_edit():
        clear_ui_elements()
        menu2.menu_edit(window, ui_elements)
        
    def menu3():
        clear_ui_elements()
        pass
    
    def menu4():
        clear_ui_elements()
        pass
    
    def menu5():
        clear_ui_elements()
        pass

    def clear_ui_elements():
        for element in ui_elements:
            element.setParent(None)
        ui_elements.clear()

    # Create a main window
    window = QWidget()
    window.setWindowTitle("Centered Button Example")
    window.resize(1280,800)  # Set the window size

    # Create a frame to contain the area for changing background color
    screen_geometry = QDesktopWidget().screenGeometry()
    screen_height = screen_geometry.height()
    frame = QFrame(window)
    frame.setGeometry(0, 0, 300,screen_height)  # Set the position and size of the frame
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setStyleSheet("background-color: lightblue;")

    # Create buttons
    button_main = QPushButton("Over view room", window)
    button_main.clicked.connect(menu_view)
    button_main.resize(260, 100)
    button_main.move(20, 170)
    button_main.setStyleSheet(style.button_style())

    button_menu1 = QPushButton("Manage Room", window)
    button_menu1.clicked.connect(menu_edit)
    button_menu1.resize(260, 100)
    button_menu1.move(20, 290)
    button_menu1.setStyleSheet(style.button_style())

    button_menu2 = QPushButton("Cleaning", window)
    button_menu2.clicked.connect(menu3)
    button_menu2.resize(260, 100)
    button_menu2.move(20, 410)
    button_menu2.setStyleSheet(style.button_style())

    button_menu3 = QPushButton("Push Me", window)
    button_menu3.clicked.connect(menu4)
    button_menu3.resize(260, 100)
    button_menu3.move(20, 530)
    button_menu3.setStyleSheet(style.button_style())

    button_menu4 = QPushButton("Push Me", window)
    button_menu4.clicked.connect(menu5)
    button_menu4.resize(260, 100)
    button_menu4.move(20, 650)
    button_menu4.setStyleSheet(style.button_style())

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
