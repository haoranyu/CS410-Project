#encoding=utf-8

import sys
from mmseg import SEG
import codecs
import MySQLdb as mysql

seg = SEG()

db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")

def segment(text):
	wlist = seg.cut(text)
	wlist.reverse()
	print " ".join(wlist)
	return wlist

def get_location(sentence,locList):
	loc_bit = [0]*len(sentence)
	for i in range(len(sentence)):
		word = sentence[i]
		if len(word) < 2:
			continue
		if i != 0 and loc_bit[i-1] == 1:
			continue
		for location in locList:
			if word == location[0:len(word)]:
				loc_bit[i] = 1
				print location[0:-1]
        
if __name__=="__main__":
	line = sys.argv[1]
	locList = codecs.open("locations.dic",'r','utf-8')
	locList = locList.readlines()
	sent = segment(line)
	get_location(sent, locList)
