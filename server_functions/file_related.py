import os
import shutil
import string
from ctypes import windll


class FileHelper():
    
    
        #Kiem drive
    def get_drives():
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter+":\\")
            bitmask >>= 1
        return drives    
    
    
    #FILE EXPLORER
    #xuat ra list tep con tu ten thu muc
    def digOneLevel(self,filename):
        downOneLevelList=[]
        if(filename=="My Computer"):
            driveList=FileHelper.get_drives()
            
            for item in driveList:
                print(item)
                downOneLevelList.append(item)
            return downOneLevelList    
        elif os.path.isdir(filename):
            for item in os.listdir(filename):
                if not item.startswith('.'):
                    downOneLevelList.append(os.path.join(filename, item))
            return downOneLevelList
        else:
            downOneLevelList.append("Khong phai thu muc")
            return downOneLevelList
      
    #DOWNLOAD FILE    
    #CHINH SUA TEN FILE NEU TEN FILE TRUNG
    def preFixFileName(self,path):
        filename=os.path.basename(path)
        downloadFolder="C:\\"
        listFileName=filename.split(".")
        num=1
        while(os.path.exists(os.path.join(downloadFolder, filename))):
            listFileName.insert(1, str(num))  
            listFileName.insert(2, ".")
            filename=''.join(listFileName)
            listFileName.pop(1)
            listFileName.pop(1)
            num+=1
        return os.path.join(downloadFolder, filename)
    
    def receiveFileFromClient(self,filename,data):
        filename=self.preFixFileName(filename)
        print(filename)
        f = open(filename, 'wb')
        f.write(data)
        f.close()
        return True;
        
    #XOA FILE        
    def deleteFile(self, filename):
        if os.path.isfile(filename):
            os.unlink(filename)
            return True
        elif os.path.isdir(filename):
            shutil.rmtree(filename)
            return True
        else:       
            return False 