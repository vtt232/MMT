from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from PIL.ImageQt import ImageQt
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QFileDialog



from PIL import Image

import sys
import PIL
import io
import time
import os
#threading
import threading
from gui.client.Capture_Stream.client_screen_ui import Ui_screenUI
from gui.popup import PopUp
class Subclass_Screen(QWidget):
    
    def __init__(self, parent = None):
        super(Subclass_Screen, self).__init__()
        self.ui = Ui_screenUI()
        self.ui.setupUi(self)
        
        self.parent = parent
        #Bind
        self.quality = self.ui.QualitySlider.value()
        self.ui.QualitySlider.valueChanged.connect(self.asign)
        self.ui.Capture.clicked.connect(
            self.CaptureScreen)
        self.ui.Save.clicked.connect(
            self.Save)
        self.ui.Stream_button.clicked.connect(
            self.Stream)
        self.ui.Stop_stream_button.clicked.connect(
            self.stopStream)
        self.stop = False
        self.streaming = None
        self.img = None
    def asign(self):
        self.quality = self.ui.QualitySlider.value()
    def show(self):
        self.stop = False
        super().show()
    def closeEvent(self, event):
        self.stopStream()
    def image_from_bytes(self, data):
        return PIL.Image.open(io.BytesIO(data))
    def decode(self, data): #return a pixmap
        self.img = img = self.image_from_bytes(data)
        size = (self.ui.View.width(), self.ui.View.height())
        
        img = self.img.copy()
        img.thumbnail(size, Image.ANTIALIAS)
        qim = ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qim).copy()
        
        return pixmap    
    def display(self, data):
        self.ui.View.setPixmap(self.decode(data))
    def CaptureScreen(self):
        try:
            self.parent.Command( { "state" : "Capture", "quality" : self.quality} )
            data = self.parent.Recv()
            self.display(data)
        except Exception as e:
            errorMsg = "Cannot capture screen.\n" + str(e)
            PopUp.show_popup(self, "Error", errorMsg,
                           "warning")
    def Save(self):
        if self.img != None:
            filename, _ = QFileDialog.getSaveFileName(
                        self, filter='*.jpg;;*.png;;*.jpeg',
                        directory=os.getenv('HOME'))
            
            if filename:
                self.img.save(filename)
    def Stream(self):
        if (self.streaming != None):
            self.stop = True
            self.streaming.join()
            self.streaming = None
        self.ui.Capture.setEnabled(False)
        self.ui.Save.setEnabled(False)
        self.stop = False
        self.streaming = threading.Thread(target = self.StreamThread, 
                                  args=(lambda: self.streaming == None, ))
        self.streaming.start()
    def StreamThread(self, stop):
        start_time = time.time()
        count = 0
        while True:
            if stop():
                break
            try:
                self.parent.Command( { "state" : "Capture", "quality" : self.quality} )
                data = self.parent.Recv()
                self.display(data)
                count+=1
                if (time.time() - start_time >= 2):
                    self.ui.FPS.setText(str(count // 2))
                    count = 0
                    start_time = time.time()
            except Exception as e:
                self.streaming = None
                return
    def stopStream(self):
        self.ui.Capture.setEnabled(True)
        self.ui.Save.setEnabled(True)
        self.ui.FPS.setText("None")
        if (self.streaming != None):
            self.streaming = None
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_Screen()
    main_win.show()
    sys.exit(app.exec_())