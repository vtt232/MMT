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
        self.verticalLayout = QtWidgets.QVBoxLayout(File_ui)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileExplorerLabel = QtWidgets.QLabel(File_ui)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileExplorerLabel.setFont(font)
        self.fileExplorerLabel.setObjectName("fileExplorerLabel")
        self.verticalLayout.addWidget(self.fileExplorerLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back = QtWidgets.QPushButton(File_ui)
        self.Back.setObjectName("Back")
        self.horizontalLayout_2.addWidget(self.Back)
        self.Reload = QtWidgets.QPushButton(File_ui)
        self.Reload.setObjectName("Reload")
        self.horizontalLayout_2.addWidget(self.Reload)
        self.pathEdit = QtWidgets.QLineEdit(File_ui)
        self.pathEdit.setObjectName("pathEdit")
        self.horizontalLayout_2.addWidget(self.pathEdit)
        self.searchEdit = QtWidgets.QLineEdit(File_ui)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 6)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.folder_content = QtWidgets.QTableWidget(File_ui)
        self.folder_content.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.folder_content.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.folder_content.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.folder_content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.folder_content.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.folder_content.setShowGrid(False)
        self.folder_content.setGridStyle(QtCore.Qt.DashLine)
        self.folder_content.setWordWrap(True)
        self.folder_content.setRowCount(0)
        self.folder_content.setColumnCount(3)
        self.folder_content.setObjectName("folder_content")
        item = QtWidgets.QTableWidgetItem()
        self.folder_content.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.folder_content.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.folder_content.setHorizontalHeaderItem(2, item)
        self.folder_content.horizontalHeader().setVisible(True)
        self.folder_content.horizontalHeader().setCascadingSectionResizes(True)
        self.folder_content.horizontalHeader().setDefaultSectionSize(200)
        self.folder_content.horizontalHeader().setStretchLastSection(True)
        self.folder_content.verticalHeader().setVisible(False)
        self.folder_content.verticalHeader().setCascadingSectionResizes(False)
        self.folder_content.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.folder_content)
        self.file_content = QtWidgets.QTableWidget(File_ui)
        self.file_content.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.file_content.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.file_content.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.file_content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.file_content.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.file_content.setShowGrid(False)
        self.file_content.setGridStyle(QtCore.Qt.DashLine)
        self.file_content.setWordWrap(True)
        self.file_content.setRowCount(0)
        self.file_content.setColumnCount(3)
        self.file_content.setObjectName("file_content")
        item = QtWidgets.QTableWidgetItem()
        self.file_content.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_content.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_content.setHorizontalHeaderItem(2, item)
        self.file_content.horizontalHeader().setVisible(True)
        self.file_content.horizontalHeader().setCascadingSectionResizes(True)
        self.file_content.horizontalHeader().setDefaultSectionSize(200)
        self.file_content.horizontalHeader().setStretchLastSection(True)
        self.file_content.verticalHeader().setVisible(False)
        self.file_content.verticalHeader().setCascadingSectionResizes(False)
        self.file_content.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.file_content)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Delete = QtWidgets.QPushButton(File_ui)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Download = QtWidgets.QPushButton(File_ui)
        self.Download.setObjectName("Download")
        self.horizontalLayout.addWidget(self.Download)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(File_ui)
        QtCore.QMetaObject.connectSlotsByName(File_ui)

    def retranslateUi(self, File_ui):
        _translate = QtCore.QCoreApplication.translate
        File_ui.setWindowTitle(_translate("File_ui", "Form"))
        self.fileExplorerLabel.setText(_translate("File_ui", "File Explorer"))
        self.Back.setText(_translate("File_ui", "Back"))
        self.Reload.setText(_translate("File_ui", "Reload"))
        self.folder_content.setSortingEnabled(True)
        item = self.folder_content.horizontalHeaderItem(0)
        item.setText(_translate("File_ui", "Folder name"))
        item = self.folder_content.horizontalHeaderItem(1)
        item.setText(_translate("File_ui", "Date created"))
        item = self.folder_content.horizontalHeaderItem(2)
        item.setText(_translate("File_ui", "Size"))
        self.file_content.setSortingEnabled(True)
        item = self.file_content.horizontalHeaderItem(0)
        item.setText(_translate("File_ui", "File name"))
        item = self.file_content.horizontalHeaderItem(1)
        item.setText(_translate("File_ui", "Date created"))
        item = self.file_content.horizontalHeaderItem(2)
        item.setText(_translate("File_ui", "Size"))
        self.Delete.setText(_translate("File_ui", "Delete"))
        self.Download.setText(_translate("File_ui", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File_ui = QtWidgets.QWidget()
    ui = Ui_File_ui()
    ui.setupUi(File_ui)
    File_ui.show()
    sys.exit(app.exec_())
