from PyQt6 import QtCore, QtGui, QtWidgets
import game


class Ui_Launcher(object):


    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(640, 320)
        Launcher.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(Launcher)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(340, 130, 141, 31))
        self.start_btn.setObjectName("start_btn")
        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Launcher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Launcher)
        self.statusbar.setObjectName("statusbar")
        Launcher.setStatusBar(self.statusbar)

        self.retranslateUi(Launcher)
        QtCore.QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QtCore.QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.start_btn.setText(_translate("Launcher", "PushButton"))
        self.start_btn.clicked.connect(self.startgame)


    def startgame(self):
        game.Start()
        

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher()
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec_())

def exitlauncher():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher()
    ui.setupUi(Launcher)
    Launcher.hide
    sys.exit(app.exec_())

