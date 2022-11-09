from PyQt6 import QtCore, QtGui, QtWidgets
import launcher


class Clicks():
    total=0
    click_cost=1


class Ui_CherryClicker(object):
    def setupUi(self, CherryClicker):
        CherryClicker.setObjectName("CherryClicker")
        CherryClicker.resize(1920, 1080)
        CherryClicker.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(CherryClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn.setGeometry(QtCore.QRect(560, 610, 220, 90))
        self.main_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_btn.setObjectName("main_btn")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(170, 60, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        self.score.setFont(font)
        self.score.setObjectName("score")
        CherryClicker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CherryClicker)
        self.statusbar.setObjectName("statusbar")
        CherryClicker.setStatusBar(self.statusbar)

        self.retranslateUi(CherryClicker)
        QtCore.QMetaObject.connectSlotsByName(CherryClicker)


    def retranslateUi(self, CherryClicker):
        _translate = QtCore.QCoreApplication.translate
        CherryClicker.setWindowTitle(_translate("CherryClicker", "CherryClicker"))
        self.main_btn.setText(_translate("CherryClicker", "PushButton"))
        self.score.setText(_translate("CherryClicker", str(Clicks.total)))
        self.main_btn.clicked.connect(self.addscore)
    

    def addscore(self):
        Clicks.total += Clicks.click_cost
        self.score.setText(str(Clicks.total))


def Start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_CherryClicker()
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec_())
    


if __name__ == "__main__":
    Start()
