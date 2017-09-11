import requests
import os
import json
import time

document = open("f-droid_native_mk.csv", "r")
des_doc = open("f-droid_native_addition.csv", "w+")
target_doc = open("f-droid_target_addition.csv", "w+")


for line in document.readlines():

	temp = line
	con_c = False

	appname = line.split(",")[0]
	giturl = line.split(",")[5].strip()
	if giturl.find("github") != -1:
		tempstr = giturl.split("/")
		midstr = tempstr[len(tempstr)-2] + "/" + tempstr[len(tempstr)-1];

	githuburl = "https://api.github.com/repos/" + midstr + "/git/trees/master?recursive=12"
	
	reqs = requests.get(githuburl)

	procontent = reqs.json()	
	for obj in procontent["tree"]:
		if obj["type"] != "tree":
			filename = obj["path"]
			if filename.endswith(".c"):
				con_c = True
	
	des_doc.write(temp.strip() + "," + str(con_c) + "\n")	
	
	if con_c == True:
		target_doc.write(appname + "," + giturl + "\n")

des_doc.close()
target_doc.close()	
document.close()
