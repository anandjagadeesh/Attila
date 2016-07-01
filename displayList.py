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

con = lite.connect('test.db')
cur = con.cursor()

NORM_FONT= ("Verdana", 12)

class Window(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle('Attila')
		self.setGeometry(100, 100, 800, 300)
		mygroupbox = QtGui.QGroupBox('Vulnerabilities Detected')
		myform = QtGui.QFormLayout()
		labellist = []
		combolist = []
		tamas=[]
		cur.execute("SELECT * FROM VULN")
		val=0
		rowss=cur.fetchall()
		for i in rowss:
			val=val+1
		cur.execute("SELECT * FROM VULN")
		for i in range(val):
			rows3=cur.fetchone()
			button=QtGui.QPushButton(str(rows3[1]))
			button.setFixedWidth(550)
			button.clicked.connect(self.buttonClicked)
			labellist.append(button)
			combolist.append(QtGui.QLabel("Vulnerability Score : "+rows3[4]))
			myform.addRow(labellist[i],combolist[i])
		mygroupbox.setLayout(myform)
		scroll = QtGui.QScrollArea()
		scroll.setWidget(mygroupbox)
		scroll.setWidgetResizable(True)
		layout = QtGui.QVBoxLayout(self)
		layout.addWidget(scroll)
	def buttonClicked(self):
		sender = self.sender()
		cur.execute("SELECT * FROM VULN")
		rowss=cur.fetchall()
		for i in rowss:
			if sender.text() in i[1]:
				t1=sender.text()
				t=t1.split(" ")
				msg="Package            :  "+str(t[0])+'\n'+"Version            :  "+str(t[1])+"\n"+"CVE-ID             :  "+str(i[0])+'\n'+"Date Added         :  "+str(i[3])+'\n'+"Summary            :  \n\n"+str(i[2])+'\n\n\n'+"Vulnerability Score:  "+str(i[4])+'\n'
				msg2="Vulnerability Details"
				self.pop_msg2(msg,msg2)
	def pop_msg2(self,msg,msg2):
		popup = tk.Tk()
		popup.wm_title(msg2)
		label = ttk.Label(popup, text=msg, font=NORM_FONT,wraplength=500)
		label.pack(side="top", fill="x", pady=10,padx=10)
		Button1= ttk.Button(popup, text="OK", command = popup.destroy)
		Button1.pack()
		popup.mainloop()		
	@staticmethod
	def callresults():
		app = QtGui.QApplication(sys.argv)
		window = Window()
		window.show()
		app.exec_()
		app.deleteLater()
if __name__ == '__main__':
	Window.callresults()
