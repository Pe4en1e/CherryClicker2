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
click_sfx_path = 'sounds/click_sfx.wav'
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
    score.vyshnivka_count = 0
    score.vyshnivka_price = 400
    score.makskust_count = 0
    score.makskust_price = 800
    score.mur_price = 1500
    score.mur_count = 0
    score.hqd_price = 3000
    score.hqd_count = 0
    score.rebirth_pb = 0
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
        'cherrycake_price': score.cake_price,
        'vyshnivka_count': score.vyshnivka_count,
        'vyshnivka_price': score.vyshnivka_price,
        'kust_count': score.makskust_count,
        'kust_price': score.makskust_price,
        'mur_count': score.mur_count,
        'mur_price': score.mur_price,
        'hqd_count': score.hqd_count,
        'hqd_price': score.hqd_price,
        'rb_tier': score.rebirth_tier,
        'rb_progress': score.rebirth_pb
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


        self.click_sfx = QSoundEffect() # click
        self.click_sfx.setSource(QUrl.fromLocalFile(click_sfx_path))


        self.continue_btn.clicked.connect(continuegame)
        self.continue_btn.clicked.connect(self.play_click_sfx)
        self.newgame_btn.clicked.connect(newgame)
        self.newgame_btn.clicked.connect(self.play_click_sfx)

        self.retranslateUi(Launcher)
        QMetaObject.connectSlotsByName(Launcher)

    def play_click_sfx(self):
        self.click_sfx.play()


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
    vyshnivka_count = data['vyshnivka_count']
    vyshnivka_price = data['vyshnivka_price']
    makskust_count = data['kust_count']
    makskust_price = data['kust_price']
    mur_count = data['mur_count']
    mur_price =data['mur_price']
    hqd_price = data['hqd_price']
    hqd_count = data['hqd_count']
    rebirth_tier = data['rb_tier']
    rebirth_pb = data['rb_progress']
    click_factor = 1.5
    auto_factor = 1.3


class autoscore():
    total = data['autoscore']

