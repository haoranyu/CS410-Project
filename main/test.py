#encoding=utf-8

from mmseg import SEG
import codecs
import MySQLdb as mysql
import re
import sys
import json
from datetime import datetime

seg = SEG()
db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")

def segment(text):
	wlist = seg.do_seg(text)
	#wlist = word_combine(wlist)
	wlist.reverse()
	#for thing in wlist:
	#	print thing
	#print "-----------------------------------------------------------------"
	wlist = word_combine(wlist)
	#print " ".join(wlist)
	return wlist

def word_combine(words):
	i = 0
	new_wlist = []
	while i < len(words):
		j = i
		jj = i
		combine = u""
		com = u""
		combit = 0
		if len(words[i]) == 1:
			while len(words[j]) == 1:
				combine += words[j]
				j += 1
				if j == len(words):
					break
			if wordsDic.has_key(combine):
				new_wlist.append(combine)
				combit = 1
			if combit == 0:
				new_wlist.append(words[jj])
		else:
			new_wlist.append(words[i])
		i += 1
	return new_wlist

def extract(iid):
	uidList = open("../outputs/uid/uid"+str(iid)+".txt",'r')
	uidList = uidList.readlines()
	uidDic = {}
	count = 0
	for uid in uidList:
		uid = uid[:-1]
		uidDic[uid[:-1]] = 0
		posts = open("../outputs/user_"+str(iid)+"/"+str(uid)+".txt")
		posts = posts.readlines()
		for post in posts:
			post = json.loads(post)	
			for each in post[1]:
				count += 1
				if len(each) > 1:
					if not dic.has_key(each):
						dic[each] = 1
					else:
						dic[each] += dic[each] + 1				
	print "finished at" + str(datetime.now())
	print "total: "+ str(len(dic))
	print "original: "+str(count)

if __name__=="__main__":
	wordsList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	wordsList = wordsList.readlines()
	wordsDic = {}
	for word in wordsList:
		ab = word[:-2]
		wordsDic[ab] = 0
	id = 1
	dic = {}
	while id < 9:
		extract(id)
		id+=1
	list = dic.keys()
	jason = json.dumps(list)
	output = codecs.open("output.txt",'w','utf-8')
	output.write(jason)
