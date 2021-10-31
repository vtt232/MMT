# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\FileExplorer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 457)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileExplorerLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileExplorerLabel.setFont(font)
        self.fileExplorerLabel.setObjectName("fileExplorerLabel")
        self.verticalLayout.addWidget(self.fileExplorerLabel)
        self.listFile = QtWidgets.QListWidget(Form)
        self.listFile.setObjectName("listFile")

        
        
        item = QtWidgets.QListWidgetItem()
        self.listFile.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listFile.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listFile.addItem(item)
        
        
        
        self.verticalLayout.addWidget(self.listFile)
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        
        
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileExplorerLabel.setText(_translate("Form", "File Explorer"))
        __sortingEnabled = self.listFile.isSortingEnabled()
        self.listFile.setSortingEnabled(False)
        item = self.listFile.item(0)
        item.setText(_translate("Form", "My Computer"))
        self.listFile.setSortingEnabled(__sortingEnabled)
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.sendButton.setText(_translate("Form", "Send"))
        