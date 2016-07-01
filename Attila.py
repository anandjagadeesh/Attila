#! /usr/bin/env python
# Required Python Libraries ------------------------------------------------------------------------------------------------------------------------

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

# Variables for Pop-up Display Setup ---------------------------------------------------------------------------------------------------------------

LARGE_FONT= ("Verdana", 12)

con = lite.connect('test.db')
cur = con.cursor()

endyear=datetime.datetime.now().year
endyear=endyear+1
startyear=endyear-3

# Class Definition for the Tray Application --------------------------------------------------------------------------------------------------------

class Tray():
######### Initialization Code for Tray -------------------------------------------------------------------------------------------------------------
	def __init__(self):
		self.tray = gtk.StatusIcon()
		self.tray.set_from_file(os.path.join(os.getcwd(),"img.png"))
		self.tray.connect('popup-menu', self.on_right_click)
		self.tray.set_tooltip('Software Vulnerability Assessment Tool')
		self.pathvar=os.getcwd() # For the current path
######### For Popup Menu on Right Click ------------------------------------------------------------------------------------------------------------
	def on_right_click(self, icon, event_button, event_time):
		self.make_menu(event_button, event_time)
######### Popup Menu Contents and Connecting them to methods ---------------------------------------------------------------------------------------
	def make_menu(self, event_button, event_time):
		menu = gtk.Menu()
		# Option 1
		opt1 = gtk.MenuItem('Open Attila') # To download/update the database
		opt1.show()
		menu.append(opt1)
		opt1.connect('activate', self.mainwindows)
		# Option 2
		opt2 = gtk.MenuItem('About') # About the code
		opt2.show()
		menu.append(opt2)
		opt2.connect('activate', self.about)
		# Option 3
		opt3 = gtk.MenuItem('Start a Scan') # To start a scan
		opt3.show()
		menu.append(opt3)
		opt3.connect('activate', self.scans)
		# Option 4
		opt4 = gtk.MenuItem('Update Database') # To download/update the database
		opt4.show()
		menu.append(opt4)
		opt4.connect('activate', self.upd_db)
		# Exit Option
		exit = gtk.MenuItem('Quit Tray') # To quit the tray
		exit.show()
		menu.append(exit)
		exit.connect('activate', gtk.main_quit) # Default GTK Function
		# Initialize popup menu
		menu.popup(None, None, gtk.status_icon_position_menu,event_button, event_time, self.tray) # Popup
######### The "About" Widget, Default from GTK -----------------------------------------------------------------------------------------------------
	def about(self, widget):
		#about_dialog = gtk.AboutDialog()
		#about_dialog.set_destroy_with_parent(True)
		#about_dialog.set_icon_name ('Software Vulnerability Analysis Tool') # Icon name
		#about_dialog.set_name('Software Vulnerability Analysis Tool') # Widget name
		#about_dialog.set_version('1.0') # Version 
		#about_dialog.set_comments((u'A software vulnerability assessment tool based on the NVD-CVE Database maintained by MITRE.org'))
		#about_dialog.set_authors([u'Designed by\n Anand J.\n Arya Rajendran\n Dickson Davies'])
		#about_dialog.run() # Run the about dialog
		#about_dialog.destroy() # Close the widget
		os.system("python help.py")
######### The scanner code (Integrated) ------------------------------------------------------------------------------------------------------------
	def scans(self,widget):
		self.pop_msg("Scan Begin..\nYour system may slow down on first scan.\nSo, it is advised to close all programs\nPress \"OK\" to begin scanning.." ,"Attila Notification")
		os.system("python scanner.py")
		self.pop_msg("Scan Completed Successfully..!","Attila Notification")
		os.system("python displayList.py")
######### The downloader code (Integrated) --------------------------------------------------------------------------------------------------------
	def upd_db(self,widget):
		self.pop_msg("Make sure your system has an active\nInternet connection and then press \"OK\"","Attila Notification")
		os.system("python forcerebuild.py")
		self.pop_msg("Program Finished Updating Database","Attila Notification")
######### Popup Message Box (Integrated) -----------------------------------------------------------------------------------------------------------
	def mainwindows(self,widget):
		os.system("python mainwindow.py")
######### Popup Message Box (Integrated) -----------------------------------------------------------------------------------------------------------
	def pop_msg(self,msg,msg2):
		popup = tk.Tk()
		popup.wm_title(msg2)
		label = ttk.Label(popup, text=msg, font=LARGE_FONT)
		label.pack(side="top", fill="x", pady=10,padx=10)
		Button1= ttk.Button(popup, text="OK", command = popup.destroy)
		Button1.pack()
		popup.mainloop()
#########-------------------------------------------------------------------------------------------------------------------------------------------

def beginners():
	Tray()
	gtk.main()

# --------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	beginners()
	con.close()
