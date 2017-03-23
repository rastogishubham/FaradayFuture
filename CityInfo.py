# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CityInfo.ui'
#
# Created: Thu Mar 23 19:36:54 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 346)
        self.label_city = QtGui.QLabel(Dialog)
        self.label_city.setGeometry(QtCore.QRect(20, 30, 62, 21))
        self.label_city.setObjectName("label_city")
        self.label_county = QtGui.QLabel(Dialog)
        self.label_county.setGeometry(QtCore.QRect(20, 80, 62, 17))
        self.label_county.setObjectName("label_county")
        self.label_lat = QtGui.QLabel(Dialog)
        self.label_lat.setGeometry(QtCore.QRect(20, 130, 62, 17))
        self.label_lat.setObjectName("label_lat")
        self.label_long = QtGui.QLabel(Dialog)
        self.label_long.setGeometry(QtCore.QRect(20, 180, 62, 17))
        self.label_long.setObjectName("label_long")
        self.City_Drop = QtGui.QComboBox(Dialog)
        self.City_Drop.setGeometry(QtCore.QRect(100, 26, 371, 31))
        self.City_Drop.setObjectName("City_Drop")
        self.text_county = QtGui.QTextEdit(Dialog)
        self.text_county.setGeometry(QtCore.QRect(100, 70, 371, 31))
        self.text_county.setObjectName("text_county")
        self.text_lat = QtGui.QTextEdit(Dialog)
        self.text_lat.setGeometry(QtCore.QRect(100, 120, 371, 31))
        self.text_lat.setObjectName("text_lat")
        self.text_long = QtGui.QTextEdit(Dialog)
        self.text_long.setGeometry(QtCore.QRect(100, 170, 371, 31))
        self.text_long.setObjectName("text_long")
        self.label_long_2 = QtGui.QLabel(Dialog)
        self.label_long_2.setGeometry(QtCore.QRect(20, 230, 62, 17))
        self.label_long_2.setObjectName("label_long_2")
        self.text_Filename = QtGui.QTextEdit(Dialog)
        self.text_Filename.setGeometry(QtCore.QRect(100, 220, 241, 31))
        self.text_Filename.setObjectName("text_Filename")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_city.setText(QtGui.QApplication.translate("Dialog", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.label_county.setText(QtGui.QApplication.translate("Dialog", "County", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lat.setText(QtGui.QApplication.translate("Dialog", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_long.setText(QtGui.QApplication.translate("Dialog", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_long_2.setText(QtGui.QApplication.translate("Dialog", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Load JSON File", None, QtGui.QApplication.UnicodeUTF8))

