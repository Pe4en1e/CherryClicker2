from PyQt6 import QtCore, QtGui, QtWidgets
from client import auth


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(640, 320)
        Launcher.setMinimumSize(QtCore.QSize(640, 320))
        Launcher.setMaximumSize(QtCore.QSize(640, 320))
        Launcher.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Launcher.setWindowIcon(icon)
        Launcher.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Ukrainian, QtCore.QLocale.Country.Ukraine))
        self.centralwidget = QtWidgets.QWidget(Launcher)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("SPRK_default_preset_name_custom – 1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.login_field = QtWidgets.QLineEdit(self.centralwidget)
        self.login_field.setGeometry(QtCore.QRect(19, 170, 279, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_field.setFont(font)
        self.login_field.setStyleSheet("border-radius: 5px; border: 2px solid #7F5AF0; color: #ffffff; background-color: #16161A")
        self.login_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_field.setObjectName("login_field")
        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(19, 218, 279, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_field.setFont(font)
        self.password_field.setStyleSheet("border-radius: 5px; border: 2px solid #7F5AF0; color: #ffffff; background-color: #16161A")
        self.password_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_field.setObjectName("password_field")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(312, 170, 161, 33))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet("border-radius: 0px; border: 0px solid white; background-image: url(btn_login.png)")
        self.login_btn.setText("")
        self.login_btn.setObjectName("login_btn")
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(312, 218, 161, 33))
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reg_btn.setStyleSheet("border-radius: 0px; border: 0px solid white; background-image: url(btn_reg.png)")
        self.reg_btn.setText("")
        self.reg_btn.setObjectName("reg_btn")
        self.result_txt = QtWidgets.QLabel(self.centralwidget)
        self.result_txt.setGeometry(QtCore.QRect(20, 260, 279, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_txt.setFont(font)
        self.result_txt.setStyleSheet("color: #ffffff")
        self.result_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_txt.setObjectName("result_txt")
        Launcher.setCentralWidget(self.centralwidget)
        self.reg_btn.clicked.connect(self.reg)
        self.login_btn.clicked.connect(self.login)

        self.retranslateUi(Launcher)
        QtCore.QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QtCore.QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.login_field.setPlaceholderText(_translate("Launcher", "Login..."))
        self.password_field.setPlaceholderText(_translate("Launcher", "Password..."))
        self.result_txt.setText(_translate("Launcher", ""))

    def reg(self):
        self.result_txt.setText(auth.reg(str(self.login_field.text()), str(self.password_field.text())))

    def login(self):
        self.result_txt.setText(auth.login(str(self.login_field.text()), str(self.password_field.text())))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher()
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec())
