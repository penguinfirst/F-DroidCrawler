import os
import re
import requests
import sys
from bs4 import BeautifulSoup

document_name_url = open("f-droid_name_url.txt", "a")
document_url = open("f-droid_url.txt", "a")
document = open("f-droid_app.txt", "r")

i = 0

reload(sys)
sys.setdefaultencoding("utf-8")

for url in document.readlines():
	i = i + 1
	if i <= 768:
		continue

	sourcehtml = url[0:len(url)-1]
	sourceurl = requests.get(sourcehtml).content
	sourcesoup = BeautifulSoup(sourceurl, 'html.parser')

	namenode = sourcesoup.find_all("h3", class_ = "package-name")
	if namenode == None:
		namenode = sourcesoup.find_all("header", class_ = "package-name")
	projectname = namenode[0].string
	projectname = projectname.lstrip().rstrip()
	
	sourcelabel = sourcesoup.find("b", string = "Source Code")
	if sourcelabel != None:
		giturl = sourcelabel.find_next_sibling("a").string
		giturl = giturl.lstrip().rstrip()
		document_name_url.write(projectname + "------" + giturl + "\n")
		document_url.write(giturl + "\n")
	else:
		document_name_url.write(projectname + " do not have direct source code url")

document.close()
document_name_url.close()
document_url.close()
