# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dicom_interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 432)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(24, 24, 36);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.body)
        self.header.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.header)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2.addWidget(self.frame_7, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main_body = QtWidgets.QFrame(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.info_dicom = QtWidgets.QFrame(self.main_body)
        self.info_dicom.setStyleSheet("    QPushButtom\n"
"{\n"
"    color:white;\n"
"}")
        self.info_dicom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_dicom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_dicom.setObjectName("info_dicom")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.info_dicom)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.info_dicom)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.PatientID = QtWidgets.QLabel(self.info_dicom)
        self.PatientID.setText("")
        self.PatientID.setObjectName("PatientID")
        self.verticalLayout_7.addWidget(self.PatientID)
        self.StudyDate = QtWidgets.QLabel(self.info_dicom)
        self.StudyDate.setText("")
        self.StudyDate.setObjectName("StudyDate")
        self.verticalLayout_7.addWidget(self.StudyDate)
        self.Modality = QtWidgets.QLabel(self.info_dicom)
        self.Modality.setText("")
        self.Modality.setObjectName("Modality")
        self.verticalLayout_7.addWidget(self.Modality)
        self.Manufacturer = QtWidgets.QLabel(self.info_dicom)
        self.Manufacturer.setText("")
        self.Manufacturer.setObjectName("Manufacturer")
        self.verticalLayout_7.addWidget(self.Manufacturer)
        self.BodyPartExamined = QtWidgets.QLabel(self.info_dicom)
        self.BodyPartExamined.setText("")
        self.BodyPartExamined.setObjectName("BodyPartExamined")
        self.verticalLayout_7.addWidget(self.BodyPartExamined)
        self.horizontalLayout_8.addWidget(self.info_dicom, 0, QtCore.Qt.AlignHCenter)
        self.dicom_ima = QtWidgets.QFrame(self.main_body)
        self.dicom_ima.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dicom_ima.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dicom_ima.setObjectName("dicom_ima")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dicom_ima)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_dmt = QtWidgets.QLabel(self.dicom_ima)
        self.label_dmt.setText("")
        self.label_dmt.setObjectName("label_dmt")
        self.verticalLayout_6.addWidget(self.label_dmt)
        self.horizontalLayout_8.addWidget(self.dicom_ima)
        self.slider = QtWidgets.QFrame(self.main_body)
        self.slider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slider.setObjectName("slider")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.slider)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalSlider = QtWidgets.QSlider(self.slider)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_9.addWidget(self.verticalSlider)
        self.horizontalLayout_8.addWidget(self.slider)
        self.horizontalLayout_8.setStretch(0, 5)
        self.horizontalLayout_8.setStretch(1, 10)
        self.horizontalLayout_8.setStretch(2, 2)
        self.verticalLayout.addWidget(self.main_body)
        self.footer = QtWidgets.QFrame(self.body)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.footer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("color: #FFFFFF")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.footer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.footer)
        self.frame_6.setMinimumSize(QtCore.QSize(10, 10))
        self.frame_6.setMaximumSize(QtCore.QSize(10, 10))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Cargar Archivo"))
        self.label.setText(_translate("MainWindow", "Imágenes DICOM"))
from content import icons_rc
