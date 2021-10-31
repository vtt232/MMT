
from gui.client.FileExplorer.client_fileExplorer_ui import Ui_Form


import sys
import os
from base64 import b64encode
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from gui.popup import PopUp
class Subclass_File(QWidget):
      
    #TAO GUI
    def __init__(self, parent = None):
        super(Subclass_File, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.parent = parent
        self.ui.listFile.doubleClicked.connect(self.item_doubleClicked)
        self.ui.deleteButton.clicked.connect(self.deleteFile)
        self.ui.sendButton.clicked.connect(self.sendFile)
        self.preFolder=[]
    def show(self):
        super().show()
        
    
    #FILE EXPLORER
    #XUAT VE MAC DINH 3 THU MUC GOC
    def restore(self):
        listDefault=["My Computer"]
        self.create_list(listDefault, 0)
    #HAM GIA LAP CHO VIEC SENT MESSAGE O MO HINH CLIENT SERVER, KHI LAP VAO MO HINH THI HAM NAY CHI GUI
    #MESSAGE VA NHAN GIA TRI TRA VE LISTITEMBELOW
    def callServerToDig(self, itemName):
        try:
            self.parent.Command( { "state" : "DigFile", "filename": itemName })
            data=self.parent.Recv()
            listItemBelow = self.parent.bytes2dict(data)
            return listItemBelow
        except Exception as e:
            msg = "Cannot open this folder.\n" + str(e)
            raise Exception(msg)
    #XUAT DANH SACH THU MUC LEN CUA SO
    def create_list(self, arrName, check):
        vbox=QVBoxLayout()
        self.ui.listFile.clear()
        if(check==1):
            self.ui.listFile.addItem("...")
        self.ui.listFile.addItems(arrName)
        vbox.addWidget(self.ui.listFile)
    #XU LY TIM THU MUC CON HOAC TRO VE THU MUC CHA
    def item_doubleClicked(self):
        try:
            itemName=self.ui.listFile.currentItem().text()
            if(itemName=="..."):
                if(len(self.preFolder)==1):
                    self.preFolder.pop()
                    self.restore()
                elif (len(self.preFolder)>1):   
                    self.preFolder.pop()              
                    itemName=self.preFolder[-1]
                    listItemBelow=self.callServerToDig(itemName)
                    self.create_list(listItemBelow, 1)
                elif (len(self.preFolder)<1):
                    self.restore()
            else:
                self.preFolder.append(itemName) 
                listItemBelow=self.callServerToDig(itemName)
                self.create_list(listItemBelow, 1)
        except Exception as e:
             PopUp.show_popup(self, "Error", str(e), "critical")
             
    #XOA FILE
    #XU LY XOA FILE
    def deleteFile(self):
        try:
            itemName=self.ui.listFile.currentItem().text()
            if(itemName!="..."):
                check=self.callServerToDelete(itemName)
                if(check==True):
                    listItemBelow=self.callServerToDig(self.preFolder[-1])
                    self.create_list(listItemBelow, 1)
                else:
                    PopUp.show_popup(self, "Error", "Cannot delete file",
                                 "critical")
            else:
                PopUp.show_popup(self, "Warning", "Wrong file name",
                                 "warning")
        except Exception as e:
            PopUp.show_popup(self, "Error", str(e), "critical")
    #HAM GIA LAP CHO VIEC SENT MESSAGE O MO HINH CLIENT SERVER, KHI LAP VAO MO HINH THI HAM NAY CHI GUI
    #MESSAGE VA NHAN GIA TRI TRA VE CHECK KIEM TRA CO THANH CONG HAY KHONG
    def callServerToDelete(self, itemName):
        try:
            self.parent.Command( { "state" : "DeleteFile" ,"filename":itemName} )
            check=self.parent.Recv()
            check= self.parent.bytes2dict(check)
            return check
        except Exception as e:
            msg = "Failed to delete file.\n" + str(e)
            raise Exception(msg)




    #GUI FILE CHO SERVER
    #DOC FILE CAN GUI
    def readFile(self,filename):
        if os.path.isfile(filename):
            filesize=int(os.path.getsize(filename))
            with open(filename, 'rb') as f:
                bytesToSend = f.read(filesize)
                return True, bytesToSend
        else:
            return False, 0
    #XU LY GUI FILE
    def sendFile(self):
        try:
            itemName=self.ui.listFile.currentItem().text()
            if(itemName!="..."):
                check, data=self.readFile(itemName)
                if(check==True):
                    self.callServerToDownload(itemName,data)
                else:
                    PopUp.show_popup(self, "Error", "Cannot find file",
                                 "critical")
            else:
                PopUp.show_popup(self, "Warning", "Wrong file name",
                                 "warning")
        except Exception as e:
            PopUp.show_popup(self, "Error", str(e),
                                 "critical")
    #HAM GIA LAP CHO VIEC SENT MESSAGE O MO HINH CLIENT SERVER, KHI LAP VAO MO HINH THI HAM NAY CHI GUI
    #MESSAGE VA NHAN GIA TRI TRA VE CHECK KIEM TRA CO THANH CONG HAY KHONG   
    def callServerToDownload(self, itemName, data):
        try:
            base64_bytes=b64encode(data)
            myfile=base64_bytes.decode("utf-8")
            self.parent.Command( { "state" : "DownloadFile" ,"filename":itemName, "data": myfile})
            check=self.parent.Recv()
            check=self.parent.bytes2dict(check)
            if(check==True):
                PopUp.show_popup(self, "Success", "Download successfully.")
            else:
                raise Exception("Failed to download file.")
        except Exception as e:
            msg = "Failed to download file.\n" + str(e)
            raise Exception(msg)

#Kich hoat
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_File()
    main_win.show()
    sys.exit(app.exec_())