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

LARGE_FONT= ("Verdana", 12)
con = lite.connect('test.db')
cur = con.cursor()

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

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.setEnabled(True)
		MainWindow.resize(422, 363)
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		MainWindow.setMouseTracking(False)
		MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
		MainWindow.setWindowTitle(_translate("MainWindow", "Attila", None))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("img.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 110, 201, 21))
		self.label.setObjectName(_fromUtf8("label"))
		self.label.setText(_translate("MainWindow", "Total Vulnerabilities Detected : ", None))

		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 20, 241, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Ellinia CLM"))
		font.setPointSize(24)
		self.label_2.setFont(font)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.label_2.setText(_translate("MainWindow", "Attila  1.0", None))

		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 70, 311, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Droid Sans Hebrew"))
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.label_3.setText(_translate("MainWindow", "Status Information", None))

		cur.execute("SELECT * FROM VULN")
		val=0
		rowss=cur.fetchall()
		for i in rowss:
			val=val+1
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(230, 110, 181, 21))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.label_4.setText(_translate("MainWindow", str(val), None))

		self.label_7 = QtGui.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(10, 140, 201, 21))
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.label_7.setText(_translate("MainWindow", "Database Statistics                :", None))

		self.label_8 = QtGui.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(230, 140, 171, 21))
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.label_8.setText(_translate("MainWindow", "Up to date", None))

		self.label_9 = QtGui.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(10, 170, 201, 21))
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.label_9.setText(_translate("MainWindow", "Monitor Status                        :", None))

		self.label_10 = QtGui.QLabel(self.centralwidget)
		self.label_10.setGeometry(QtCore.QRect(230, 170, 69, 21))
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.label_10.setText(_translate("MainWindow", "Enabled", None))

		self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 111, 31))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.pushButton_4.setText(_translate("MainWindow", "Start A Scan", None))
		self.pushButton_4.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton_4)))

		#self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
		#self.pushButton_5.setGeometry(QtCore.QRect(140, 230, 141, 31))
		#self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		#self.pushButton_5.setText(_translate("MainWindow", "Check A Software", None))
		#self.pushButton_5.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton_5)))

		self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_7.setGeometry(QtCore.QRect(300, 230, 111, 31))
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.pushButton_7.setText(_translate("MainWindow", "Update DB", None))
		self.pushButton_7.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton_7)))

		self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_8.setGeometry(QtCore.QRect(10, 270, 111, 31))
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.pushButton_8.setText(_translate("MainWindow", "Help", None))
		self.pushButton_8.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.pushButton_8)))

		self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_9.setGeometry(QtCore.QRect(140, 270, 141, 31))
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.pushButton_9.setText(_translate("MainWindow", "Quit to Tray", None))

		self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_11.setGeometry(QtCore.QRect(300, 270, 111, 31))
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.pushButton_11.setText(_translate("MainWindow", "Close", None))

		MainWindow.setCentralWidget(self.centralwidget)

		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 32))
		self.menubar.setObjectName(_fromUtf8("menubar"))

		self.menuView = QtGui.QMenu(self.menubar)
		self.menuView.setObjectName(_fromUtf8("menuView"))
		self.menuView.setTitle(_translate("MainWindow", "View", None))

		self.menuScan = QtGui.QMenu(self.menubar)
		self.menuScan.setObjectName(_fromUtf8("menuScan"))
		self.menuScan.setTitle(_translate("MainWindow", "Scan", None))

		self.menuDatabase = QtGui.QMenu(self.menubar)
		self.menuDatabase.setObjectName(_fromUtf8("menuDatabase"))
		self.menuDatabase.setTitle(_translate("MainWindow", "Database", None))

		self.menuAbout = QtGui.QMenu(self.menubar)
		self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
		self.menuAbout.setTitle(_translate("MainWindow", "About", None))

		MainWindow.setMenuBar(self.menubar)

		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.actionTray = QtGui.QAction(MainWindow)
		self.actionTray.setObjectName(_fromUtf8("actionTray"))
		self.actionTray.setText(_translate("MainWindow", "Back to Tray", None))

		self.actionStart_Manual_Scan = QtGui.QAction(MainWindow)
		self.actionStart_Manual_Scan.setObjectName(_fromUtf8("actionStart_Manual_Scan"))
		self.actionStart_Manual_Scan.setText(_translate("MainWindow", "Start A Scan", None))

		self.actionVulnerability_List = QtGui.QAction(MainWindow)
		self.actionVulnerability_List.setObjectName(_fromUtf8("actionVulnerability_List"))
		self.actionVulnerability_List.setText(_translate("MainWindow", "Vulnerability List", None))

		#self.actionManual_Search = QtGui.QAction(MainWindow)
		#self.actionManual_Search.setObjectName(_fromUtf8("actionManual_Search"))
		#self.actionManual_Search.setText(_translate("MainWindow", "Manual Search", None))

		self.actionUpdate_Database = QtGui.QAction(MainWindow)
		self.actionUpdate_Database.setObjectName(_fromUtf8("actionUpdate_Database"))
		self.actionUpdate_Database.setText(_translate("MainWindow", "Update Database", None))

		self.actionAbout_CVE = QtGui.QAction(MainWindow)
		self.actionAbout_CVE.setObjectName(_fromUtf8("actionAbout_CVE"))
		self.actionAbout_CVE.setText(_translate("MainWindow", "About CVE", None))

		self.actionAbout_the_Authors = QtGui.QAction(MainWindow)
		self.actionAbout_the_Authors.setObjectName(_fromUtf8("actionAbout_the_Authors"))
		self.actionAbout_the_Authors.setText(_translate("MainWindow", "About the Authors", None))

		self.menuView.addAction(self.actionTray)
		self.menuView.triggered[QtGui.QAction].connect(self.processtrigger)

		self.menuScan.addAction(self.actionStart_Manual_Scan)

		self.menuScan.addSeparator()

		self.menuScan.addAction(self.actionVulnerability_List)

		#self.menuScan.addAction(self.actionManual_Search)
		self.menuScan.triggered[QtGui.QAction].connect(self.processtrigger)

		self.menuDatabase.addAction(self.actionUpdate_Database)
		self.menuDatabase.triggered[QtGui.QAction].connect(self.processtrigger)

		self.menuAbout.addAction(self.actionAbout_CVE)

		self.menuAbout.addSeparator()

		self.menuAbout.addAction(self.actionAbout_the_Authors)
		self.menuAbout.triggered[QtGui.QAction].connect(self.processtrigger)

		self.menubar.addAction(self.menuView.menuAction())

		self.menubar.addAction(self.menuScan.menuAction())

		self.menubar.addAction(self.menuDatabase.menuAction())

		self.menubar.addAction(self.menuAbout.menuAction())
		
		QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
		QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def buttonClicked(self,whichone):
		if whichone=="Start A Scan":
			self.pop_msg("Scan Begin..\nYour system may slow down on first scan.\nSo, it is advised to close all programs\nPress \"OK\" to begin scanning.." ,"Attila Notification")
			os.system("python scanner.py")
			self.pop_msg("Scan Completed Successfully..!","Attila Notification")
			os.system("python displayList.py")
		#if whichone=="Check A Software":
			#print "Check A Software Not Linked"
		if whichone=="Update DB":
			self.pop_msg("Make sure your system has an active\nInternet connection and then press \"OK\"","Attila Notification")
			os.system("python forcerebuild.py")
			self.pop_msg("Program Finished Updating Database","Attila Notification")
		if whichone=="Help":
			os.system("python help.py")

	def whichbtn(self,but):
		return but.text()

	def processtrigger(self,items):
		whatmenu=items.text()
		if whatmenu=="Back to Tray":
			sys.exit()
		if whatmenu=="Start A Scan":
			self.pop_msg("Scan Begin..\nYour system may slow down on first scan.\nSo, it is advised to close all programs\nPress \"OK\" to begin scanning.." ,"Attila Notification")
			os.system("python scanner.py")
			self.pop_msg("Scan Completed Successfully..!","Attila Notification")
			os.system("python displayList.py")
		if whatmenu=="Vulnerability List":
			os.system("python displayList.py")
		#if whatmenu=="Manual Search":
			#print "Manual Search Not Linked"
		if whatmenu=="Update Database":
			self.pop_msg("Make sure your system has an active\nInternet connection and then press \"OK\"","Attila Notification")
			os.system("python forcerebuild.py")
			self.pop_msg("Program Finished Updating Database","Attila Notification")
		if whatmenu=="About CVE":
			os.system("python aboutcve.py")
		if whatmenu=="About the Authors":
			os.system("python aboutauthors.py")
	def pop_msg(self,msg,msg2):
		popup = tk.Tk()
		popup.wm_title(msg2)
		label = ttk.Label(popup, text=msg, font=LARGE_FONT)
		label.pack(side="top", fill="x", pady=10,padx=10)
		Button1= ttk.Button(popup, text="OK", command = popup.destroy)
		Button1.pack()
		popup.mainloop()



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

