# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(640, 320)
        self.centralwidget = QtWidgets.QWidget(Launcher)
        self.centralwidget.setObjectName("centralwidget")
        self.newgame_btn = QtWidgets.QPushButton(self.centralwidget)
        self.newgame_btn.setGeometry(QtCore.QRect(340, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newgame_btn.setFont(font)
        self.newgame_btn.setObjectName("newgame_btn")
        self.continue_btn = QtWidgets.QPushButton(self.centralwidget)
        self.continue_btn.setGeometry(QtCore.QRect(340, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continue_btn.setFont(font)
        self.continue_btn.setObjectName("continue_btn")
        Launcher.setCentralWidget(self.centralwidget)

        self.retranslateUi(Launcher)
        QtCore.QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QtCore.QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.newgame_btn.setText(_translate("Launcher", "Новая игра"))
        self.continue_btn.setText(_translate("Launcher", "Продолжить "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher()
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec())
