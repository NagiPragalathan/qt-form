from PyQt5 import QtWidgets, QtCore
from form import Ui_Form
import sys
import sqlite3, bcrypt

class LoginApp(QtWidgets.QWidget, Ui_Form):
    def changeForm(self):
        if self.side.isChecked():
            print("clicked")
            self.log.hide()
            self.reg.show()
            self.side.setText("<")
        else:
            self.reg.show()
            self.log.hide()
            self.side.setText(">")
    def signin(self):
        def set_id():
            count = 0
            quary = conn.execute(f"""select * from COMPANY""")
            for i in quary:
                count = count + 1
            return count+1
        conn = sqlite3.connect('test.sqlite')
        name = self.lineEdit_13.text()
        email = self.lineEdit_12.text()
        password = self.lineEdit_15.text()
        con_password = self.lineEdit_16.text()
        org = self.lineEdit_17.text()
        if(password == con_password):
            try:
                bytes = password.encode("utf-8")
                salt = bcrypt.gensalt()
                hash = bcrypt.hashpw(bytes, salt)
                conn.execute(f"""INSERT INTO COMPANY (ID,NAME,EMAIL,PASS,ORG) VALUES (?,?,?,?,?)""",(set_id(),name,email,hash,org))
                conn.commit()
                conn.close()
            except:
                print("email already exist....")
        else:
            print("did not same")
    def login(self):
        worng = True
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        conn = sqlite3.connect('test.sqlite')
        quary = conn.execute(f"""select * from COMPANY""")
        for i in quary:
             if( email == i[2]):
                if(bcrypt.checkpw(password.encode('utf-8'),i[3])):
                    print("user name and passwords are correct...!")
                    worng = False
                    break
        if worng:
            print("check your user name (or) password")

        
        
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.logbtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.regbtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.reg.hide()
        self.side.clicked.connect(self.changeForm)
        self.regbtn.clicked.connect(self.signin)
        self.logbtn.clicked.connect(self.login)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())
