import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    credentials = []
    def login_pressed(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        Ui_MainWindow.credentials += [email,password]        
        # print(email)
        # print(password)
        QtWidgets.QApplication.quit()


        
    # def closeEvent(self,event):
    #     event.accept()


    # def cancel_pressed(self):
    #     MainWindow.close()
    #     print("closed")

    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 70, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 110, 70, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(102)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AnjaliOldLipi")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(160, 150, 131, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 300, 89, 25))
        self.pushButton.setObjectName("Login")

        self.pushButton.clicked.connect(self.login_pressed)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 180, 211, 25))
        self.lineEdit.setObjectName("Email")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 220, 211, 25))
        self.lineEdit_2.setObjectName("Password")

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 300, 91, 25))
        self.pushButton_2.setObjectName("Cancel")

        self.pushButton_2.clicked.connect(QtWidgets.QApplication.quit)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 22))
        self.menubar.setObjectName("menubar")
        self.menuGmail_Login = QtWidgets.QMenu(self.menubar)
        self.menuGmail_Login.setObjectName("menuGmail_Login")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGmail_Login.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Gmail"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.menuGmail_Login.setTitle(_translate("MainWindow", "Gmail Login"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
    #sys.exit(app.exec_())
    
else:
    def gui():
        global MainWindow
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
