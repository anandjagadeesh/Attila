#! /usr/bin/env python
# Required Python Libraries ------------------------------------------------------------------------------------------------------------------------

from xml.dom import minidom # For parsing the xml file
import glob # For traversing the folders
import os # For the OS related system calls
import os.path # For tracing the file paths
import urllib2 # For downloading the databases
import datetime # For getting the current year
import gzip # For unzipping the databases downloaded
import sqlite3 as lite # For DB integration
import sys # For system based functions

# Variables ----------------------------------------------------------------------------------------------------------------------------------------

con = lite.connect('test.db')
cur = con.cursor()

endyear=datetime.datetime.now().year
endyear=endyear+1
startyear=endyear-3
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Updater Code -------------------------------------------------------------------------------------------------------------------------------------
pathvar=os.getcwd()
os.chdir(pathvar)
if not os.path.exists(os.path.join(os.getcwd(),"gzdb")):
	os.makedirs(os.path.join(os.getcwd(),"gzdb"))
if not os.path.exists(os.path.join(os.getcwd(),"xmldb")):
	os.makedirs(os.path.join(os.getcwd(),"xmldb"))
t=sys.argv[1]
b2='https://nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Modified.xml.gz'
yw2p1='https://nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-'

nf2p1='nvdcve-2.0-'
nfp2='.xml.gz'
if not os.path.isfile(os.path.join(os.getcwd(),"xmldb/nvdcve-2.0-Modified.xml")):
	with open(os.path.join(os.getcwd(),"gzdb/nvdcve-2.0-Modified.xml.gz"), "wb") as file1:
		file1.write(urllib2.urlopen(b2).read())
	file2=gzip.GzipFile(os.path.join(os.getcwd(),"gzdb/nvdcve-2.0-Modified.xml.gz"), 'rb')
	data2 = file(os.path.join(os.getcwd(),"xmldb/nvdcve-2.0-Modified.xml"), 'wb')
	data2.write(file2.read())
if (t=='y' or t=='Y' or t=='yes' or t=='YES' or t=='Yes'):
	cur.execute("DROP TABLE IF EXISTS CMOD")
cur.execute(""" SELECT COUNT(*) FROM sqlite_master WHERE name = ?  """, ("CMOD", ))
res = cur.fetchone()
if not bool(res[0]):
	cur.execute("CREATE TABLE IF NOT EXISTS CMOD(id TEXT, name TEXT, summary TEXT, pubdate TEXT, score TEXT, avector TEXT, acompl TEXT, auth TEXT, cimpact TEXT,iimpact TEXT,aimpact TEXT)")
	xmldoc=minidom.parse(os.path.join(os.getcwd(),"xmldb/nvdcve-2.0-Modified.xml"))
	entries=xmldoc.getElementsByTagName("entry")
	for entry in entries:
		vulswlist=entry.getElementsByTagName("vuln:vulnerable-software-list")
		for vulsw in vulswlist:
			vul=vulsw.getElementsByTagName("vuln:product")
			for vul2 in vul:
				a=vul2.firstChild.data.replace(":"," ").replace("cpe /a ","").replace("cpe /o ","").replace("cpe /h ","").replace("_"," ").lower()
				vid=entry.getElementsByTagName("vuln:cve-id")[0].firstChild.data
				summary=entry.getElementsByTagName("vuln:summary")[0].firstChild.data
				date=entry.getElementsByTagName("vuln:published-datetime")[0].firstChild.data
				b=entry.getElementsByTagName("vuln:cvss")[0]
				c=b.getElementsByTagName("cvss:base_metrics")[0]
				score=c.getElementsByTagName("cvss:score")[0].firstChild.data
				avector=c.getElementsByTagName("cvss:access-vector")[0].firstChild.data
				acompl=c.getElementsByTagName("cvss:access-complexity")[0].firstChild.data
				auth=c.getElementsByTagName("cvss:authentication")[0].firstChild.data
				cimpact=c.getElementsByTagName("cvss:confidentiality-impact")[0].firstChild.data
				iimpact=c.getElementsByTagName("cvss:integrity-impact")[0].firstChild.data
				aimpact=c.getElementsByTagName("cvss:availability-impact")[0].firstChild.data
				cur.execute("INSERT INTO CMOD VALUES(?,?,?,?,?,?,?,?,?,?,?)",(vid,a,summary,date,score,avector,acompl,auth,cimpact,iimpact,aimpact))
				con.commit()
for x in range(startyear,endyear):
	if not os.path.isfile(os.path.join(os.getcwd(),"xmldb/"+nf2p1+str(x)+".xml")):
		with open(os.path.join(os.getcwd(),"gzdb/"+nf2p1+str(x)+nfp2), "wb") as file1:
			file1.write(urllib2.urlopen(yw2p1+str(x)+nfp2).read())
		file2=gzip.GzipFile(os.path.join(os.getcwd(),"gzdb/"+nf2p1+str(x)+nfp2), 'rb')
		data2 = file(os.path.join(os.getcwd(),"xmldb/"+nf2p1+str(x)+".xml"), 'wb')
		data2.write(file2.read())
	if (t=='y' or t=='Y' or t=='yes' or t=='YES' or t=='Yes'):
		cur.execute("DROP TABLE IF EXISTS C"+str(x))
	cur.execute(""" SELECT COUNT(*) FROM sqlite_master WHERE name = ?  """, ("C"+str(x), ))
	res = cur.fetchone()
	if not bool(res[0]):
		cur.execute("CREATE TABLE IF NOT EXISTS C"+str(x)+"(id TEXT, name TEXT, summary TEXT, pubdate TEXT, score TEXT, avector TEXT, acompl TEXT, auth TEXT, cimpact TEXT,iimpact TEXT,aimpact TEXT)")
		xmldoc=minidom.parse(os.path.join(os.getcwd(),"xmldb/"+nf2p1+str(x)+".xml"))
		entries=xmldoc.getElementsByTagName("entry")
		for entry in entries:
			vulswlist=entry.getElementsByTagName("vuln:vulnerable-software-list")
			for vulsw in vulswlist:
				vul=vulsw.getElementsByTagName("vuln:product")
				for vul2 in vul:
					a=vul2.firstChild.data.replace(":"," ").replace("cpe /a ","").replace("cpe /o ","").replace("cpe /h ","").replace("_"," ").lower()
					vid=entry.getElementsByTagName("vuln:cve-id")[0].firstChild.data
					summary=entry.getElementsByTagName("vuln:summary")[0].firstChild.data
					date=entry.getElementsByTagName("vuln:published-datetime")[0].firstChild.data
					b=entry.getElementsByTagName("vuln:cvss")[0]
					c=b.getElementsByTagName("cvss:base_metrics")[0]
					score=c.getElementsByTagName("cvss:score")[0].firstChild.data
					avector=c.getElementsByTagName("cvss:access-vector")[0].firstChild.data
					acompl=c.getElementsByTagName("cvss:access-complexity")[0].firstChild.data
					auth=c.getElementsByTagName("cvss:authentication")[0].firstChild.data
					cimpact=c.getElementsByTagName("cvss:confidentiality-impact")[0].firstChild.data
					iimpact=c.getElementsByTagName("cvss:integrity-impact")[0].firstChild.data
					aimpact=c.getElementsByTagName("cvss:availability-impact")[0].firstChild.data
					cur.execute("INSERT INTO C"+str(x)+" VALUES(?,?,?,?,?,?,?,?,?,?,?)",(vid,a,summary,date,score,avector,acompl,auth,cimpact,iimpact,aimpact))
					con.commit()
# Updater Code Ended -------------------------------------------------------------------------------------------------------------------------------
