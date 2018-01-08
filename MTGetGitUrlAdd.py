import os
import re
import requests
import sys
import thread
from bs4 import BeautifulSoup


i = 0

reload(sys)
sys.setdefaultencoding("utf-8")

def getGitUrlWithNum(i, x):

	try:
		document_name_url = open("f-droid_name_url_" + str(i) + ".txt", "a")
		document_url = open("f-droid_url_" + str(i) + ".txt", "a")
		document = open("f-droid_app.txt", "r")
		
		j = 0
		for url in document.readlines():
			j = j + 1
			if j <= (i - 1) * 200 or j > i * 200 or j < x:
				continue

			sourcehtml = url[0:len(url)-1]
			sourceurl = requests.get(sourcehtml).content
			sourcesoup = BeautifulSoup(sourceurl, 'html.parser')

			namenode = sourcesoup.find_all("h3", class_ = "package-name")
			if namenode == None:
				namenode = sourcesoup.find_all("header", class_ = "package-name")
			projectname = namenode[0].string
			projectname = projectname.lstrip().rstrip()
			
			judge = False
			sourcelabel_link = sourcesoup.find_all("li", class_ = "package-link")
			for sourcelabel in sourcelabel_link :
				sourcetag = sourcelabel.find("a", string = "Source Code")
				if sourcetag != None :
					giturl = sourcetag.get('href')
					document_name_url.write(projectname + "------" + giturl + "\n")
					document_url.write(giturl + "\n")
					judge = True
			if judge == False:
				document_name_url.write(projectname + "------ do not have direct source code url\n")

		document.close()
		document_name_url.close()
		document_url.close()
		print str(i) + " is ok\n"
	except:

		document.close()
		document_name_url.close()
		document_url.close()
		print str(i) + " exists error in " + str(j) + "\n"

try:
	thread.start_new_thread(getGitUrlWithNum, (3,571,))
except:
	print "Error!!"

while 1:
	pass
