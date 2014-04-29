#encoding=utf-8

import codecs
import MySQLdb as mysql
from time import gmtime, strftime
import sys
import json

locations = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="wb_location", charset = 'utf8')

if __name__=="__main__":
	wordsList = open('wordsList/wordsList_9','r')
	wordsList = wordsList.readline()
	wordsList = json.loads(wordsList)
	output = open('location_9.txt','a')
	conn = locations.cursor()
	i = 85000
	leng = len(wordsList)
	#for word in wordsList:          #starting from 52243
	while i < leng:
		word = wordsList[i]
		conn.execute(u"select lid from wb_beijing_location where sname like %s",(u'%'+word+u'%',))
		r = conn.fetchall()
		if len(r)>0:
			r = list(r)
			for j in range(len(r)):
				r[j] = int(r[j][0])
			result = [word,r]
			print i
			result = json.dumps(result)
			output.write(result)
			output.write('\n')
		i += 1
	
	wordsList = open('wordsList/wordsList_10','r')
	wordsList = wordsList.readline()
	wordsList = json.loads(wordsList)
	output = open('location_10.txt','w')
	conn = locations.cursor()
	i = 0
	#leng = len(wordsList)
	for word in wordsList:          #starting from 52243
	#while i < leng:
		conn.execute(u"select lid from wb_beijing_location where sname like %s",(u'%'+word+u'%',))
		r = conn.fetchall()
		if len(r)>0:
			r = list(r)
			for j in range(len(r)):
				r[j] = int(r[j][0])
			result = [word,r]
			print i
			result = json.dumps(result)
			output.write(result)
			output.write('\n')
		i += 1
