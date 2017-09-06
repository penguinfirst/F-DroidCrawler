import os

src_doc_url = open("f-droid_app.txt", "r")
src_doc_name = open("f-droid_name_url.txt", "r")
des_doc = open("f_droid.csv", "w+")

def main():
	for line in src_doc_url.readlines():	
		info = src_doc_name.readline()
		appname = info.split("------")[0]
		giturl = info.split("------")[1]
		des_doc.write(appname + "," + line.strip() + "," + giturl.strip() + "\n")
	src_doc_url.close()
	src_doc_name.close()
	des_doc.close()

main()
