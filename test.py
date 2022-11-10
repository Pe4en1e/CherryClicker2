import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

def startgame():
    window.close()
    window2.show()


class Ui_Launcher(QMainWindow):


    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(640, 320)
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QRect(340, 130, 141, 31))
        self.start_btn.setObjectName("start_btn")
        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Launcher)
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Launcher)
        self.statusbar.setObjectName("statusbar")
        Launcher.setStatusBar(self.statusbar)
        self.start_btn.clicked.connect(startgame)

        self.retranslateUi(Launcher)
        QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.start_btn.setText(_translate("Launcher", "PushButton"))


class Clicks():
    total=0
    click_cost=1


class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1920, 1080)
        self.centralwidget = QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QRect(560, 610, 220, 90))
        self.main_btn.setObjectName("main_btn")
        self.score = QLabel(self.centralwidget)
        self.score.setGeometry(QRect(170, 60, 391, 161))
        font = QFont()
        font.setPointSize(20)
        self.score.setFont(font)
        self.score.setObjectName("score")
        CherryClicker.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CherryClicker)
        self.statusbar.setObjectName("statusbar")
        CherryClicker.setStatusBar(self.statusbar)

        self.retranslateUi(CherryClicker)
        QMetaObject.connectSlotsByName(CherryClicker)


    def retranslateUi(self, CherryClicker):
        _translate = QCoreApplication.translate
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.main_btn.setText(_translate("CherryClicker", "PushButton"))
        self.score.setText(_translate("CherryClicker", str(Clicks.total)))
        self.main_btn.clicked.connect(self.addscore)
    

    def addscore(self):
        Clicks.total += Clicks.click_cost
        self.score.setText(str(Clicks.total))




app=QApplication(sys.argv)
ui = Ui_Launcher()
window=QMainWindow()
window2=QMainWindow()
gameUi=Ui_CherryClicker()
gameUi.setupUi(window2)
ui.setupUi(window)
window.show()
app.exec()

