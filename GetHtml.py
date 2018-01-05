import os
import re
import requests
from bs4 import BeautifulSoup

document = open("f-droid_app.txt", "w+")

for i in range(1,48):
	if i == 1:
	    pageurl = "https://f-droid.org/packages/"
	else:
	    pageurl = "https://f-droid.org/packages/" + str(i) + "/index.html"
	html = requests.get(pageurl).content
	soup = BeautifulSoup(html, 'html.parser')
	searcharea = soup.find("div", class_ = "article-area")
	incomplete_url = searcharea.find_all("a", class_ = "package-header")
	for link in incomplete_url:
		url = "https://f-droid.org" + link.get('href')
		document.write(url + "\n");
document.close()

