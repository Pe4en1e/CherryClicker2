import sys, os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
import yaml
from yaml import Loader, Dumper


sfx_path = "sounds/effect.wav"

def startgame():
    launcher.close()
    game.show()


def savegame():
    playerscore = {
        'playerscore': Clicks.total
    }
    with open('data/playerdata.yml', 'w') as f:
        yaml.dump(playerscore, f)
    game.close()


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
        self.start_btn.setText(_translate("Launcher", "Начать игру"))


class Clicks():
    yaml_file = open('data/playerdata.yml', 'r')
    data = yaml.load(yaml_file, Loader=Loader)
    total = data['playerscore']
    click_cost=1


class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1920, 1080)
        self.centralwidget = QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QRect(160, 540, 340, 320))
        self.main_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet("border-image:url(images/cherry.png)")
        self.main_btn.setText("")
        self.main_btn.setObjectName("main_btn")
        self.score = QLabel(self.centralwidget)
        self.score.setGeometry(QRect(80, 180, 580, 80))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(255, 255, 255)")
        self.score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score.setObjectName("score")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QPixmap("images/game_bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QRect(1620, 70, 240, 70))
        self.exit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setStyleSheet("border-image:url(images/exit_btn.png)")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.label.raise_()
        self.score.raise_()
        self.main_btn.raise_()
        self.exit_btn.raise_()
        CherryClicker.setCentralWidget(self.centralwidget)


        # self.sfx = QMediaPlayer() # Медленная поебень для теста
        # self.sfx_output = QAudioOutput()
        # self.sfx.setAudioOutput(self.sfx_output)
        # self.sfx.setSource(QUrl.fromLocalFile(sfx_path))

        self.sfx = QSoundEffect() # тык sfx
        self.sfx.setSource(QUrl.fromLocalFile(sfx_path))

        

        self.retranslateUi(CherryClicker)
        QMetaObject.connectSlotsByName(CherryClicker)


    def retranslateUi(self, CherryClicker):
        _translate = QCoreApplication.translate
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.score.setText(_translate("CherryClicker", str(Clicks.total)))
        self.main_btn.clicked.connect(self.addscore)
        self.exit_btn.clicked.connect(savegame)
        

    def addscore(self):
        Clicks.total += Clicks.click_cost
        self.score.setText(str(Clicks.total))
        self.sfx.play()

        

app=QApplication(sys.argv)
ui = Ui_Launcher()
launcher=QMainWindow()
game=QMainWindow()
gameUi=Ui_CherryClicker()
gameUi.setupUi(game)
ui.setupUi(launcher)
launcher.show()
app.exec()
