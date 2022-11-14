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
yaml_file = open('data/playerdata.yml', 'r')
data = yaml.load(yaml_file, Loader=Loader)


def startgame():
    launcher.close()
    game.show()

def exitgame():
    game.close()

def savegame():
    playerscore = {
        'playerscore': score.total,
        'cherryjam_count': score.jam_count,
        'cherryjam_price': score.jam_price,
        'autoscore': autoscore.total
        }
    with open('data/playerdata.yml', 'w') as f:
        yaml.dump(playerscore, f)


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



class score():
    total = data['playerscore']
    jam_count = data['cherryjam_count']
    jam_price = data['cherryjam_price']
    per_click = 1


class autoscore():
    total = data['autoscore']

class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1400, 800)
        CherryClicker.setMaximumSize(1400,800)
        self.centralwidget = QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QRect(70, 390, 291, 291))
        self.main_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet("border-image:url(images/cherry.png)")
        self.main_btn.setText("")
        self.main_btn.setObjectName("main_btn")
        self.score = QLabel(self.centralwidget)
        self.score.setGeometry(QRect(20, 100, 421, 81))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(255, 255, 255)")
        self.score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score.setObjectName("score")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 1401, 801))
        self.label.setText("")
        self.label.setPixmap(QPixmap("images/game_bg.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QRect(1160, 40, 201, 71))
        self.exit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setStyleSheet("border-image:url(images/exit_btn.png)")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.click_cost = QLabel(self.centralwidget)
        self.click_cost.setGeometry(QRect(220, 200, 221, 41))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.click_cost.setFont(font)
        self.click_cost.setStyleSheet("color: rgb(255, 255, 255);")
        self.click_cost.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.click_cost.setObjectName("click_cost")
        self.per_second = QLabel(self.centralwidget)
        self.per_second.setGeometry(QRect(220, 280, 221, 41))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.per_second.setFont(font)
        self.per_second.setStyleSheet("color: rgb(255, 255, 255);")
        self.per_second.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.per_second.setObjectName("per_second")
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(450, -20, 20, 831))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(1100, 0, 20, 831))
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QRect(1160, 120, 201, 41))
        font = QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.save_btn.setObjectName("save_btn")
        self.shop_text = QLabel(self.centralwidget)
        self.shop_text.setGeometry(QRect(460, 30, 591, 81))
        font = QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.shop_text.setFont(font)
        self.shop_text.setStyleSheet("color: rgb(255, 255, 255)")
        self.shop_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shop_text.setObjectName("shop_text")
        self.cherryjam_btn = QPushButton(self.centralwidget)
        self.cherryjam_btn.setGeometry(QRect(560, 120, 391, 61))
        self.cherryjam_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cherryjam_btn.setStyleSheet("border-image:url(images/cherryjam_btn.png)")
        self.cherryjam_btn.setText("")
        self.cherryjam_btn.setObjectName("cherryjam_btn")
        self.cherrypie_btn = QPushButton(self.centralwidget)
        self.cherrypie_btn.setGeometry(QRect(560, 200, 391, 61))
        self.cherrypie_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cherrypie_btn.setStyleSheet("border-image:url(images/cherrypie_btn.png)")
        self.cherrypie_btn.setText("")
        self.cherrypie_btn.setObjectName("cherrypie_btn")
        self.cherrycake_btn = QPushButton(self.centralwidget)
        self.cherrycake_btn.setGeometry(QRect(560, 280, 391, 61))
        self.cherrycake_btn.setStyleSheet("border-image:url(images/cherrycake_btn.png)")
        self.cherrycake_btn.setText("")
        self.cherrycake_btn.setObjectName("cherrycake_btn")
        self.cherrycake_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.price_text = QLabel(self.centralwidget)
        self.price_text.setGeometry(QRect(1000, 70, 71, 21))
        font = QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.price_text.setFont(font)
        self.price_text.setStyleSheet("color: rgb(255, 255, 255)")
        self.price_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price_text.setObjectName("price_text")
        self.price_text_2 = QLabel(self.centralwidget)
        self.price_text_2.setGeometry(QRect(470, 70, 81, 21))
        font = QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.price_text_2.setFont(font)
        self.price_text_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.price_text_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price_text_2.setObjectName("price_text_2")
        self.cherryjam_price = QLabel(self.centralwidget)
        self.cherryjam_price.setGeometry(QRect(960, 120, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherryjam_price.setFont(font)
        self.cherryjam_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherryjam_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherryjam_price.setObjectName("cherryjam_price")
        self.cherryjam_count = QLabel(self.centralwidget)
        self.cherryjam_count.setGeometry(QRect(470, 120, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherryjam_count.setFont(font)
        self.cherryjam_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherryjam_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherryjam_count.setObjectName("cherryjam_count")
        self.cherrypie_count = QLabel(self.centralwidget)
        self.cherrypie_count.setGeometry(QRect(470, 200, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrypie_count.setFont(font)
        self.cherrypie_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrypie_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherrypie_count.setObjectName("cherrypie_count")
        self.cherrycake_count = QLabel(self.centralwidget)
        self.cherrycake_count.setGeometry(QRect(470, 280, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrycake_count.setFont(font)
        self.cherrycake_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrycake_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherrycake_count.setObjectName("cherrycake_count")
        self.cherrypie_price = QLabel(self.centralwidget)
        self.cherrypie_price.setGeometry(QRect(960, 200, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrypie_price.setFont(font)
        self.cherrypie_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrypie_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherrypie_price.setObjectName("cherrypie_price")
        self.cherrycake_price = QLabel(self.centralwidget)
        self.cherrycake_price.setGeometry(QRect(960, 280, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrycake_price.setFont(font)
        self.cherrycake_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrycake_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cherrycake_price.setObjectName("cherrycake_price")
        self.label.raise_()
        self.score.raise_()
        self.main_btn.raise_()
        self.click_cost.raise_()
        self.per_second.raise_()
        self.exit_btn.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.save_btn.raise_()
        self.shop_text.raise_()
        self.cherryjam_btn.raise_()
        self.cherrypie_btn.raise_()
        self.cherrycake_btn.raise_()
        self.price_text.raise_()
        self.price_text_2.raise_()
        self.cherryjam_price.raise_()
        self.cherryjam_count.raise_()
        self.cherrypie_count.raise_()
        self.cherrycake_count.raise_()
        self.cherrypie_price.raise_()
        self.cherrycake_price.raise_()
        CherryClicker.setCentralWidget(self.centralwidget)


        self.sfx = QSoundEffect() # тык sfx
        self.sfx.setSource(QUrl.fromLocalFile(sfx_path))

    
        self.retranslateUi(CherryClicker)
        QMetaObject.connectSlotsByName(CherryClicker)


    def retranslateUi(self, CherryClicker):
        _translate = QCoreApplication.translate
        self.click_cost.setText(_translate("CherryClicker", "1"))
        self.per_second.setText(_translate("CherryClicker", str(autoscore.total)))
        self.save_btn.setText(_translate("CherryClicker", "СОХРАНИТЬ"))
        self.shop_text.setText(_translate("CherryClicker", "Магазин"))
        self.price_text.setText(_translate("CherryClicker", "Цена"))
        self.price_text_2.setText(_translate("CherryClicker", "Кол-во"))
        self.cherryjam_price.setText(_translate("CherryClicker", str(score.jam_price)))
        self.cherryjam_count.setText(_translate("CherryClicker", str(score.jam_count)))
        self.cherrypie_count.setText(_translate("CherryClicker", "0"))
        self.cherrycake_count.setText(_translate("CherryClicker", "0"))
        self.cherrypie_price.setText(_translate("CherryClicker", "100"))
        self.cherrycake_price.setText(_translate("CherryClicker", "150"))
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.score.setText(_translate("CherryClicker", str(score.total)))
        self.main_btn.clicked.connect(self.addscore)
        self.exit_btn.clicked.connect(exitgame)
        self.save_btn.clicked.connect(savegame)


        self.timer = QTimer()
        self.timer.timeout.connect(self.autofarm)
        self.timer.setInterval(1000)
        self.timer.start()
        

        self.cherryjam_btn.clicked.connect(self.buy_cherryjam)

    def autofarm(self):
        score.total += autoscore.total
        self.score.setText(str(score.total))


    def addscore(self):
        score.total += score.per_click
        self.sfx.play()
        self.score.setText(str(score.total))

    def buy_cherryjam(self):
        if score.total >= score.jam_price:
            score.jam_count += 1
            autoscore.total += 5
            score.total = score.total-score.jam_price
            score.jam_price = round(score.jam_price*1.01**score.jam_count)
            self.cherryjam_count.setText(str(score.jam_count))
            self.cherryjam_price.setText(str(score.jam_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
            
        else:
            print('ты нищий')




app=QApplication(sys.argv)
ui = Ui_Launcher()
launcher=QMainWindow()
game=QMainWindow()
gameUi=Ui_CherryClicker()
gameUi.setupUi(game)
ui.setupUi(launcher)
launcher.show()
app.exec()
