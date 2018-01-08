import os
import sys

document_name_url = open("f-droid_name_url.txt", "a")
document_url = open("f-droid_url.txt", "a")


reload(sys)
sys.setdefaultencoding("utf-8")

for i in range(1,8):
    document1 = open("f-droid_name_url_" + str(i) + ".txt", "r")
    document2 = open("f-droid_url_" + str(i) + ".txt", "r")

    for url in document1.readlines():
	document_name_url.write(url)

    for url in document2.readlines():
	document_url.write(url)

    document1.close()
    document2.close()

document_name_url.close()
document_url.close()
