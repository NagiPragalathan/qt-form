# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 565)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#pushButton, #pushButton_6, #pushButton_7{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover, #pushButton_6:hover, #pushButton_7:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed, #pushButton_6:pressed, #pushButton_7:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-21, 30, 341, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/3d-model-1024x722.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(70, 150, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(100, 170, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(90, 210, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")
        self.log = QtWidgets.QWidget(self.widget)
        self.log.setGeometry(QtCore.QRect(320, 60, 231, 391))
        self.log.setObjectName("log")
        self.label_4 = QtWidgets.QLabel(self.log)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.log)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 145, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.log)
        self.lineEdit.setGeometry(QtCore.QRect(15, 80, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.logbtn = QtWidgets.QPushButton(self.log)
        self.logbtn.setGeometry(QtCore.QRect(15, 225, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.logbtn.setFont(font)
        self.logbtn.setObjectName("logbtn")
        self.label_5 = QtWidgets.QLabel(self.log)
        self.label_5.setGeometry(QtCore.QRect(50, 290, 181, 21))
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);font-size:14px;")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.log)
        self.label_10.setGeometry(QtCore.QRect(40, 330, 161, 21))
        self.label_10.setStyleSheet("color:rgba(0, 0, 0, 210);font-size:13px;")
        self.label_10.setObjectName("label_10")
        self.side = QtWidgets.QPushButton(self.log)
        self.side.setGeometry(QtCore.QRect(180, 330, 30, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.side.setFont(font)
        self.side.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.side.setCheckable(True)
        self.side.setObjectName("side")
        self.reg = QtWidgets.QWidget(self.widget)
        self.reg.setGeometry(QtCore.QRect(340, 30, 220, 411))
        self.reg.setObjectName("reg")
        
        self.side_ = QtWidgets.QPushButton(self.reg)
        self.side_.setGeometry(QtCore.QRect(180, 330, 15, 80))
        self.side_.setFont(font)
        self.side_.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.side_.setCheckable(True)
        self.side_.setObjectName("side_")
        
        self.label_17 = QtWidgets.QLabel(self.reg)
        self.label_17.setGeometry(QtCore.QRect(30, 10, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_17.setObjectName("label_17")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.reg)
        self.lineEdit_12.setGeometry(QtCore.QRect(15, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.reg)
        self.lineEdit_13.setGeometry(QtCore.QRect(15, 60, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.regbtn = QtWidgets.QPushButton(self.reg)
        self.regbtn.setGeometry(QtCore.QRect(10, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.regbtn.setFont(font)
        self.regbtn.setObjectName("regbtn")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.reg)
        self.lineEdit_15.setGeometry(QtCore.QRect(15, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_15.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.reg)
        self.lineEdit_16.setGeometry(QtCore.QRect(15, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.reg)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 250, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_17.setText("")
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_18 = QtWidgets.QLabel(self.reg)
        self.label_18.setGeometry(QtCore.QRect(30, 370, 161, 21))
        self.label_18.setStyleSheet("color:rgba(0, 0, 0, 210);font-size:13px;")
        self.label_18.setObjectName("label_18")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Futaucon"))
        self.label_8.setText(_translate("Form", "3D Model Generation"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.logbtn.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot Password?"))
        self.label_10.setText(_translate("Form", "New User?, Register"))
        self.side.setText(_translate("Form", ">"))
        self.label_17.setText(_translate("Form", "Register"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "  Email Address"))
        self.lineEdit_13.setPlaceholderText(_translate("Form", "  First Name"))
        self.regbtn.setText(_translate("Form", "R e g i s t e r"))
        self.lineEdit_15.setPlaceholderText(_translate("Form", "  Password"))
        self.lineEdit_16.setPlaceholderText(_translate("Form", "  Confirm Password"))
        self.lineEdit_17.setPlaceholderText(_translate("Form", "  Organization"))
        self.label_18.setText(_translate("Form", "Already Registered?"))
        self.side_.setText(_translate("Form", "<"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())