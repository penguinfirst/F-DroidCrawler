import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getGithubUrl(html)
	reg = ''

for i in range(2,3):
	pageurl = "https://f-droid.org/packages/" + str(i) + "/index.html"
	html = getHtml(pageurl)
	
