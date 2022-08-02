import sys, database as db
import mysql.connector
from PyQt5 import  QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidgetItem

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "cc15")
mycursor = mydb.cursor()
student_prioritycount = 0
guest_prioritycount = 0
guest_enrollment_count = 0
current_account = {"id":"", "name":""}

# ///// Login UI /////
class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("UI\Login\Login.ui", self)
        self.guest_teacher_list()
        self.button_login.clicked.connect(self.loginfunction)
        self.button_register.clicked.connect(self.gotoregister)
        self.student_login.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.goto_guest.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.Submit_pushButton_2.clicked.connect(self.guest_generate_queue)
        self.Submit_pushButton.clicked.connect(self.sga)
        self.getdb = db.database()
        self.sup()

    def sup(self):
        statement = "SELECT guest, student FROM cq"
        qnum = db.database().select_all(statement)[0]
        self.guest_label.setText(qnum[0])
        self.student_label.setText(qnum[1])
        
    def loginfunction(self):
        global username
        global password


        username = self.entry_username.text()
        password = self.entry_password.text()

        account = self.getdb.selectone("SELECT school_id, type FROM user_account WHERE school_id = %s AND password = %s", (username,password))

        if (account != None):
            current_account["id"] = username
            if account[1] == "student":
                QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Student")
                self.gotostudentmenu()
            elif account[1] == "faculty":
                QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Faculty")
                self.gotofaculty()
        elif username == "admin" and password == "admin":
            QtWidgets.QMessageBox.information(self, "Success", "You have logged in as Admin")
            self.gotoadmin()
        else:
            QtWidgets.QMessageBox.information(self, "Error", "Account does not exist")

    def gotoregister(self):
        createacc = RegisterForm()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.showNormal()

    def gotostudentmenu(self):
        sm = StudentMenu()
        widget.addWidget(sm)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.showMaximized()

    def gotoadmin(self):
        ad = AdminMenu()
        widget.addWidget(ad)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.showMaximized()

    def gotofaculty(self):
        fa = FacultyMenu()
        widget.addWidget(fa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.showMaximized()

    def guest_teacher_list(self):
        sql_statement = "SELECT fname, lname, department FROM user_account WHERE type = 'faculty'"
        name_list = db.database().select_all(sql_statement)
        for name in name_list:
            self.entry_combobox.addItem(name[0] + " " + name[1])
        
    def guest_generate_queue(self):
        statement = "SELECT number FROM guest_queue"
        prionum = db.database().select_all(statement)[0][0]
        prionum = self.guest_label_2.setText(prionum)
    
    def sga(self, prionum):
        fname = self.entry_firstname.text()
        lname = self.entry_lastname.text()
        cnum = self.entry_contactnumber.text()
        rson = self.entry_combobox_2.currentText()
        faculty = self.entry_combobox.currentText()
        prionum = self.guest_label_2.text()

        if prionum:
            statement = "INSERT INTO guest_appointment (fname, lname, contact_number, faculty, reason, queue_number) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (fname, lname, cnum, faculty, rson, prionum)
            db.database().save(statement, data)

            statement = "UPDATE guest_queue SET number = %s"
            data = (str(int(prionum) + 1),)
            db.database().save(statement, data)
            QtWidgets.QMessageBox.information(self, "Congrats", "You have successfully created an Appointment")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please get a Priority Number")


# ///// Register UI /////
class RegisterForm(QDialog):
    def __init__(self):
        super(RegisterForm, self).__init__()
        loadUi("UI\Register\RegisterForm.ui", self)
        self.button_createaccount.clicked.connect(self.createaccountfunction)
        self.button_return_reg.clicked.connect(self.returnfunction)

    def create_success(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("You have created an Account!")
        msgBox.setWindowTitle("Success!")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.returnfunction()

    def check_password(self):
        if self.entry_password.text() == self.entry_confirmpassword.text():
            return True
        else:
            return False


    def createaccountfunction(self):
        if self.entry_password.text() == self.entry_confirmpassword.text():
            statement = "INSERT INTO user_account (school_id, fname, lname, department, password, type) VALUES (%s, %s, %s, %s, %s, 'student')" 
            data = (self.entry_username.text(), self.entry_firstname.text(), self.entry_lastname.text(), self.combobox_department.currentText(), self.entry_password.text())
            db.database().save(statement, data)
            self.create_success()
        else:
            QtWidgets.QMessageBox.information(self, "Error", "Passwords do not match")

    def returnfunction(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.showMaximized()

# ///// Student UI /////
class StudentMenu(QDialog):
    def __init__(self):
        super(StudentMenu, self).__init__()
        loadUi("UI\Student\StudentMenu.ui", self)
        self.SetAppointmentButton.clicked.connect(self.asup)
        self.MyAppointmentButton.clicked.connect(self.set_my_appointment)
        self.HomeButton.clicked.connect(self.home_page)
        self.button_logout.clicked.connect(self.logoutfuncton)
        self.generate_priority.clicked.connect(self.generatequeue)
        self.SubmitButton.clicked.connect(self.getappointment)
        self.student_teacher_list()
        self.home_page()

    def generatequeue(self):
        statement = "SELECT number FROM student_queue"
        qnum = db.database().select_all(statement)[0][0]
        self.queue_label.setText(qnum)
        
        statement = "UPDATE student_queue SET number = %s"
        data = (str(int(qnum) + 1),)
        db.database().save(statement, data)
        
    def asup(self):
        self.Pages_widgets.setCurrentWidget(self.SetAppointment)
        self.queue_label.setText("")

        statement = "SELECT guest, student FROM cq"
        qnum = db.database().select_all(statement)[0]
        self.guest_label.setText(qnum[0])
        self.student_label.setText(qnum[1])
    
    def home_page(self):
        self.Pages_widgets.setCurrentWidget(self.HomePage)
        statement = "SELECT school_id, fname, lname, department FROM user_account WHERE school_id = %s"
        data = (current_account["id"],)
        account = db.database().selectone(statement, data)
        print(current_account["id"])

        self.label_idnumber.setText(account[0])
        self.label_fname.setText(account[1])
        self.label_lname.setText(account[2])
        self.User.setText(account[1] + " " + account[2])
        self.label_department.setText(account[3])
        self.now_serving()

    def now_serving(self):
        statement = "SELECT guest, student FROM cq"
        qnum = db.database().select_all(statement)[0]
        self.guest_label_2.setText(qnum[0])
        self.student_label_2.setText(qnum[1])
    
    def set_my_appointment(self):
        self.Pages_widgets.setCurrentWidget(self.MyAppointment)
        self.tableWidget_4.verticalHeader().hide()

        self.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        
        statement = "SELECT student_id, queue_number, purpose, teacher, date, status FROM student_appointment WHERE student_id = '" + current_account["id"] + "'"
        my_appointments = db.database().select_all(statement)

        self.tableWidget_4.setRowCount(0)

        count = 0
        for data in my_appointments:
            self.tableWidget_4.insertRow(count)
            
            self.tableWidget_4.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget_4.setItem(count, 1, QTableWidgetItem(str(data[1])))
            self.tableWidget_4.setItem(count, 2, QTableWidgetItem(str(data[2])))
            self.tableWidget_4.setItem(count, 3, QTableWidgetItem(str(data[3])))
            self.tableWidget_4.setItem(count, 4, QTableWidgetItem(str(data[4])))
            self.tableWidget_4.setItem(count, 5, QTableWidgetItem(str(data[5])))

            count += 1


    def student_teacher_list(self):
        sql_statement = "SELECT fname, lname, department FROM user_account WHERE type = 'faculty'"
        name_list = db.database().select_all(sql_statement)
        for name in name_list:
            self.teacher_comboBox.addItem(name[0] + " " + name[1])
        
    def getappointment(self):
        faculty = str(self.teacher_comboBox.currentText())
        purpose = str(self.appoint_comboBox.currentText())
        priority = self.entry_prioritynumber.text()
        date = self.calendarWidget.selectedDate().toString()

        if priority:
            try:
                QtWidgets.QMessageBox.information(self, "Congrats", "You have successfully created an Appointment")
                result_statement = "INSERT INTO student_appointment (student_id, queue_number, purpose, teacher, date) VALUES (%s, %s, %s, %s, %s)"
                result_date = (current_account["id"], priority, purpose, faculty, date)
                db.database().save(result_statement, result_date)
                self.teacher_comboBox.setCurrentIndex(0)
                self.appoint_comboBox.setCurrentIndex(0)
                self.entry_prioritynumber.setText("")
            except:
                QtWidgets.QMessageBox.warning(self, "Error", "Please recheck Priority Number")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please put a Priority Number")

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

# ///// Admin UI /////
class AdminMenu(QDialog):
    def __init__(self):
        super(AdminMenu, self).__init__()
        loadUi("UI\Admin\AdminMenu.ui", self)
        # # self.entry_contactnumber.setValidator(onlyInt)
        # # self.entry_idnumber.setValidator(onlyInt)
        # self.button_guest_appointment.clicked.connect(self.appointments_guest)
        self.student_account_display()
        self.button_student_appointment.clicked.connect(self.student_account_display)
        self.button_guest_appointment.clicked.connect(self.guest_account_display)
        self.button_studentacc.clicked.connect(self.sad)
        self.button_facultyacc.clicked.connect(self.fad)
        self.button_registerfaculty.clicked.connect(lambda: self.Pages_widgets_admin.setCurrentWidget(self.RegisterFaculty))
        self.button_logout.clicked.connect(self.logoutfuncton)
        self.button_createaccount.clicked.connect(self.createaccountfunction)
        # self.button_appointmentlogs.clicked.connect(self.set_appointment_log)
        self.adminlabel.setText("Admin nga bogok")
        # self.set_appointment_log()

    def student_account_display(self):
        self.Pages_widgets_admin.setCurrentWidget(self.Student_Appointments)
        self.tableWidget_3.verticalHeader().hide()

        self.tableWidget_3.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        
        # statement = "SELECT student_id, queue_number, purpose, teacher, date, status FROM student_appointment WHERE student_id = '" + current_account["id"] + "'"
        statement = "SELECT * FROM student_appointment"
        my_appointments = db.database().select_all(statement)

        self.tableWidget_3.setRowCount(0)

        count = 0
        for data in my_appointments:
            self.tableWidget_3.insertRow(count)
            
            self.tableWidget_3.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget_3.setItem(count, 1, QTableWidgetItem(str(data[1])))
            self.tableWidget_3.setItem(count, 2, QTableWidgetItem(str(data[2])))
            self.tableWidget_3.setItem(count, 3, QTableWidgetItem(str(data[3])))
            self.tableWidget_3.setItem(count, 4, QTableWidgetItem(str(data[4])))
            self.tableWidget_3.setItem(count, 5, QTableWidgetItem(str(data[5])))
            self.tableWidget_3.setItem(count, 6, QTableWidgetItem(str(data[6])))

            count += 1

    def guest_account_display(self):
        self.Pages_widgets_admin.setCurrentWidget(self.Guest_Appointments)
        self.tableWidget_6.verticalHeader().hide()

        self.tableWidget_6.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        
        # statement = "SELECT student_id, queue_number, purpose, teacher, date, status FROM student_appointment WHERE student_id = '" + current_account["id"] + "'"
        statement = "SELECT * FROM guest_appointment"
        my_appointments = db.database().select_all(statement)

        self.tableWidget_6.setRowCount(0)

        count = 0
        for data in my_appointments:
            self.tableWidget_6.insertRow(count)
            
            self.tableWidget_6.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget_6.setItem(count, 1, QTableWidgetItem(str(data[1])))
            self.tableWidget_6.setItem(count, 2, QTableWidgetItem(str(data[2])))
            self.tableWidget_6.setItem(count, 3, QTableWidgetItem(str(data[3])))
            self.tableWidget_6.setItem(count, 4, QTableWidgetItem(str(data[4])))
            self.tableWidget_6.setItem(count, 5, QTableWidgetItem(str(data[5])))
            self.tableWidget_6.setItem(count, 6, QTableWidgetItem(str(data[6])))
            self.tableWidget_6.setItem(count, 7, QTableWidgetItem(str(data[7])))

            count += 1

    def sad(self):
        self.Pages_widgets_admin.setCurrentWidget(self.StudentAccounts)
        self.tableWidget.verticalHeader().hide()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        statement = "SELECT * FROM user_account WHERE type = 'student'"
        mn = db.database().select_all(statement)

        self.tableWidget.setRowCount(0)
        
        count = 0
        for data in mn:
            self.tableWidget.insertRow(count)
            
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(data[1])))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(data[2])))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(data[3])))
            self.tableWidget.setItem(count, 4, QTableWidgetItem(str(data[4])))
            self.tableWidget.setItem(count, 5, QTableWidgetItem(str(data[5])))

            count += 1

    def fad(self):
        self.Pages_widgets_admin.setCurrentWidget(self.FacultyAccounts)
        self.facultyWidget.verticalHeader().hide()

        self.facultyWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.facultyWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.facultyWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.facultyWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.facultyWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.facultyWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        
        statement = "SELECT * FROM user_account WHERE type = 'faculty'"
        mn = db.database().select_all(statement)

        self.facultyWidget.setRowCount(0)
        
        count = 0
        for data in mn:
            self.facultyWidget.insertRow(count)
            
            self.facultyWidget.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.facultyWidget.setItem(count, 1, QTableWidgetItem(str(data[1])))
            self.facultyWidget.setItem(count, 2, QTableWidgetItem(str(data[2])))
            self.facultyWidget.setItem(count, 3, QTableWidgetItem(str(data[3])))
            self.facultyWidget.setItem(count, 4, QTableWidgetItem(str(data[4])))
            self.facultyWidget.setItem(count, 5, QTableWidgetItem(str(data[5])))

            count += 1

    def returnfunction(self):
        self.student_account_display()

    def create_success(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("You have created an Account!")
        msgBox.setWindowTitle("Success!")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.returnfunction()

    def createaccountfunction(self):
        statement = "INSERT INTO user_account (school_id, fname, lname, department, password, type) VALUES (%s, %s, %s, %s, %s, 'faculty')"
        data = (self.entry_username.text(), self.entry_firstname.text(), self.entry_lastname.text(), self.combobox_department.currentText(), self.entry_password.text())
        db.database().save(statement,data)
        self.create_success()
        # QtWidgets.QMessageBox.information(self, "Success", "You have created an Account")

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

# ///// Faculty UI /////
class FacultyMenu(QDialog):
    def __init__(self):
        super(FacultyMenu, self).__init__()
        loadUi("UI\Faculty\FacultyMenu.ui", self)
        self.HomeButton.clicked.connect(lambda: self.Pages_widgets.setCurrentWidget(self.HomePage))
        self.StudentAppointmentButton.clicked.connect(self.sas)
        self.GuestAppointmentButton.clicked.connect(self.sag)
        self.button_logout.clicked.connect(self.logoutfuncton)
        self.home_page()
    
    def sag(self):
        self.Pages_widgets.setCurrentWidget(self.GuestAppointments)
        self.tableWidget_4.verticalHeader().hide()

        self.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        

        self.sags()
    
    def sags(self):
        statement = "SELECT fname, lname FROM user_account WHERE school_id = '"+current_account["id"]+"'"
        mn = db.database().select_all(statement)[0]
        mfn = mn[0] + " " + mn[1]
        statement = "SELECT id, fname, lname, queue_number, reason, faculty FROM guest_appointment WHERE faculty = '"+mfn+"'"
        listahan = db.database().select_all(statement)

        self.tableWidget_4.setRowCount(0)

        count = 0
        for data in listahan:
            name = data[1] + " " + data[2]

            self.tableWidget_4.insertRow(count)
            self.tableWidget_4.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget_4.setItem(count, 1, QTableWidgetItem(name))
            self.tableWidget_4.setItem(count, 2, QTableWidgetItem(str(data[3])))
            self.tableWidget_4.setItem(count, 3, QTableWidgetItem(str(data[4])))
            self.tableWidget_4.setItem(count, 4, QTableWidgetItem(str(data[5])))

            count += 1
    
    def sas(self):
        self.Pages_widgets.setCurrentWidget(self.StudentAppointments)
        self.tableWidget.verticalHeader().hide()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

        self.sals()
    
    def sals(self):
        statement = "SELECT fname, lname FROM user_account WHERE school_id = '"+current_account["id"]+"'"
        mn = db.database().select_all(statement)[0]
        mfn = mn[0] + " " + mn[1]
        statement = "SELECT a.id, fname, lname, school_id, queue_number, purpose, teacher, date FROM student_appointment a LEFT JOIN user_account aa ON student_id = school_id WHERE teacher = '"+mfn+"'"
        listahan = db.database().select_all(statement)

        self.tableWidget.setRowCount(0)

        count = 0
        for data in listahan:
            name = data[1] + " " + data[2]

            self.tableWidget.insertRow(count)
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(data[3])))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(data[4])))
            self.tableWidget.setItem(count, 4, QTableWidgetItem(str(data[5])))
            self.tableWidget.setItem(count, 5, QTableWidgetItem(str(data[6])))
            self.tableWidget.setItem(count, 6, QTableWidgetItem(str(data[7])))

            count += 1

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

    def home_page(self):
            statement = "SELECT school_id, fname, lname, department FROM user_account WHERE school_id = %s"
            data = (current_account["id"],)
            account = db.database().selectone(statement, data)
            self.label_fname.setText(account[1])
            self.label_lname.setText(account[2])
            # self.User.setText(account[1] + " " + account[2])
            self.label_department.setText(account[3])
            self.label_idnumber.setText(account[0])
            
            self.reset_prio.clicked.connect(self.rq)
            self.guest_skip_queue.clicked.connect(self.nqg)
            self.student_skip_queue.clicked.connect(self.nqs)
            self.dq()

    def guest_set_cs(self):
        statement = "SELECT guest FROM cq"
        qnum = db.database().select_all(statement)[0]
        self.guest_label_2.setText(qnum)

    def student_cet_cs(self):
        statement = "SELECT sudent FROM cq"
        qnum = db.database().select_all(statement)[0]
        self.student_label_2.setText(qnum)
    
    def nqg(self):
        # statement = "SELECT guest FROM cq"
        # qnum = db.database().select_all(statement)[0][0]
        # self.guest_label_2.setText(qnum)
        
        # statement = "UPDATE student_queue SET number = %s"
        # # data = (str(int(qnum) + 1),)
        # data = (str(int(qnum) + 1),)
        # db.database().save(statement, data)
        # statement = "SELECT fname, lname FROM user_account WHERE school_id = '"+current_account["id"]+"'"
        self.guest_label_2.setText(str(int(self.guest_label_2.text()) + 1))

    def nqs(self):
        self.student_label_2.setText(str(int(self.student_label_2.text()) + 1))
        
    def dq(self):
        s = "SELECT guest, student FROM cq"
        l = db.database().select_all(s)[0]
        self.guest_label_2.setText(l[0])
        self.student_label_2.setText(l[1])   

    def rq(self):
        statement = "UPDATE guest_queue SET number = %s"
        data = ("1",)
        db.database().save(statement, data)

        statement = "UPDATE student_queue SET number = %s"
        data = ("1",)
        db.database().save(statement, data)

        statement = "UPDATE guest_appointment SET status = %s"
        data = ("pending",)
        db.database().save(statement, data)

        statement = "UPDATE student_appointment SET status = %s"
        data = ("pending",)
        db.database().save(statement, data)

        statement = "UPDATE cq SET guest = %s, student = %s"
        data = ("0", "0")
        db.database().save(statement, data)

        self.dq()

# ///// Main Window /////
app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Computer Studies Queueing System")
widget.showMaximized()
widget.show()
app.exec_()