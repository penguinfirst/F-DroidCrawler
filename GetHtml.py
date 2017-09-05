import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

for i in range(2,4):
	pageurl = "https://f-droid.org/packages/" + str(i) + "/index.html"
	html = getHtml(pageurl)
	print html
	print "**********************************************"
