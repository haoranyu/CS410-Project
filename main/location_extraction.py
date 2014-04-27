#encoding=utf-8

from mmseg import SEG
import codecs
import MySQLdb as mysql
from time import gmtime, strftime
import re
import sys

seg = SEG()

db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")
locations = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="wb_location")

filterList = [u'北京市',u'北京',u'人民',u'中国']
#filterList = []

def segment(text):
	wlist = seg.do_seg(text)
	wlist.reverse()
	for thing in wlist:
		print thing
	print "-----------------------------------------------------------------"
	wlist = word_combine(wlist)
	print " ".join(wlist)
	return wlist

def get_location(sentence, locDb):
	for i in range(len(sentence)-1):
		word = sentence[i]
		j = i+1
		word += sentence[j]
	#	locDb.query("select sname from wb_beijng_location where sname like'" +word+"'")
		if locationIdDic.has_key(word):	
			#lid = locationIdDic[word]
			locDb.query("select sname from wb_beijing_location where lid = "+str(lid))
			r = locDb.store_result()
			for i in range(r.num_rows()):
				print (r.fetch_row()[0])[0]
		else:
			if locationIdDic.has_key(sentence[i]):
				print "first"
				lid = locationIdDic[sentence[i]]
				locDb.query("select sname from wb_beijing_location where lid="+str(lid))
				print ("select sname from wb_beijing_location where lid="+str(lid))
				r = locDb.store_result()
				for i in range(r.num_rows()):
					print (r.fetch_row()[0])[0]

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

def freq_count(sen):
	sent_dict = {}
	weiboLength = 0
	wordCount = 0
	segWordCount = 0
	for word in sen:
		weiboLength += len(word)
		wordCount += 1
		if sent_dict.has_key(word):
			sent_dict[word] += 1
		else:
			sent_dict[word] = 1
	freq = u""
	for keys in sent_dict.keys():
		segWordCount += 1
		freq = freq + keys + ": " + str(sent_dict[keys]) + ", "
	return freq, str(segWordCount) + ", " + str(weiboLength) + ", " + str(wordCount)

if __name__=="__main__":
	testSentence = sys.argv[1]
	locList = codecs.open("dictionary/geo_dict_locations.dic",'r','utf-8')
	locList = locList.readlines()
	locations.query("select lid,sname from wb_beijing_location")
	locationIdDic = {}
	r = locations.store_result()
	num = r.num_rows()
	for i in range(num):
		line = r.fetch_row()[0]
		lid, sname = line[0], line[1]
		locationIdDic[sname.decode('utf-8')] = lid
	wordsList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	wordsList = wordsList.readlines()
	wordsDic = {}
	for word in wordsList:
		ab = word[:-2]
		wordsDic[ab] = 0
	sent = segment(testSentence)
	get_location(sent, locations)
