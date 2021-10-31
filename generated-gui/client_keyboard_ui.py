# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\MMT\generated-gui\client_keyboard_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 462)
        self.lock_button_2 = QtWidgets.QPushButton(Form)
        self.lock_button_2.setGeometry(QtCore.QRect(20, 60, 93, 41))
        self.lock_button_2.setObjectName("lock_button_2")
        self.unhook_button = QtWidgets.QPushButton(Form)
        self.unhook_button.setGeometry(QtCore.QRect(150, 60, 93, 41))
        self.unhook_button.setObjectName("unhook_button")
        self.show_button = QtWidgets.QPushButton(Form)
        self.show_button.setGeometry(QtCore.QRect(280, 60, 93, 41))
        self.show_button.setObjectName("show_button")
        self.lock_button = QtWidgets.QPushButton(Form)
        self.lock_button.setGeometry(QtCore.QRect(400, 60, 93, 41))
        self.lock_button.setObjectName("lock_button")
        self.unlock_button = QtWidgets.QPushButton(Form)
        self.unlock_button.setGeometry(QtCore.QRect(530, 60, 93, 41))
        self.unlock_button.setObjectName("unlock_button")
        self.textKeyboard = QtWidgets.QTextBrowser(Form)
        self.textKeyboard.setGeometry(QtCore.QRect(40, 130, 561, 291))
        self.textKeyboard.setObjectName("textKeyboard")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lock_button_2.setText(_translate("Form", "Lock"))
        self.unhook_button.setText(_translate("Form", "Unhook"))
        self.show_button.setText(_translate("Form", "Show"))
        self.lock_button.setText(_translate("Form", "Lock"))
        self.unlock_button.setText(_translate("Form", "Unlock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

