import requests
import os
import json

document = open("f_droid.csv", "r")
des_doc = open("f-droid_native.csv", "w+")
target_doc = open("f-droid_target.csv", "w+")

i = 0
for line in document.readlines():
	"""i = i + 1
	if i > 4:
		break
	"""
	con_cpp = False
	con_mk = False
	con_cmake = False
	con_java = False

	appname = line.split(",")[0]
	giturl = line.split(",")[2].strip()
	if giturl.find("github") != -1:
		tempstr = giturl.split("/")
		midstr = tempstr[len(tempstr)-2] + "/" + tempstr[len(tempstr)-1];
	else:
		des_doc.write(appname + "," + "not in Github\n")
		continue

	githuburl = "https://api.github.com/repos/" + midstr + "/git/trees/master?recursive=12"
	procontent = requests.get(githuburl).json()	
	for obj in procontent["tree"]:
		if obj["type"] != "tree":
			filename = obj["path"]
			if filename.endswith(".cpp"):
				con_cpp = True
			if filename.endswith(".mk"):
				con_mk = True
			if filename.find("CMakeLists.txt") != -1:
				con_cmake = True
			if filename.endswith(".java"):
				con_java = True
	
	des_doc.write(appname + "," + str(con_cpp) + "," + str(con_mk) + "," + str(con_cmake) + "\n")	
	
	if con_cpp == True and (con_mk == True or con_cmake == True):
		target_doc.write(appname + "," + giturl + "\n")

target_doc.close()
des_doc.close()		
document.close()
