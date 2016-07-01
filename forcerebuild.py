from PyQt4 import QtCore, QtGui
import os # For the OS related system calls
import os.path # For tracing the file paths
import sys


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

class Ui_DatabaseUpdate(object):
	def setupUi(self, DatabaseUpdate):
		DatabaseUpdate.setObjectName(_fromUtf8("DatabaseUpdate"))
		DatabaseUpdate.resize(454, 181)
		self.label = QtGui.QLabel(DatabaseUpdate)
		self.label.setGeometry(QtCore.QRect(10, 10, 431, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("David CLM"))
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(DatabaseUpdate)
		self.label_2.setGeometry(QtCore.QRect(10, 50, 621, 51))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.label_3 = QtGui.QLabel(DatabaseUpdate)
		self.label_3.setGeometry(QtCore.QRect(10, 80, 421, 26))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.pushButton = QtGui.QPushButton(DatabaseUpdate)
		self.pushButton.setGeometry(QtCore.QRect(20, 120, 181, 36))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton)))
		self.pushButton_2 = QtGui.QPushButton(DatabaseUpdate)
		self.pushButton_2.setGeometry(QtCore.QRect(250, 120, 181, 36))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_2.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton_2)))

		self.retranslateUi(DatabaseUpdate)
		QtCore.QMetaObject.connectSlotsByName(DatabaseUpdate)

	def retranslateUi(self, DatabaseUpdate):
		DatabaseUpdate.setWindowTitle(_translate("DatabaseUpdate", "Update Database", None))
		self.label.setText(_translate("DatabaseUpdate", "Force Database Rebuild?", None))
		self.label_2.setText(_translate("DatabaseUpdate", "Database Rebuild will delete old databases and creates new one. ", None))
		self.label_3.setText(_translate("DatabaseUpdate", "You can select No if you wish to keep the existing database.", None))
		self.pushButton.setText(_translate("DatabaseUpdate", "Yes", None))
		self.pushButton_2.setText(_translate("DatabaseUpdate", "No", None))
	def buttonClicked(self,whichone):
		if whichone=='Yes':
			os.system("python updater.py yes")
		if whichone=='No':
			os.system("python updater.py no")
		sys.exit()
	def whichbtn(self,b):
		return b.text()
    


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	DatabaseUpdate = QtGui.QDialog()
	ui = Ui_DatabaseUpdate()
	ui.setupUi(DatabaseUpdate)
	DatabaseUpdate.show()
	sys.exit(app.exec_())

