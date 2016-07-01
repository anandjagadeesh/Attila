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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(647, 511)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 80, 611, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 621, 301))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.aboutcve1 = QtGui.QPushButton(self.tab)
        self.aboutcve1.setGeometry(QtCore.QRect(10, 20, 241, 36))
        self.aboutcve1.setObjectName(_fromUtf8("aboutcve1"))
        self.aboutcve1.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.aboutcve1)))
        self.credits1 = QtGui.QPushButton(self.tab)
        self.credits1.setGeometry(QtCore.QRect(540, 20, 91, 36))
        self.credits1.setObjectName(_fromUtf8("credits1"))
        self.credits1.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.credits1)))
        self.close1 = QtGui.QPushButton(self.tab)
        self.close1.setGeometry(QtCore.QRect(530, 430, 94, 36))
        self.close1.setObjectName(_fromUtf8("close1"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.close2 = QtGui.QPushButton(self.tab1)
        self.close2.setGeometry(QtCore.QRect(530, 430, 94, 36))
        self.close2.setObjectName(_fromUtf8("close2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab1)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 110, 621, 301))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 611, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.aboutcve2 = QtGui.QPushButton(self.tab1)
        self.aboutcve2.setGeometry(QtCore.QRect(10, 20, 241, 36))
        self.aboutcve2.setObjectName(_fromUtf8("aboutcve2"))
        self.aboutcve2.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.aboutcve2)))
        self.credits2 = QtGui.QPushButton(self.tab1)
        self.credits2.setGeometry(QtCore.QRect(540, 20, 91, 36))
        self.credits2.setObjectName(_fromUtf8("credits2"))
        self.credits2.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.credits2)))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.aboutcve3 = QtGui.QPushButton(self.tab_2)
        self.aboutcve3.setGeometry(QtCore.QRect(10, 20, 241, 36))
        self.aboutcve3.setObjectName(_fromUtf8("aboutcve3"))
        self.aboutcve3.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.aboutcve3)))
        self.credits3 = QtGui.QPushButton(self.tab_2)
        self.credits3.setGeometry(QtCore.QRect(540, 20, 91, 36))
        self.credits3.setObjectName(_fromUtf8("credits3"))
        self.credits3.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.credits3)))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 110, 621, 301))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 611, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.close3 = QtGui.QPushButton(self.tab_2)
        self.close3.setGeometry(QtCore.QRect(530, 430, 94, 36))
        self.close3.setObjectName(_fromUtf8("close3"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.close4 = QtGui.QPushButton(self.tab_3)
        self.close4.setGeometry(QtCore.QRect(530, 430, 94, 36))
        self.close4.setObjectName(_fromUtf8("close4"))
        self.aboutcve4 = QtGui.QPushButton(self.tab_3)
        self.aboutcve4.setGeometry(QtCore.QRect(10, 20, 241, 36))
        self.aboutcve4.setObjectName(_fromUtf8("aboutcve4"))
        self.aboutcve4.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.aboutcve4)))
        self.credits4 = QtGui.QPushButton(self.tab_3)
        self.credits4.setGeometry(QtCore.QRect(540, 20, 91, 36))
        self.credits4.setObjectName(_fromUtf8("credits4"))
        self.credits4.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.credits4)))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 601, 26))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 601, 26))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        TabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(450, 210, 171, 26))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(210, 180, 221, 26))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(450, 150, 161, 26))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 180, 26))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(10, 280, 591, 26))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(10, 320, 591, 26))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_10 = QtGui.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 181, 26))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(210, 210, 221, 26))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(10, 300, 591, 26))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(10, 180, 181, 26))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(10, 250, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(210, 150, 221, 26))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(450, 180, 171, 26))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.close5 = QtGui.QPushButton(self.tab_4)
        self.close5.setGeometry(QtCore.QRect(530, 430, 94, 36))
        self.close5.setObjectName(_fromUtf8("close5"))
        self.aboutcve5 = QtGui.QPushButton(self.tab_4)
        self.aboutcve5.setGeometry(QtCore.QRect(10, 20, 241, 36))
        self.aboutcve5.setObjectName(_fromUtf8("aboutcve5"))
        self.aboutcve5.clicked.connect(lambda: self.buttonClicked(self.whichbtn(self.aboutcve5)))
        TabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.close1, QtCore.SIGNAL(_fromUtf8("clicked()")), TabWidget.close)
        QtCore.QObject.connect(self.close2, QtCore.SIGNAL(_fromUtf8("clicked()")), TabWidget.close)
        QtCore.QObject.connect(self.close3, QtCore.SIGNAL(_fromUtf8("clicked()")), TabWidget.close)
        QtCore.QObject.connect(self.close4, QtCore.SIGNAL(_fromUtf8("clicked()")), TabWidget.close)
        QtCore.QObject.connect(self.close5, QtCore.SIGNAL(_fromUtf8("clicked()")), TabWidget.close)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Attila Help", None))
        self.label.setText(_translate("TabWidget", "About Attila", None))
        self.textBrowser.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cortoba\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A software vulnerability and exploits analysis tool is a software that checks for the vulnerabilities or exploits that are present in the softwares installed on a particular system, making use of any vulnerability database available. Most of the available vulnerability scanners are either over the network or are paid softwares available with limited applications support. The designed software tracks down the various softwares installed on a system, uses the NVD-Common Vulnerabilities and Exposures database to track down existing or unpatched vulnerabilities available with each software and inform the users about the vulnerabilities if they are fatal. The proposed system will bring the vulnerability scanning software for the open source operating systems, focussing mainly on the Debian Variants. The scanner is based on the GNU/Linux Platform that include all security rule checks based on the available CVE vulnerability database, updated from time to time. The system also includes a self updation and improvement capability by which the newer databases are downloaded automatically in preset periods, usually the start of every year and are utilized in the scanning processes in order to track the vulnerabilities that are being detected and reported over time. The software is simple to implement and provides more functionality than available counterparts as they involve mere manual software list specification and checking.</p></body></html>", None))
        self.aboutcve1.setText(_translate("TabWidget", "About CVE Database", None))
        self.credits1.setText(_translate("TabWidget", "Credits", None))
        self.close1.setText(_translate("TabWidget", "Close", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "General Information", None))
        self.close2.setText(_translate("TabWidget", "Close", None))
        self.textBrowser_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cortoba\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The initial scanning involves population of the databases. This consumes time and processing capacity.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">What this module does:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The list of installed softwares can be retrieved by executing the \'dpkg -l\' and the \'apt-show-version\' utilities in the shell. In order to execute these commands, we use the getstatusoutput function in the commands utility. The returned string is stripped off and cut into sections based on new line character and each line is then formatted such that only the software name and the software version are extracted. Now, the retrieved software list is searched in the database. For this, the software name and version is searched in the table that stores the already identified vulnerabilities in the system, then in the safe list. If it is not found in both these tables, it is then searched in the tables storing the parsed database. The vulnerability, if detected is written into the table storing the vulnerabilities else, it is written into the safe list. The detected vulnerability is shown to the user as a popup message. Once the scan is completed, we get a fully populated database to use.</p></body></html>", None))
        self.label_2.setText(_translate("TabWidget", "Scanning", None))
        self.aboutcve2.setText(_translate("TabWidget", "About CVE Database", None))
        self.credits2.setText(_translate("TabWidget", "Credits", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Scanning", None))
        self.aboutcve3.setText(_translate("TabWidget", "About CVE Database", None))
        self.credits3.setText(_translate("TabWidget", "Credits", None))
        self.textBrowser_3.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cortoba\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The thorough study of the .xml file patterns used by CVE in the NVD-CVE Site in the preliminary design phase provides a clear idea of what is present in the server, the folder or directory paths where these files are stored and the naming pattern for the stored files. This information is used in the phase one of the implementation where the data files from the server were downloaded using the urllib2 package utilities, exploiting the naming convention of the stored files. The downloaded files are then unzipped using the gzip utility. The unzipped files are in the XML format and each contains more than 600k lines of text and normal process of traversing is time consuming. So, we need to parse and retrieve the data. To parse the XML file, minidom package in the xml.dom package was used. From the parsed database,the data was retieved in terms of tag names and attribute values.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Now since the XML is parsed and the values can be retrieved, we can formulate a database for the entries as scanning through each file for all the softwares is time consuming. So we create a database and a table for each year and the XML files for each year is read and the data is written into the table. Now each entry in the table is traversed and the tables are compared for duplicate entries. If duplicate entries are found, each attribute is thoroughly compared and if they match, one of the entries is deleted and the process proceeds.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There may be situation when we need to rebuild databases. This functionality is provided by a function to update the database. The existing databases are dropped or kept as per the user\'s settings. If dropped, new table is created and populated. Also, since the date is updated in each run, the correct year is taken and new databases are downloaded automatically and the table is also created and populated using the data fetched. The popup messages were also integrated to inform user about the vulnerabilities using the Tkinter package.</p></body></html>", None))
        self.label_3.setText(_translate("TabWidget", "Updating Databases", None))
        self.close3.setText(_translate("TabWidget", "Close", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Updating Databases", None))
        self.close4.setText(_translate("TabWidget", "Close", None))
        self.aboutcve4.setText(_translate("TabWidget", "About CVE Database", None))
        self.credits4.setText(_translate("TabWidget", "Credits", None))
        self.label_4.setText(_translate("TabWidget", "This feature is not available in this version", None))
        self.label_5.setText(_translate("TabWidget", "For more queries, visit the manual at ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Advanced Help", None))
        self.label_8.setText(_translate("TabWidget", "Scanners, Popups", None))
        self.label_6.setText(_translate("TabWidget", "Arya Rajendran", None))
        self.label_7.setText(_translate("TabWidget", "UI Designs, Tray App", None))
        self.label_9.setText(_translate("TabWidget", "Dickson Davies", None))
        self.label_11.setText(_translate("TabWidget", "Resources Provided by Federal Institute of Science And Technology (FISAT), Angamaly", None))
        self.label_13.setText(_translate("TabWidget", "Supported by Mr. Jestin Joy, Dr. Sreeraj M and Mr. Pankaj Kumar G", None))
        self.label_10.setText(_translate("TabWidget", "Anand J.", None))
        self.label_12.setText(_translate("TabWidget", "Credits", None))
        self.label_14.setText(_translate("TabWidget", "Dickson Davies", None))
        self.label_15.setText(_translate("TabWidget", "Project Guided by Mr. Mahesh C., Ms. R. Reshmi and Ms. Soumya S. Raj", None))
        self.label_16.setText(_translate("TabWidget", "Arya Rajendran", None))
        self.label_17.setText(_translate("TabWidget", "Guidance & Support", None))
        self.label_18.setText(_translate("TabWidget", "anandjagadeesh@computer.org", None))
        self.label_19.setText(_translate("TabWidget", "Updaters, Main Windows", None))
        self.close5.setText(_translate("TabWidget", "Close", None))
        self.aboutcve5.setText(_translate("TabWidget", "About CVE Database", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "Credits and Author Info", None))

    def whichbtn(self,but):
        return but.text()

    def buttonClicked(self,whichone):
        if whichone=="About CVE Database":
            os.system("python aboutcve.py")
        if whichone=="Credits":
            os.system("python aboutauthors.py")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

