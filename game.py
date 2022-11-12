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
        CherryClicker.resize(1920, 1080)
        CherryClicker.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Ukrainian, QtCore.QLocale.Country.Ukraine))
        self.centralwidget = QtWidgets.QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QtCore.QRect(160, 540, 340, 320))
        self.main_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet("border-image:url(images/cherry.png)")
        self.main_btn.setText("")
        self.main_btn.setObjectName("main_btn")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(80, 180, 580, 80))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(255, 255, 255)")
        self.score.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score.setObjectName("score")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/game_bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(1620, 70, 240, 70))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit_btn.setStyleSheet("border-image:url(images/exit_btn.png)")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.label.raise_()
        self.score.raise_()
        self.main_btn.raise_()
        self.exit_btn.raise_()
        CherryClicker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CherryClicker)
        self.statusbar.setObjectName("statusbar")
        CherryClicker.setStatusBar(self.statusbar)

        self.retranslateUi(CherryClicker)
        QtCore.QMetaObject.connectSlotsByName(CherryClicker)

    def retranslateUi(self, CherryClicker):
        _translate = QtCore.QCoreApplication.translate
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.score.setText(_translate("CherryClicker", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CherryClicker = QtWidgets.QMainWindow()
    ui = Ui_CherryClicker()
    ui.setupUi(CherryClicker)
    CherryClicker.show()
    sys.exit(app.exec())
