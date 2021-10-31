# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableView.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class TableView(QMainWindow):
    def __init__(self, window_name, column_names):
        super(TableView, self).__init__()
        self.window_name = window_name
        self.column_names = column_names
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(557, 607)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(90, 140, 381, 391))
        self.table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setObjectName("table")
        self.table.setColumnCount(len(self.column_names))
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(30, 30, 93, 71))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(160, 30, 93, 71))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        self.view_button.setFont(font)
        self.view_button.setObjectName("view_button")
        self.terminate_button = QtWidgets.QPushButton(self.centralwidget)
        self.terminate_button.setGeometry(QtCore.QRect(290, 30, 93, 71))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        self.terminate_button.setFont(font)
        self.terminate_button.setObjectName("terminate_button")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(420, 30, 93, 71))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.clear_button.clicked.connect(self.clear_data)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", self.window_name))
        for i in range(len(self.column_names)):
            column_name = self.column_names[i]
            item = self.table.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", column_name))

        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.view_button.setText(_translate("MainWindow", "View"))
        self.terminate_button.setText(_translate("MainWindow", "Terminate"))
        self.start_button.setText(_translate("MainWindow", "Start"))

    def insert_data(self, data):
        self.clear_data()

        for i in range(len(data)):
            self.table.insertRow(i)
            for j in range(len(data[i])):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def clear_data(self):
        self.table.setRowCount(0)
