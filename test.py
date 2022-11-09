import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

def startgame():
    window.close()
    window2.show()

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

        button.clicked.connect(startgame)

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App 2")

        # Устанавливаем центральный виджет Window.

app = QApplication(sys.argv)

window2= MainWindow2()
window = MainWindow()
window.show()


app.exec()