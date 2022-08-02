import sys
from PyQt5 import  QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector

count = 0
prioritycount = 0
queue = []
onlyInt = QIntValidator()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("Login.ui", self)
        self.button_login.clicked.connect(self.loginfunction)
        self.button_register.clicked.connect(self.gotoregister)

    def loginfunction(self):
        global username

        username = self.entry_username.text()
        password = self.entry_password.text()

        if username == "admin" and password == 'admin':
            QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Admin")
            self.gotoadmin()
        elif username == 'faculty' and password == 'faculty':
            QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Faculty")
            self.gotofaculty()
        elif username == 'student' and password == 'student':
            QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Student")
            self.gotostudentmenu()
        else:
            QtWidgets.QMessageBox.information(self, "Error", "Please try again")


    def gotoregister(self):
        createacc = RegisterForm()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotostudentmenu(self):
        sm = StudentMenu()
        widget.addWidget(sm)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        sm.User.setText(username)

    def gotoadmin(self):
        ad = AdminMenu()
        widget.addWidget(ad)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        ad.adminlabel.setText(username)

    def gotofaculty(self):
        fa = FacultyMenu()
        widget.addWidget(fa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        fa.User.setText(username)

class RegisterForm(QDialog):
    def __init__(self):
        super(RegisterForm, self).__init__()
        loadUi("RegisterForm.ui", self)
        self.button_createaccount.clicked.connect(self.createaccountfunction)
        self.button_return_reg.clicked.connect(self.returnfunction)
        self.entry_contactnumber.setValidator(onlyInt)
        self.entry_idnumber.setValidator(onlyInt)

    def createaccountfunction(self):
        firstname = self.entry_firstname.text()
        lastname = self.entry_lastname.text()
        username = self.entry_username.text()
        password = self.entry_password.text()
        repassword = self.entry_confirmpassword.text()
        idnumber = self.entry_idnumber.text()
        email = self.entry_emailaddress.text()
        phonenumber = self.entry_contactnumber.text()
        gender = 0
        department = str(self.combobox_department.currentText())
        if self.male_Button.isChecked():
            gender = 'Male'
        elif self.female_Button.isChecked():
            gender = 'Female'

        if password == repassword and password != '' and repassword != '':
            QtWidgets.QMessageBox.information(self, "Success", "You have created an Account")
        else:
            QtWidgets.QMessageBox.information(self, "Error", "Passwords do not match")


        #mycursor.execute("INSERT INTO students (idnumber, firstname, lastname, contactnumber, email, gender, department, username, password, confirmpassword) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #(idnumber, firstname, lastname, phonenumber, email, gender, department, username, password, repassword))


        #mydb.commit()


        print(firstname)
        print(lastname)
        print(phonenumber)
        print(idnumber)
        print(email)
        print(gender)
        print(department)
        print(username)
        print(password)
        print(repassword)

    def returnfunction(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class StudentMenu(QDialog):
    def __init__(self):
        super(StudentMenu, self).__init__()
        loadUi("StudentMenu.ui", self)
        self.SetAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.SetAppointment))
        self.UpdateAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.UpdateAppointment))
        self.MyAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.MyAppointment))
        self.HomeButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.HomePage))
        self.button_logout.clicked.connect(self.logoutfuncton)
        self.GetPriorityNumberButton.clicked.connect(self.getprionumber)
        self.lineEdit_2.setValidator(onlyInt)
        self.SubmitButton.clicked.connect(self.getappointment)

    def logoutfuncton(self):
        login = Login()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to Logout?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def getprionumber(self):
        global queue
        global prioritycount
        global count
        count += 1

        if prioritycount < 1:
            self.PriorityNumber.setText(str(count).zfill(3))
            prioritycount += 1
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Only 1 Priority Number per User")

        queue.append(count)

    def getappointment(self):
        print("1")


class AdminMenu(QDialog):
    def __init__(self):
        super(AdminMenu, self).__init__()
        loadUi("AdminMenu.ui", self)
        self.button_logout.clicked.connect(self.logoutfuncton)
        self.button_home.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.HomeAdmin))
        self.button_studentacc.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.StudentAccountst))
        self.button_facultyacc.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.FacultyAccounts))
        self.button_logbook.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.LogBook))
        self.button_appointmentlogs.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.AppointmentLogs))
        self.button_registerfaculty.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.RegisterFaculty))
        self.entry_contactnumber.setValidator(onlyInt)
        self.entry_idnumber.setValidator(onlyInt)

    def logoutfuncton(self):
        login = Login()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to Logout?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class FacultyMenu(QDialog):
    def __init__(self):
        super(FacultyMenu, self).__init__()
        loadUi("FacultyMenu.ui", self)
        self.HomeButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.HomePage))
        self.SetAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.ManageAppointment))
        self.UpdateAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.EditSchedule))
        self.MyAppointmentButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.ViewAppointments))
        self.button_logout.clicked.connect(self.logoutfuncton)

    def logoutfuncton(self):
        login = Login()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to Logout?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class Database:
    def __init__(self):
        pass

    def connect(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'cc15'
        )
        self.mycursor = self.mydb.cursor()

    def akobahala(self):
        self.awtsu()
        db = "SELECT firstname, lastname FROM students WHERE (username = 'raynhard' and password = 1)"
        self.mycursor.execute(db)
        result = self.mycursor.fetchone()
        self.mycursor.close()
        self.mydb.close()
        return result


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(681)
widget.setFixedHeight(714)
widget.show()
app.exec_()

temp = Pangalan()
awts = list(temp.akobahala())
print(awts[0], awts[1])