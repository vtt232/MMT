from generated_gui.client_fileExplorer import Ui_File_ui

from collections import namedtuple
import sys
import os
from datetime import datetime, timezone
from os.path import abspath
from base64 import b64encode
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from gui.popup import PopUp

class Subclass_File(QWidget):
      
    #TAO GUI
    def __init__(self, parent = None):
        super(Subclass_File, self).__init__()
        self.ui = Ui_File_ui()
        self.ui.setupUi(self)
        
        self.parent = parent
        #bind
        
        self.ui.Back.clicked.connect(lambda: print("hi"))
        self.ui.Reload.clicked.connect(lambda: print("hi"))
        self.ui.Delete.clicked.connect(lambda: print("hi"))
        self.ui.Download.clicked.connect(lambda: print("hi"))
        
        self.ui.file_content.doubleClicked.connect(lambda : 
                                       self.item_doubleClicked(self.ui.file_content))
        self.ui.folder_content.doubleClicked.connect(lambda : 
                                       self.item_doubleClicked(self.ui.folder_content))
        self.ui.pathEdit.returnPressed.connect(self.Populate)
        self.preFolder=[]
        self.currentPath = ""
    def Populate(self, to = False):
        #C:/Users/Ms Dung/Desktop
        if not to:
            self.currentPath  = self.ui.pathEdit.text()
        data = []
        DataTuple = namedtuple('Data', ['name', 'date',
                                    'size', 'type'])
        for i in os.listdir(self.currentPath ):
            curpath = os.path.join(self.currentPath , i)
            curpath = curpath.replace('\\', '/')
            time = datetime.fromtimestamp(os.path.getmtime(curpath)).strftime('%d-%m-%Y-%H:%M')
            isFile = os.path.isfile(curpath)
            if not isFile: 
                size = 0
            else:
                size = os.path.getsize(curpath)
            data.append(DataTuple(i, time, size, isFile))
        folders = [x[:-1] for x in data if x.type == False]
        files   = [x[:-1] for x in data if x.type == True]
        
        self.insert_data(files, self.ui.file_content)
        self.insert_data(folders, self.ui.folder_content)
    def show(self):
        super().show()
    def insert_data(self, data, table):
        self.clear_data(table)
        for i in range(len(data)):
            table.insertRow(i)
            for j in range(len(data[i])):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
    def clear_data(self, table):
        table.setRowCount(0)
    def item_doubleClicked(self, table):
        name = (table.item(table.currentRow(),0).text())
        self.currentPath = os.path.join(self.currentPath, name)
        self.currentPath = self.currentPath.replace('\\', '/')
        self.Populate(True)
#Kich hoat
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_File()
    main_win.show()
    sys.exit(app.exec_())