import requests
import os
import json
import time

document = open("f-droid.csv", "r")
des_doc = open("f-droid_native.csv", "a+")
target_doc = open("f-droid_target.csv", "a+")

i = 0
try:
	for line in document.readlines():
		i = i + 1
		if i < 357:
			continue	
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

		githuburl = "https://api.github.com/repos/" + midstr + "/git/trees/master?recursive=12&access_token=9fed5f2f0cceb1412577a79394d5fb8b7c2b24f1"
		
		reqs = requests.get(githuburl)
		if reqs.status_code == 404 :
			des_doc.write(appname + "," + "do not have master\n")
			continue

		procontent = reqs.json()	
		for obj in procontent["tree"]:
			if obj["type"] != "tree":
				filename = obj["path"]
				if filename.endswith(".cpp") or filename.endswith(".c") or filename.endswith(".cc"):
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

except:
	print "Program fails at " + str(i)

target_doc.close()
des_doc.close()		
document.close()
