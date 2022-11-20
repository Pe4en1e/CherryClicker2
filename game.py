# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1400, 800)
        CherryClicker.setMinimumSize(QtCore.QSize(1400, 800))
        CherryClicker.setMaximumSize(QtCore.QSize(1400, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        CherryClicker.setWindowIcon(icon)
        CherryClicker.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Ukrainian, QtCore.QLocale.Country.Ukraine))
        self.centralwidget = QtWidgets.QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QtCore.QRect(80, 440, 251, 251))
        self.main_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet("border-image:url(images/cherry.png)")
        self.main_btn.setText("")
        self.main_btn.setObjectName("main_btn")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(10, 100, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(255, 255, 255)")
        self.score.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score.setObjectName("score")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1401, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/game_bg.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(1140, 40, 241, 71))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setStyleSheet("border-image:url(images/exit_btn.png)")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.click_cost = QtWidgets.QLabel(self.centralwidget)
        self.click_cost.setGeometry(QtCore.QRect(280, 200, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.click_cost.setFont(font)
        self.click_cost.setStyleSheet("color: rgb(255, 255, 255);")
        self.click_cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.click_cost.setObjectName("click_cost")
        self.per_second = QtWidgets.QLabel(self.centralwidget)
        self.per_second.setGeometry(QtCore.QRect(220, 280, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.per_second.setFont(font)
        self.per_second.setStyleSheet("color: rgb(255, 255, 255);")
        self.per_second.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.per_second.setObjectName("per_second")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(440, -20, 20, 831))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1100, -10, 20, 831))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(1140, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.save_btn.setStyleSheet("border-image:url(images/save_btn.png)")
        self.save_btn.setText("")
        self.save_btn.setObjectName("save_btn")
        self.shop_text = QtWidgets.QLabel(self.centralwidget)
        self.shop_text.setGeometry(QtCore.QRect(460, 30, 591, 81))
        font = QtGui.QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.shop_text.setFont(font)
        self.shop_text.setStyleSheet("color: rgb(255, 255, 255)")
        self.shop_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.shop_text.setObjectName("shop_text")
        self.cherryjam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cherryjam_btn.setGeometry(QtCore.QRect(560, 120, 391, 61))
        self.cherryjam_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cherryjam_btn.setStyleSheet("border-image:url(images/cherryjam_btn.png)")
        self.cherryjam_btn.setText("")
        self.cherryjam_btn.setObjectName("cherryjam_btn")
        self.cherrypie_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cherrypie_btn.setGeometry(QtCore.QRect(560, 200, 391, 61))
        self.cherrypie_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cherrypie_btn.setStyleSheet("border-image:url(images/cherrypie_btn.png)")
        self.cherrypie_btn.setText("")
        self.cherrypie_btn.setObjectName("cherrypie_btn")
        self.cherrycake_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cherrycake_btn.setGeometry(QtCore.QRect(560, 280, 391, 61))
        self.cherrycake_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cherrycake_btn.setStyleSheet("border-image:url(images/cherrycake_btn.png)")
        self.cherrycake_btn.setText("")
        self.cherrycake_btn.setObjectName("cherrycake_btn")
        self.price_text = QtWidgets.QLabel(self.centralwidget)
        self.price_text.setGeometry(QtCore.QRect(1000, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.price_text.setFont(font)
        self.price_text.setStyleSheet("color: rgb(255, 255, 255)")
        self.price_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.price_text.setObjectName("price_text")
        self.price_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.price_text_2.setGeometry(QtCore.QRect(470, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Bubbleboddy Neue Trial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.price_text_2.setFont(font)
        self.price_text_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.price_text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.price_text_2.setObjectName("price_text_2")
        self.cherryjam_price = QtWidgets.QLabel(self.centralwidget)
        self.cherryjam_price.setGeometry(QtCore.QRect(960, 120, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherryjam_price.setFont(font)
        self.cherryjam_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherryjam_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherryjam_price.setObjectName("cherryjam_price")
        self.cherryjam_count = QtWidgets.QLabel(self.centralwidget)
        self.cherryjam_count.setGeometry(QtCore.QRect(470, 120, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherryjam_count.setFont(font)
        self.cherryjam_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherryjam_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherryjam_count.setObjectName("cherryjam_count")
        self.cherrypie_count = QtWidgets.QLabel(self.centralwidget)
        self.cherrypie_count.setGeometry(QtCore.QRect(470, 200, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrypie_count.setFont(font)
        self.cherrypie_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrypie_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherrypie_count.setObjectName("cherrypie_count")
        self.cherrycake_count = QtWidgets.QLabel(self.centralwidget)
        self.cherrycake_count.setGeometry(QtCore.QRect(470, 280, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrycake_count.setFont(font)
        self.cherrycake_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrycake_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherrycake_count.setObjectName("cherrycake_count")
        self.cherrypie_price = QtWidgets.QLabel(self.centralwidget)
        self.cherrypie_price.setGeometry(QtCore.QRect(960, 200, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrypie_price.setFont(font)
        self.cherrypie_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrypie_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherrypie_price.setObjectName("cherrypie_price")
        self.cherrycake_price = QtWidgets.QLabel(self.centralwidget)
        self.cherrycake_price.setGeometry(QtCore.QRect(960, 280, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cherrycake_price.setFont(font)
        self.cherrycake_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.cherrycake_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cherrycake_price.setObjectName("cherrycake_price")
        self.vyshnivka_count = QtWidgets.QLabel(self.centralwidget)
        self.vyshnivka_count.setGeometry(QtCore.QRect(470, 360, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.vyshnivka_count.setFont(font)
        self.vyshnivka_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.vyshnivka_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vyshnivka_count.setObjectName("vyshnivka_count")
        self.vyshnivka_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vyshnivka_btn.setGeometry(QtCore.QRect(560, 360, 391, 61))
        self.vyshnivka_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.vyshnivka_btn.setStyleSheet("border-image:url(images/vyshnivka_btn.png)")
        self.vyshnivka_btn.setText("")
        self.vyshnivka_btn.setObjectName("vyshnivka_btn")
        self.vyshnivka_price = QtWidgets.QLabel(self.centralwidget)
        self.vyshnivka_price.setGeometry(QtCore.QRect(960, 360, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.vyshnivka_price.setFont(font)
        self.vyshnivka_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.vyshnivka_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vyshnivka_price.setObjectName("vyshnivka_price")
        self.notify = QtWidgets.QLabel(self.centralwidget)
        self.notify.setGeometry(QtCore.QRect(0, 350, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.notify.setFont(font)
        self.notify.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.notify.setStyleSheet("color: #ffffff")
        self.notify.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notify.setObjectName("notify")
        self.makskust_btn = QtWidgets.QPushButton(self.centralwidget)
        self.makskust_btn.setGeometry(QtCore.QRect(560, 440, 391, 61))
        self.makskust_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.makskust_btn.setStyleSheet("border-image:url(images/maxkust.png)")
        self.makskust_btn.setText("")
        self.makskust_btn.setObjectName("makskust_btn")
        self.makskust_price = QtWidgets.QLabel(self.centralwidget)
        self.makskust_price.setGeometry(QtCore.QRect(960, 440, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.makskust_price.setFont(font)
        self.makskust_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.makskust_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.makskust_price.setObjectName("makskust_price")
        self.makskust_count = QtWidgets.QLabel(self.centralwidget)
        self.makskust_count.setGeometry(QtCore.QRect(470, 440, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.makskust_count.setFont(font)
        self.makskust_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.makskust_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.makskust_count.setObjectName("makskust_count")
        self.mur_count = QtWidgets.QLabel(self.centralwidget)
        self.mur_count.setGeometry(QtCore.QRect(470, 520, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mur_count.setFont(font)
        self.mur_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.mur_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mur_count.setObjectName("mur_count")
        self.mur_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mur_btn.setGeometry(QtCore.QRect(560, 520, 391, 61))
        self.mur_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mur_btn.setStyleSheet("border-image:url(images/mur_btn.png)")
        self.mur_btn.setText("")
        self.mur_btn.setObjectName("mur_btn")
        self.mur_price = QtWidgets.QLabel(self.centralwidget)
        self.mur_price.setGeometry(QtCore.QRect(960, 520, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mur_price.setFont(font)
        self.mur_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.mur_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mur_price.setObjectName("mur_price")
        self.hqd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hqd_btn.setGeometry(QtCore.QRect(560, 600, 391, 61))
        self.hqd_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hqd_btn.setStyleSheet("border-image:url(images/hqd_btn.png)")
        self.hqd_btn.setText("")
        self.hqd_btn.setObjectName("hqd_btn")
        self.hqd_count = QtWidgets.QLabel(self.centralwidget)
        self.hqd_count.setGeometry(QtCore.QRect(470, 600, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hqd_count.setFont(font)
        self.hqd_count.setStyleSheet("color: rgb(255, 255, 255)")
        self.hqd_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hqd_count.setObjectName("hqd_count")
        self.hqd_price = QtWidgets.QLabel(self.centralwidget)
        self.hqd_price.setGeometry(QtCore.QRect(960, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hqd_price.setFont(font)
        self.hqd_price.setStyleSheet("color: rgb(255, 255, 255)")
        self.hqd_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hqd_price.setObjectName("hqd_price")
        self.rb_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.rb_bar.setGeometry(QtCore.QRect(1140, 242, 241, 21))
        self.rb_bar.setAutoFillBackground(False)
        self.rb_bar.setStyleSheet("#rb_bar{\n""background-color: #16161a;\n""border: 2px solid #FFFFFF;\n""}\n""\n""#rb_bar::chunk {\n""background-color: #7f5af0;\n""}")
        self.rb_bar.setProperty("value", 24)
        self.rb_bar.setTextVisible(False)
        self.rb_bar.setObjectName("rb_bar")
        self.rb_txt = QtWidgets.QLabel(self.centralwidget)
        self.rb_txt.setGeometry(QtCore.QRect(1140, 205, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(18)
        self.rb_txt.setFont(font)
        self.rb_txt.setStyleSheet("color: #ffffff")
        self.rb_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rb_txt.setObjectName("rb_txt")
        self.rb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rb_btn.setEnabled(True)
        self.rb_btn.setGeometry(QtCore.QRect(1140, 270, 241, 31))
        self.rb_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rb_btn.setObjectName("rb_btn")
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

        self.retranslateUi(CherryClicker)
        QtCore.QMetaObject.connectSlotsByName(CherryClicker)

    def retranslateUi(self, CherryClicker):
        _translate = QtCore.QCoreApplication.translate
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.score.setText(_translate("CherryClicker", "0"))
        self.click_cost.setText(_translate("CherryClicker", "1"))
        self.per_second.setText(_translate("CherryClicker", "0"))
        self.shop_text.setText(_translate("CherryClicker", "Магазин"))
        self.price_text.setText(_translate("CherryClicker", "Цена"))
        self.price_text_2.setText(_translate("CherryClicker", "Кол-во"))
        self.cherryjam_price.setText(_translate("CherryClicker", "15"))
        self.cherryjam_count.setText(_translate("CherryClicker", "0"))
        self.cherrypie_count.setText(_translate("CherryClicker", "0"))
        self.cherrycake_count.setText(_translate("CherryClicker", "0"))
        self.cherrypie_price.setText(_translate("CherryClicker", "100"))
        self.cherrycake_price.setText(_translate("CherryClicker", "150"))
        self.vyshnivka_count.setText(_translate("CherryClicker", "0"))
        self.vyshnivka_price.setText(_translate("CherryClicker", "400"))
        self.notify.setText(_translate("CherryClicker", "NOTIFY"))
        self.makskust_price.setText(_translate("CherryClicker", "800"))
        self.makskust_count.setText(_translate("CherryClicker", "0"))
        self.mur_count.setText(_translate("CherryClicker", "0"))
        self.mur_price.setText(_translate("CherryClicker", "1500"))
        self.hqd_count.setText(_translate("CherryClicker", "0"))
        self.hqd_price.setText(_translate("CherryClicker", "3000"))
        self.rb_txt.setText(_translate("CherryClicker", "Tier 1"))
        self.rb_btn.setText(_translate("CherryClicker", "RE-BIRTH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CherryClicker = QtWidgets.QMainWindow()
    ui = Ui_CherryClicker()
    ui.setupUi(CherryClicker)
    CherryClicker.show()
    sys.exit(app.exec())
