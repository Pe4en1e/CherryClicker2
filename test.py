import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.l1=QPushButton("Let's Close this Window")
        self.setCentralWidget(self.l1)
        self.setWindowTitle('close window')
        self.l1.clicked.connect(self.close)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()