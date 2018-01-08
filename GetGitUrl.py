import os
import re
import requests
import sys
from bs4 import BeautifulSoup

document_name_url = open("f-droid_name_url.txt", "a")
document_url = open("f-droid_url.txt", "a")
document = open("f-droid_app.txt", "r")

i = 0

# reload(sys)
# sys.setdefaultencoding("utf-8")

for url in document.readlines():
	i = i + 1
	if i <= 397:
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
