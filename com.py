import sys
import glob
import codecs

fileList = glob.glob("geo_dict*")
output = codecs.open("geo_main.dic",'a','utf-8')
for fname in fileList:
	part  = open(fname, 'r')
	lines = part.readlines()
	for line in lines:
		print line
		output.write(line.decode("utf-8"))
