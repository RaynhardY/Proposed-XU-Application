# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(28, 42, 57);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1390, 750, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.entry_username = QtWidgets.QLineEdit(Form)
        self.entry_username.setGeometry(QtCore.QRect(1380, 590, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entry_username.setFont(font)
        self.entry_username.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(60, 74, 89);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding: 0px 20px 0px 20px;\n"
"    background-color: rgb(44, 58, 73);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(188, 202, 217);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(156, 170, 185);\n"
"}")
        self.entry_username.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_username.setObjectName("entry_username")
        self.Login_Label = QtWidgets.QLabel(Form)
        self.Login_Label.setGeometry(QtCore.QRect(1440, 470, 241, 71))
        self.Login_Label.setStyleSheet("color:#fff;\n"
"color: rgb(123, 138, 149);")
        self.Login_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Label.setObjectName("Login_Label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1590, 790, 141, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(60, 74, 89);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding: 0px 20px 0px 20px;\n"
"    background-color: rgb(44, 58, 73);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(188, 202, 217);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.entry_password = QtWidgets.QLineEdit(Form)
        self.entry_password.setGeometry(QtCore.QRect(1380, 680, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entry_password.setFont(font)
        self.entry_password.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(60, 74, 89);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding: 0px 20px 0px 20px;\n"
"    background-color: rgb(44, 58, 73);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(188, 202, 217);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(156, 170, 185);\n"
"}")
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_password.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_password.setObjectName("entry_password")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1380, 790, 191, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(60, 74, 89);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding: 0px 20px 0px 20px;\n"
"    background-color: rgb(44, 58, 73);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(188, 202, 217);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1151, 1081))
        self.widget.setStyleSheet("background-color: rgb(59, 69, 84);")
        self.widget.setObjectName("widget")
        self.Login_Label_2 = QtWidgets.QLabel(self.widget)
        self.Login_Label_2.setGeometry(QtCore.QRect(360, 190, 461, 71))
        self.Login_Label_2.setStyleSheet("color:#fff;\n"
"color: rgb(123, 138, 149);")
        self.Login_Label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Label_2.setObjectName("Login_Label_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(190, 500, 291, 171))
        self.frame.setStyleSheet("background-color: rgb(44, 58, 73);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login_Label_3 = QtWidgets.QLabel(self.widget)
        self.Login_Label_3.setGeometry(QtCore.QRect(240, 420, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Label_3.setFont(font)
        self.Login_Label_3.setStyleSheet("color:#fff;\n"
"color: rgb(123, 138, 149);")
        self.Login_Label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Label_3.setObjectName("Login_Label_3")
        self.Login_Label_4 = QtWidgets.QLabel(self.widget)
        self.Login_Label_4.setGeometry(QtCore.QRect(700, 420, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Label_4.setFont(font)
        self.Login_Label_4.setStyleSheet("color:#fff;\n"
"color: rgb(123, 138, 149);")
        self.Login_Label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Label_4.setObjectName("Login_Label_4")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(650, 500, 291, 171))
        self.frame_2.setStyleSheet("background-color: rgb(44, 58, 73);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1320, 20, 481, 561))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("xu-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1800, 1050, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.entry_username.raise_()
        self.pushButton.raise_()
        self.entry_password.raise_()
        self.pushButton_3.raise_()
        self.widget.raise_()
        self.label_2.raise_()
        self.Login_Label.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Need Account?"))
        self.entry_username.setPlaceholderText(_translate("Form", "Username"))
        self.Login_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Login</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.entry_password.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton_3.setText(_translate("Form", "Register"))
        self.Login_Label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">NOW SERVING</span></p><p><br/></p></body></html>"))
        self.Login_Label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Window 1</span></p></body></html>"))
        self.Login_Label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Window 2</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "?? Copyright."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