class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1400, 800)
        CherryClicker.setMaximumSize(QSize(1400, 800))
        CherryClicker.setMinimumSize(QSize(1400, 800))
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        CherryClicker.setWindowIcon(icon)
        CherryClicker.setLocale(QLocale(QLocale.Language.Ukrainian, QLocale.Country.Ukraine))
        self.centralwidget = QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QRect(80, 440, 251, 251))
        self.main_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet("border-image:url(images/cherry.png)")
        self.main_btn.setText("")
        self.main_btn.setObjectName("main_btn")
        self.score = QLabel(self.centralwidget)
        self.score.setGeometry(QRect(10, 100, 431, 81))
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
        self.exit_btn.setGeometry(QRect(1140, 40, 241, 71))
        self.exit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setStyleSheet("border-image:url(images/exit_btn.png)")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.click_cost = QLabel(self.centralwidget)
        self.click_cost.setGeometry(QRect(280, 200, 161, 41))
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
        self.line.setGeometry(QRect(440, -20, 20, 831))
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(1100, -10, 20, 831))
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QRect(1140, 120, 241, 51))
        font = QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.save_btn.setStyleSheet("border-image:url(images/save_btn.png)")
        self.save_btn.setText("")
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
        self.cherrycake_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cherrycake_btn.setStyleSheet("border-image:url(images/cherrycake_btn.png)")
        self.cherrycake_btn.setText("")
        self.cherrycake_btn.setObjectName("cherrycake_btn")
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
        self.vyshnivka_count = QLabel(self.centralwidget)
        self.vyshnivka_count.setGeometry(QRect(470, 360, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.vyshnivka_count.setFont(font)
        self.vyshnivka_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.vyshnivka_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vyshnivka_count.setObjectName("vyshnivka_count")
        self.vyshnivka_btn = QPushButton(self.centralwidget)
        self.vyshnivka_btn.setGeometry(QRect(560, 360, 391, 61))
        self.vyshnivka_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.vyshnivka_btn.setStyleSheet("border-image:url(images/vyshnivka_btn.png)")
        self.vyshnivka_btn.setText("")
        self.vyshnivka_btn.setObjectName("vyshnivka_btn")
        self.vyshnivka_price = QLabel(self.centralwidget)
        self.vyshnivka_price.setGeometry(QRect(960, 360, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.vyshnivka_price.setFont(font)
        self.vyshnivka_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.vyshnivka_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vyshnivka_price.setObjectName("vyshnivka_price")
        self.notify = QLabel(self.centralwidget)
        self.notify.setGeometry(QRect(0, 330, 441, 81))
        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.notify.setFont(font)
        self.notify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.notify.setStyleSheet("color: #ffffff")
        self.notify.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.notify.setObjectName("notify")
        self.makskust_btn = QPushButton(self.centralwidget)
        self.makskust_btn.setGeometry(QRect(560, 440, 391, 61))
        self.makskust_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.makskust_btn.setStyleSheet("border-image:url(images/maxkust.png)")
        self.makskust_btn.setText("")
        self.makskust_btn.setObjectName("makskust_btn")
        self.makskust_price = QLabel(self.centralwidget)
        self.makskust_price.setGeometry(QRect(960, 440, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.makskust_price.setFont(font)
        self.makskust_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.makskust_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.makskust_price.setObjectName("makskust_price")
        self.makskust_count = QLabel(self.centralwidget)
        self.makskust_count.setGeometry(QRect(470, 440, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.makskust_count.setFont(font)
        self.makskust_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.makskust_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.makskust_count.setObjectName("makskust_count")
        self.mur_count = QLabel(self.centralwidget)
        self.mur_count.setGeometry(QRect(470, 520, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mur_count.setFont(font)
        self.mur_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.mur_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mur_count.setObjectName("mur_count")
        self.mur_btn = QPushButton(self.centralwidget)
        self.mur_btn.setGeometry(QRect(560, 520, 391, 61))
        self.mur_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mur_btn.setStyleSheet("border-image:url(images/mur_btn.png)")
        self.mur_btn.setText("")
        self.mur_btn.setObjectName("mur_btn")
        self.mur_price = QLabel(self.centralwidget)
        self.mur_price.setGeometry(QRect(960, 520, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mur_price.setFont(font)
        self.mur_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.mur_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mur_price.setObjectName("mur_price")
        self.hqd_btn = QPushButton(self.centralwidget)
        self.hqd_btn.setGeometry(QRect(560, 600, 391, 61))
        self.hqd_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hqd_btn.setStyleSheet("border-image:url(images/hqd_btn.png)")
        self.hqd_btn.setText("")
        self.hqd_btn.setObjectName("hqd_btn")
        self.hqd_count = QLabel(self.centralwidget)
        self.hqd_count.setGeometry(QRect(470, 600, 81, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hqd_count.setFont(font)
        self.hqd_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.hqd_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hqd_count.setObjectName("hqd_count")
        self.hqd_price = QLabel(self.centralwidget)
        self.hqd_price.setGeometry(QRect(960, 600, 141, 51))
        font = QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hqd_price.setFont(font)
        self.hqd_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.hqd_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hqd_price.setObjectName("hqd_price")
        self.rb_bar = QProgressBar(self.centralwidget)
        self.rb_bar.setGeometry(QRect(1140, 242, 241, 21))
        self.rb_bar.setAutoFillBackground(False)
        self.rb_bar.setStyleSheet("#rb_bar{\n""background-color: #16161a;\n""border: 2px solid #FFFFFF;\n""}\n""\n""#rb_bar::chunk {\n""background-color: #7f5af0;\n""}")
        self.rb_bar.setProperty("value", score.rebirth_pb)
        self.rb_bar.setTextVisible(False)
        self.rb_bar.setObjectName("rb_bar")
        self.rb_txt = QLabel(self.centralwidget)
        self.rb_txt.setGeometry(QRect(1140, 205, 241, 31))
        font = QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(18)
        self.rb_txt.setFont(font)
        self.rb_txt.setStyleSheet("color: #ffffff")
        self.rb_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rb_txt.setObjectName("rb_txt")
        self.rb_btn = QPushButton(self.centralwidget)
        self.rb_btn.setEnabled(True)
        self.rb_btn.setGeometry(QRect(1140, 270, 241, 31))
        self.rb_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_btn.setObjectName("rb_btn")
        self.rb_btn.setEnabled(False)
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
        self.vyshnivka_count.raise_()
        self.vyshnivka_btn.raise_()
        self.vyshnivka_price.raise_()
        self.notify.raise_()
        self.makskust_btn.raise_()
        self.makskust_price.raise_()
        self.makskust_count.raise_()
        self.mur_count.raise_()
        self.mur_btn.raise_()
        self.mur_price.raise_()
        self.hqd_btn.raise_()
        self.hqd_count.raise_()
        self.hqd_price.raise_()
        self.rb_bar.raise_()
        self.rb_txt.raise_()
        self.rb_btn.raise_()
        CherryClicker.setCentralWidget(self.centralwidget)


        self.sfx = QSoundEffect() # тык sfx
        self.sfx.setSource(QUrl.fromLocalFile(sfx_path))
        self.click_sfx = QSoundEffect() # click
        self.click_sfx.setSource(QUrl.fromLocalFile(click_sfx_path))

    
        self.retranslateUi(CherryClicker)
        QMetaObject.connectSlotsByName(CherryClicker)


    def retranslateUi(self, CherryClicker):
        _translate = QCoreApplication.translate
        self.click_cost.setText(_translate("CherryClicker", "1"))
        self.per_second.setText(_translate("CherryClicker", str(autoscore.total)))
        self.shop_text.setText(_translate("CherryClicker", "Магазин"))
        self.price_text.setText(_translate("CherryClicker", "Цена"))
        self.price_text_2.setText(_translate("CherryClicker", "Кол-во"))
        self.cherryjam_price.setText(_translate("CherryClicker", str(score.jam_price)))
        self.cherryjam_count.setText(_translate("CherryClicker", str(score.jam_count)))
        self.cherrypie_count.setText(_translate("CherryClicker", str(score.pie_count)))
        self.cherrycake_count.setText(_translate("CherryClicker", str(score.cake_count)))
        self.cherrypie_price.setText(_translate("CherryClicker", str(score.pie_price)))
        self.cherrycake_price.setText(_translate("CherryClicker", str(score.cake_count)))
        self.vyshnivka_count.setText(_translate("CherryClicker", str(score.vyshnivka_count)))
        self.vyshnivka_price.setText(_translate("CherryClicker", str(score.vyshnivka_price)))
        self.makskust_price.setText(_translate("CherryClicker", str(score.makskust_price)))
        self.makskust_count.setText(_translate("CherryClicker", str(score.makskust_count)))
        self.mur_count.setText(_translate("CherryClicker", str(score.mur_count)))
        self.mur_price.setText(_translate("CherryClicker", str(score.mur_price)))
        self.hqd_count.setText(_translate("CherryClicker", str(score.hqd_count)))
        self.hqd_price.setText(_translate("CherryClicker", str(score.hqd_price)))
        self.rb_txt.setText(_translate("CherryClicker", "Tier 1"))
        self.rb_btn.setText(_translate("CherryClicker", "RE-BIRTH"))

        self.notify.setText(_translate("CherryClicker", ""))
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.score.setText(_translate("CherryClicker", str(score.total)))
        self.main_btn.clicked.connect(self.addscore)
        self.exit_btn.clicked.connect(exitgame)
        self.exit_btn.clicked.connect(self.play_click_sfx)
        self.save_btn.clicked.connect(savegame)
        self.save_btn.clicked.connect(self.play_click_sfx)


        self.timer = QTimer()
        self.timer.timeout.connect(self.autofarm)
        self.timer.setInterval(1000)
        self.timer.start()
        

        self.cherryjam_btn.clicked.connect(self.buy_cherryjam)
        self.cherrypie_btn.clicked.connect(self.buy_cherrypie)
        self.cherrycake_btn.clicked.connect(self.buy_cherrycake)
        self.vyshnivka_btn.clicked.connect(self.buy_vyshnivka)
        self.makskust_btn.clicked.connect(self.buy_makskust)
        self.mur_btn.clicked.connect(self.buy_mur)
        self.hqd_btn.clicked.connect(self.buy_hqd)

        
    def play_click_sfx(self):
        self.click_sfx.play()

    def nomoney(self):
        self.notify.setText('Недостаточно денег!')

    def noprev(self):
        self.notify.setText('Купите предыдущее\nулучшение!')

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
        self.vyshnivka_count.setText(str(score.vyshnivka_count))
        self.vyshnivka_price.setText(str(score.vyshnivka_price))
        self.makskust_count.setText(str(score.makskust_count))
        self.makskust_price.setText(str(score.makskust_price))
        self.mur_count.setText(str(score.mur_count))
        self.mur_price.setText(str(score.mur_price))
        self.hqd_count.setText(str(score.hqd_count))
        self.hqd_price.setText(str(score.hqd_price))
        score.rebirth_pb = score.total/10000
        self.rb_bar.setProperty('value', score.rebirth_pb)
        if score.total >= 1000000:
            self.rb_btn.setEnabled(True)
        else:
            self.rb_btn.setEnabled(False)
        self.notify.setText('')
        

    def addscore(self):
        score.total += score.per_click
        self.sfx.play()
        self.score.setText(str(score.total))
        score.rebirth_pb = score.total/10000
        self.rb_bar.setProperty('value', score.rebirth_pb)
        if score.total >= 1000000:
            self.rb_btn.setEnabled(True)
        else:
            self.rb_btn.setEnabled(False)

    def buy_cherryjam(self):
        self.play_click_sfx()
        if score.total >= score.jam_price:
            score.jam_count += 1
            autoscore.total += 1
            score.total = score.total-score.jam_price
            score.jam_price = round(score.jam_price*score.auto_factor)
            self.cherryjam_count.setText(str(score.jam_count))
            self.cherryjam_price.setText(str(score.jam_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        else:
            self.nomoney()

    def buy_cherrypie(self):
        self.play_click_sfx()
        if score.total >= score.pie_price and score.jam_count>=1:
            score.pie_count += 1
            autoscore.total += 5
            score.total = score.total-score.pie_price
            score.pie_price = round(score.pie_price*score.auto_factor)
            self.cherrypie_count.setText(str(score.pie_count))
            self.cherrypie_price.setText(str(score.pie_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        elif score.total >= score.pie_price and score.jam_count==0:
            self.noprev()
        else:
            self.nomoney()

    def buy_cherrycake(self):
        self.play_click_sfx()
        if score.total >= score.cake_price and score.pie_count>=1:
            score.cake_count += 1
            score.per_click += 1
            score.total = score.total-score.cake_price
            score.cake_price = round(score.cake_price*score.click_factor)
            self.cherrycake_count.setText(str(score.cake_count))
            self.cherrycake_price.setText(str(score.cake_price))
            self.click_cost.setText(str(score.per_click))
            self.score.setText(str(score.total))
        elif score.total >= score.cake_price and score.pie_count==0:
            self.noprev()
        else:
            self.nomoney()
    
    def buy_vyshnivka(self):
        self.play_click_sfx()
        if score.total >= score.vyshnivka_price and score.cake_count >=1:
            score.vyshnivka_count += 1
            autoscore.total += 10
            score.total = score.total - score.vyshnivka_price
            score.vyshnivka_price = round(score.vyshnivka_price*score.auto_factor)
            self.vyshnivka_count.setText(str(score.vyshnivka_count))
            self.vyshnivka_price.setText(str(score.vyshnivka_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        elif score.total >= score.vyshnivka_price and score.cake_count==0:
            self.noprev()
        else:
            self.nomoney()
        
    def buy_makskust(self):
        self.play_click_sfx()
        if score.total >= score.makskust_price and score.vyshnivka_count>=1:
            score.makskust_count += 1
            autoscore.total += 25
            score.total = score.total - score.makskust_price
            score.makskust_price = round(score.makskust_price*score.auto_factor)
            self.makskust_count.setText(str(score.makskust_count))
            self.makskust_price.setText(str(score.makskust_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        elif score.total >= score.makskust_price and score.vyshnivka_count==0:
            self.noprev()
        else:
            self.nomoney()


    def buy_mur(self):
        self.play_click_sfx()
        if score.total >= score.mur_price and score.makskust_count>=1:
            score.mur_count += 1
            autoscore.total += 50
            score.total = score.total - score.mur_price
            score.mur_price = round(score.mur_price*score.auto_factor)
            self.mur_count.setText(str(score.mur_count))
            self.mur_price.setText(str(score.mur_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        elif score.total >= score.mur_price and score.makskust_count==0:
            self.noprev()
        else:
            self.nomoney()

    def buy_hqd(self):
        self.play_click_sfx()
        if score.total >= score.hqd_price and score.mur_count>=1:
            score.hqd_count += 1
            autoscore.total += 100
            score.total = score.total-score.hqd_price
            score.hqd_price = round(score.hqd_price*score.auto_factor)
            self.hqd_count.setText(str(score.hqd_count))
            self.hqd_price.setText(str(score.hqd_price))
            self.per_second.setText(str(autoscore.total))
            self.score.setText(str(score.total))
        elif score.total >= score.hqd_price and score.mur_count>=0:
           self.noprev()
        else:
            self.nomoney() 


app=QApplication(sys.argv)
ui = Ui_Launcher()
launcher=QMainWindow()
game=QMainWindow()
gameUi=Ui_CherryClicker()
gameUi.setupUi(game)
ui.setupUi(launcher)
launcher.show()
app.exec()
