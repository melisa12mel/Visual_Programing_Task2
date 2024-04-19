from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 423)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 471, 371))
        self.widget.setStyleSheet("background-color: rgb(255,192,203);\n"
"border-bottom-right-radius: 50px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 351))
        self.label.setStyleSheet("border-image: url(:/image/Melisa Putri Dwi Anggari_2105176042/image/flower.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(250, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,81,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,81,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(250, 210, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,81,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.528409 rgba(195, 0, 60, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,125);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(250, 280, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255,255,255,255);")
        self.label_6.setObjectName("label_6")

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Log in"))
        self.textEdit.setPlaceholderText(_translate("Form", "UserName"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.textEdit_3.setPlaceholderText(_translate("Form", "Email"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_3.setText(_translate("Form", "Forgot you username or password?"))
        self.label_6.setText(_translate("Form", "Developed by Melisa Putri Dwi Anggari"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
