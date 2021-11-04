# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileExplorer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_File_ui(object):
    def setupUi(self, File_ui):
        File_ui.setObjectName("File_ui")
        File_ui.resize(801, 600)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(File_ui)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fileExplorerLabel = QtWidgets.QLabel(File_ui)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileExplorerLabel.setFont(font)
        self.fileExplorerLabel.setObjectName("fileExplorerLabel")
        self.verticalLayout_3.addWidget(self.fileExplorerLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back = QtWidgets.QPushButton(File_ui)
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        self.Home = QtWidgets.QPushButton(File_ui)
        self.Home.setObjectName("Home")
        self.horizontalLayout.addWidget(self.Home)
        self.pathEdit = QtWidgets.QLineEdit(File_ui)
        self.pathEdit.setObjectName("pathEdit")
        self.horizontalLayout.addWidget(self.pathEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.content = QtWidgets.QTableWidget(File_ui)
        self.content.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.content.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.content.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.content.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.content.setShowGrid(False)
        self.content.setGridStyle(QtCore.Qt.DashLine)
        self.content.setWordWrap(True)
        self.content.setRowCount(0)
        self.content.setColumnCount(3)
        self.content.setObjectName("content")
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(2, item)
        self.content.horizontalHeader().setVisible(True)
        self.content.horizontalHeader().setCascadingSectionResizes(True)
        self.content.horizontalHeader().setDefaultSectionSize(200)
        self.content.horizontalHeader().setStretchLastSection(True)
        self.content.verticalHeader().setVisible(False)
        self.content.verticalHeader().setCascadingSectionResizes(False)
        self.content.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.content)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Reload = QtWidgets.QPushButton(File_ui)
        self.Reload.setObjectName("Reload")
        self.verticalLayout_2.addWidget(self.Reload)
        self.Del = QtWidgets.QPushButton(File_ui)
        self.Del.setObjectName("Del")
        self.verticalLayout_2.addWidget(self.Del)
        self.Upload = QtWidgets.QPushButton(File_ui)
        self.Upload.setObjectName("Upload")
        self.verticalLayout_2.addWidget(self.Upload)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(File_ui)
        QtCore.QMetaObject.connectSlotsByName(File_ui)

    def retranslateUi(self, File_ui):
        _translate = QtCore.QCoreApplication.translate
        File_ui.setWindowTitle(_translate("File_ui", "Form"))
        self.fileExplorerLabel.setText(_translate("File_ui", "File Explorer"))
        self.Back.setText(_translate("File_ui", "Parent"))
        self.Home.setText(_translate("File_ui", "Home"))
        self.content.setSortingEnabled(True)
        item = self.content.horizontalHeaderItem(0)
        item.setText(_translate("File_ui", "Name"))
        item = self.content.horizontalHeaderItem(1)
        item.setText(_translate("File_ui", "Date created"))
        item = self.content.horizontalHeaderItem(2)
        item.setText(_translate("File_ui", "Size"))
        self.Reload.setText(_translate("File_ui", "Reload"))
        self.Del.setText(_translate("File_ui", "Delete"))
        self.Upload.setText(_translate("File_ui", "Upload file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File_ui = QtWidgets.QWidget()
    ui = Ui_File_ui()
    ui.setupUi(File_ui)
    File_ui.show()
    sys.exit(app.exec_())