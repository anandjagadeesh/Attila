#! /usr/bin/env python
# Required Libraries ------------------------------------------------------------------------------------------------------------------------

import datetime # For getting the current year
import commands # For executing the shell commands
import sqlite3 as lite # For DB integration
import sys # For system based functions

# Variables ----------------------------------------------------------------------------------------------------------------------------------------

con = lite.connect('test.db')
cur = con.cursor()

endyear=datetime.datetime.now().year
endyear=endyear+1
startyear=endyear-3

# Scanner Code -------------------------------------------------------------------------------------------------------------------------------------

cur.execute("CREATE TABLE IF NOT EXISTS VULN(id TEXT, name TEXT, summary TEXT, pubdate TEXT, score TEXT, avector TEXT, acompl TEXT, auth TEXT, cimpact TEXT,iimpact TEXT,aimpact TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS SAFE(software TEXT)")

Vul_Count=0
list1=commands.getstatusoutput('dpkg -l | cut -c5-79') # Get software list using "dpkg" utility
list2=list1[1].split("\n") # Form the list for processing
# Format the entries for better processing ---------------------------------------------------------------------------------------------------------
list3=[]
for i in list2:
	j=i.split(" ")
	list4=[]
	for k in j:
		if k!="":
			l=k.split(":")
			k=l[0]
			l=k.split("-")
			k=l[0]
			l=k.split("~")
			k=l[0]
			k.replace("install","").replace("deinstall","").replace("\t","").replace("-"," ")
			k.replace(":"," ").replace("amd64","").replace("desktop ","").replace("default ","")
			list4.append(k)
			string1=' '.join(list4)
	list4=[]
	list4.append(string1)
	list4.append(" ")
	string2=''.join(list4)
	if string2=='g 4 ':
		string2='g++ 4 '
	if string2 not in list3:
		list3.append(string2)
del list3[:5] # Deleting the unwanted entries and headers at the top
list1=commands.getstatusoutput("apt-show-versions") # Get software list using "dpkg" utility
list2=list1[1].split("\n") # Form the list for processing
list4=[]
for i in list2:
	temp1=i.split(':')
	temp2=temp1[1].split(" ")
	j=temp1[0]+" "+temp2[1]
	list4.append(j)
# Scan Begins --------------------------------------------------------------------------------------------------------------------------------------
for i in list3:
	cur.execute("SELECT * FROM SAFE")
	rows2=cur.fetchall()
	searchconf=1
	for row in rows2:
		if i in row[0]:
			searchconf=0
	if searchconf==1:
		cur.execute("SELECT * FROM VULN")
		rows3=cur.fetchall()
		for row in rows3:
			if i in row[1] or row[1] in i:
				Vul_Count=Vul_Count+1
				searchconf=0
		if searchconf==1:
			flag1=0
			for x in range(startyear,endyear):
				cur.execute("SELECT * FROM C"+str(x))
				rows = cur.fetchall()
				for row in rows:
					if i in row[1]:
						Vul_Count=Vul_Count+1
						flag1=1
						print i
						print row[1]
						cur.execute("INSERT INTO VULN VALUES(?,?,?,?,?,?,?,?,?,?,?)",(row[0],i,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
						con.commit()
						break
			if flag1==0:
				cur.execute("INSERT INTO SAFE(software) VALUES('"+str(i)+"')")
				con.commit()
# Double Check Verification ------------------------------------------------------------------------------------------------------------------------
#for i in list4:
#	cur.execute("SELECT * FROM SAFE")
#	rows2=cur.fetchall()
#	searchconf=1
#	for row in rows2:
#		if i in row[0]:
#			searchconf=0
#	if searchconf==1:
#		cur.execute("SELECT * FROM VULN")
#		rows3=cur.fetchall()
#		for row in rows3:
#			if i in row[1]:
#				Vul_Count=Vul_Count+1
#				searchconf=0
#				
#		if searchconf==1:
#			flag1=0
#			for x in range(startyear,endyear):
#				cur.execute("SELECT * FROM C"+str(x))
#				rows = cur.fetchall()
#				for row in rows:
#					if i in row[1] or row[1] in i:
#						Vul_Count=Vul_Count+1
#						flag1=1
#						print i
#						print row[1]
#						cur.execute("INSERT INTO VULN VALUES(?,?,?,?,?,?,?,?,?,?,?)",(row[0],i,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
#						con.commit()
#						break
#			if flag1==0:
#				cur.execute("INSERT INTO SAFE(software) VALUES('"+str(i)+"')")
#				con.commit()
#
# Scanner Code Ends --------------------------------------------------------------------------------------------------------------------------------
