﻿#encoding=utf-8

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
	for uid in uidList:
		uidDic[uid[:-1]] = 0
	#user = codecs.open("../outputs/user_"+str(iid)+"/"+uid+".txt",'w','utf-8')
	db.query("SELECT * FROM wb_post_beijing_"+str(iid))
	r = db.store_result()
	num = r.num_rows()
	#print num
	print datetime.now()
	i = 0
	while(i<num):
		line = (r.fetch_row())[0]
		query = line[7]
		uid = line[2]
		#print str(uid) + "  " + str(datetime.now())
		wid = line[0]
		time = line[3]
		user = codecs.open("../outputs/user_post/user_"+str(iid)+"/"+str(uid)+".txt",'a','utf-8')
		line = re.sub(r'href=[\'"]?([^\'" >]+)',"",query)
		line = re.sub(r'(&lt;(.*?)&gt;)|(&amp;quot;(.*?)&amp;quot;)', '', line)
		line = re.sub(r'http://\S+', '', line)
		sent = segment(line)
		for each in sent:
			if each == '':
				sent.remove(each)
		seg_sentence = [wid,sent,time]
		seg_sentence = json.dumps(seg_sentence)
		user.write(seg_sentence+"\n")
		i+=1
		user.close()
	print "finished at" + str(datetime.now())

if __name__=="__main__":
	wordsList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	wordsList = wordsList.readlines()
	wordsDic = {}
	for word in wordsList:
		ab = word[:-2]
		wordsDic[ab] = 0
	id = 8
	while id < 9:
		extract(id)
		id+=1
