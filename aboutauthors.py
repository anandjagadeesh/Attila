import gtk # For tray application
from xml.dom import minidom # For parsing the xml file
import glob # For traversing the folders
import os # For the OS related system calls
import os.path # For tracing the file paths
import urllib2 # For downloading the databases
import datetime # For getting the current year
import gzip # For unzipping the databases downloaded
import commands # For executing the shell commands
import Tkinter as tk # For popups
import ttk # For popups
import sqlite3 as lite # For DB integration
import sys # For system based functions
from PyQt4 import QtCore, QtGui # For interface

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 314)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 270, 94, 36))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 181, 26))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 70, 221, 26))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(460, 70, 161, 26))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 181, 26))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 100, 221, 26))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(460, 100, 171, 26))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(460, 130, 171, 26))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 180, 26))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(220, 130, 221, 26))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 591, 26))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 220, 591, 26))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 240, 591, 26))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(20, 170, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Attila", None))
        self.pushButton.setText(_translate("Dialog", "Close", None))
        self.label.setText(_translate("Dialog", "Credits", None))
        self.label_2.setText(_translate("Dialog", "Anand J.", None))
        self.label_3.setText(_translate("Dialog", "anandjagadeesh@computer.org", None))
        self.label_4.setText(_translate("Dialog", "UI Designs, Tray App", None))
        self.label_5.setText(_translate("Dialog", "Arya Rajendran", None))
        self.label_6.setText(_translate("Dialog", "Arya Rajendran", None))
        self.label_7.setText(_translate("Dialog", "Updaters, Main Windows", None))
        self.label_8.setText(_translate("Dialog", "Scanners, Popups", None))
        self.label_9.setText(_translate("Dialog", "Dickson Davies", None))
        self.label_10.setText(_translate("Dialog", "Dickson Davies", None))
        self.label_11.setText(_translate("Dialog", "Resources Provided by Federal Institute of Science And Technology (FISAT), Angamaly", None))
        self.label_12.setText(_translate("Dialog", "Project Guided by Mr. Mahesh C., Ms. R. Reshmi and Ms. Soumya S. Raj", None))
        self.label_13.setText(_translate("Dialog", "Supported by Mr. Jestin Joy, Dr. Sreeraj M and Mr. Pankaj Kumar G", None))
        self.label_14.setText(_translate("Dialog", "Guidance & Support", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

