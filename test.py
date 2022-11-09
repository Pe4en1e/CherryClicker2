from PyQt5 import QtGui, QtCore, QtWidgets
import sys

class Ui_Launcher(object):
    def __init__(self, Launcher):
        super(Launcher, self).__init__
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher(Launcher)
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

