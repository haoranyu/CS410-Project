import sys
import glob
import codecs

fileList = glob.glob("geo*")
fileList = ["geo_"]
output = codecs.open("location.dic",'a','utf-8')
for fname in fileList:
	part  = open(fname, 'r')
	lines = part.readlines()
	for line in lines:
		print line
		output.write(line.decode("utf-8"))
