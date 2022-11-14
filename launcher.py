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


def newgame():
    launcher.close()
    score.total = 0
    score.jam_count = 0
    score.jam_price = 15
    autoscore.total = 0
    score.pie_price = 100
    score.pie_count = 0
    score.per_click = 1
    score.cake_count = 0
    score.cake_price = 150
    game.show()

def continuegame():
    launcher.close()
    game.show()

def exitgame():
    game.close()
    launcher.show()

def savegame():
    playerscore = {
        'playerscore': score.total,
        'cherryjam_count': score.jam_count,
        'cherryjam_price': score.jam_price,
        'autoscore': autoscore.total,
        'cherrypie_price': score.pie_price,
        'cherrypie_count': score.pie_count,
        'per_click': score.per_click,
        'cherrycake_count': score.cake_count,
        'cherrycake_price': score.cake_price
        }
    with open('data/playerdata.yml', 'w') as f:
        yaml.dump(playerscore, f)


class Ui_Launcher(QMainWindow):


    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(640, 320)
        Launcher.setMinimumSize(QSize(640, 320))
        Launcher.setMaximumSize(QSize(640, 320))
        Launcher.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        Launcher.setWindowIcon(icon)
        Launcher.setLocale(QLocale(QLocale.Language.Ukrainian, QLocale.Country.Ukraine))
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName("centralwidget")
        self.newgame_btn = QPushButton(self.centralwidget)
        self.newgame_btn.setGeometry(QRect(10, 130, 171, 41))
        font = QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.newgame_btn.setFont(font)
        self.newgame_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newgame_btn.setStyleSheet("background-color: #7f5af0;\n""color: #fffffe\n""")
        self.newgame_btn.setObjectName("newgame_btn")
        self.continue_btn = QPushButton(self.centralwidget)
        self.continue_btn.setGeometry(QRect(10, 180, 171, 41))
        font = QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.continue_btn.setFont(font)
        self.continue_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.continue_btn.setStyleSheet("background-color: #7f5af0;\n""color: #fffffe\n""")
        self.continue_btn.setObjectName("continue_btn")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 641, 321))
        self.label.setText("")
        self.label.setPixmap(QPixmap("images/launcher.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.newgame_btn.raise_()
        self.continue_btn.raise_()
        Launcher.setCentralWidget(self.centralwidget)



        self.continue_btn.clicked.connect(continuegame)
        self.newgame_btn.clicked.connect(newgame)

        self.retranslateUi(Launcher)
        QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.newgame_btn.setText(_translate("Launcher", "Новая игра"))
        self.continue_btn.setText(_translate("Launcher", "Продолжить "))


class score():
    total = data['playerscore']
    jam_count = data['cherryjam_count']
    jam_price = data['cherryjam_price']
    pie_count = data['cherrypie_count']
    pie_price = data ['cherrypie_price']
    cake_count = data['cherrycake_count']
    cake_price = data['cherrycake_price']
    per_click = data['per_click']
    click_factor = 1.5
    auto_factor = 1.3


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
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        CherryClicker.setWindowIcon(icon)
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
        self.cherrypie_count.setText(_translate("CherryClicker", str(score.pie_count)))
        self.cherrycake_count.setText(_translate("CherryClicker", str(score.cake_count)))
        self.cherrypie_price.setText(_translate("CherryClicker", str(score.pie_price)))
        self.cherrycake_price.setText(_translate("CherryClicker", str(score.cake_count)))
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
        self.cherrypie_btn.clicked.connect(self.buy_cherrypie)
        self.cherrycake_btn.clicked.connect(self.buy_cherrycake)

    def resettext(self):
        self.score.setText(str(score.total))
        self.click_cost.setText(str(score.per_click))
        self.per_second.setText(str(autoscore.total))
        self.cherryjam_count.setText(str(score.jam_count))
        self.cherryjam_price.setText(str(score.jam_price))

    def autofarm(self):
        score.total += autoscore.total
        self.score.setText(str(score.total))
        self.click_cost.setText(str(score.per_click))
        self.per_second.setText(str(autoscore.total))
        self.cherryjam_count.setText(str(score.jam_count))
        self.cherryjam_price.setText(str(score.jam_price))
        self.cherrypie_count.setText(str(score.pie_count))
        self.cherrypie_price.setText(str(score.pie_price))
        self.cherrycake_count.setText(str(score.cake_count))
        self.cherrycake_price.setText(str(score.cake_price))


    def addscore(self):
        score.total += score.per_click
        self.sfx.play()
        self.score.setText(str(score.total))

    def buy_cherryjam(self):
        if score.total >= score.jam_price:
            score.jam_count += 1
            autoscore.total += 5
            score.total = score.total-score.jam_price
            score.jam_price = round(score.jam_price*score.auto_factor)
            self.cherryjam_count.setText(str(score.jam_count))
            self.cherryjam_price.setText(str(score.jam_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        else:
            print('ты нищий')

    def buy_cherrypie(self):
        if score.total >= score.pie_price and score.jam_count>=1:
            score.pie_count += 1
            autoscore.total += 10
            score.total = score.total-score.pie_price
            score.pie_price = round(score.pie_price*score.auto_factor)
            self.cherrypie_count.setText(str(score.pie_count))
            self.cherrypie_price.setText(str(score.pie_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        else:
            print('ты нищий')

    def buy_cherrycake(self):
        if score.total >= score.cake_price and score.pie_count>=1:
            score.cake_count += 1
            score.per_click += 1
            score.total = score.total-score.cake_price
            score.cake_price = round(score.cake_price*score.click_factor)
            self.cherrycake_count.setText(str(score.cake_count))
            self.cherrycake_price.setText(str(score.cake_price))
            self.click_cost.setText(str(score.per_click))
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
