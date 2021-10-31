# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_capture_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screenUI(object):
    def setupUi(self, screenUI):
        screenUI.setObjectName("screenUI")
        screenUI.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(screenUI.sizePolicy().hasHeightForWidth())
        screenUI.setSizePolicy(sizePolicy)
        self.groupBox_3 = QtWidgets.QGroupBox(screenUI)
        self.groupBox_3.setGeometry(QtCore.QRect(680, 0, 111, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QualitySlider = QtWidgets.QSlider(self.groupBox_3)
        self.QualitySlider.setToolTip("")
        self.QualitySlider.setAutoFillBackground(False)
        self.QualitySlider.setMinimum(50)
        self.QualitySlider.setMaximum(200)
        self.QualitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.QualitySlider.setObjectName("QualitySlider")
        self.verticalLayout.addWidget(self.QualitySlider)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Capture = QtWidgets.QPushButton(self.groupBox)
        self.Capture.setObjectName("Capture")
        self.horizontalLayout_2.addWidget(self.Capture)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Stream_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Stream_button.setObjectName("Stream_button")
        self.verticalLayout_2.addWidget(self.Stream_button)
        self.Stop_stream_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Stop_stream_button.setObjectName("Stop_stream_button")
        self.verticalLayout_2.addWidget(self.Stop_stream_button)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.Save = QtWidgets.QPushButton(self.groupBox_3)
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)
        self.groupBox_4 = QtWidgets.QGroupBox(screenUI)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 661, 591))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.View = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.View.sizePolicy().hasHeightForWidth())
        self.View.setSizePolicy(sizePolicy)
        self.View.setMinimumSize(QtCore.QSize(0, 0))
        self.View.setText("")
        self.View.setObjectName("View")
        self.horizontalLayout.addWidget(self.View)
        self.groupBox_5 = QtWidgets.QGroupBox(screenUI)
        self.groupBox_5.setGeometry(QtCore.QRect(680, 240, 111, 46))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FPS = QtWidgets.QLabel(self.groupBox_5)
        self.FPS.setAlignment(QtCore.Qt.AlignCenter)
        self.FPS.setObjectName("FPS")
        self.horizontalLayout_3.addWidget(self.FPS)

        self.retranslateUi(screenUI)
        QtCore.QMetaObject.connectSlotsByName(screenUI)

    def retranslateUi(self, screenUI):
        _translate = QtCore.QCoreApplication.translate
        screenUI.setWindowTitle(_translate("screenUI", "Form"))
        self.groupBox_3.setTitle(_translate("screenUI", "Functions"))
        self.groupBox.setTitle(_translate("screenUI", "Image"))
        self.Capture.setText(_translate("screenUI", "Capture"))
        self.groupBox_2.setTitle(_translate("screenUI", "Stream"))
        self.Stream_button.setText(_translate("screenUI", "Stream"))
        self.Stop_stream_button.setText(_translate("screenUI", "Stop stream"))
        self.Save.setText(_translate("screenUI", "Save"))
        self.groupBox_4.setTitle(_translate("screenUI", "Screen"))
        self.groupBox_5.setTitle(_translate("screenUI", "FPS"))
        self.FPS.setText(_translate("screenUI", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screenUI = QtWidgets.QWidget()
    ui = Ui_screenUI()
    ui.setupUi(screenUI)
    screenUI.show()
    sys.exit(app.exec_())

