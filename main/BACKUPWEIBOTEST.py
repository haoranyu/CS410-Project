#encoding=utf-8

from mmseg import SEG
import codecs
import MySQLdb as mysql
from time import gmtime, strftime
import re
import sys

seg = SEG()

db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")

filterList = [u'北京市',u'北京',u'人民',u'中国']
#filterList = []

def segment(text):
	wlist = seg.do_seg(text)
	#wlist = word_combine(wlist)
	wlist.reverse()
	for thing in wlist:
		print thing
	print "-----------------------------------------------------------------"
	wlist = word_combine(wlist)
	print " ".join(wlist)
	return wlist

def get_location(sentence,dic_list):
	for x in sentence:
		if commonDict.has_key(x):
			print "common"+x
			#continue
		leng = len(x)
		if leng == 1:
			continue
		i = 0
		while dic_list[leng-2].has_key(x+" "+str(i)):
			print (dic_list[leng-2])[x+" "+str(i)]
			i+=1
def word_combine(words):
	i = 0
	new_wlist = []
	while i < len(words):
		j = i
		combine = u""
		com = u""
		combit = 0
		if len(words[i]) == 1:
			while len(words[j]) == 1:
				print "bcombine "+words[j]
				combine += words[j]
				j += 1
				if j == len(words):
					break
			for z in xrange(len(combine)-1,-1,-1):
				com += combine[z]
			#print "combine "+combine
			for word_com in wordsList:
				if len(word_com)<len(combine):
					continue
				if combine == word_com[0:len(combine)]:
					new_wlist.append(combine)
					combit = 1
					break
			if combit == 0:
				for k in xrange(len(com)-1,-1,-1):
					new_wlist.append(com[k])
			i = j-1
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
	uid = sys.argv[1]
	locList = codecs.open("dictionary/geo_dict_locations.dic",'r','utf-8')
	locList = locList.readlines()
	LOC = codecs.open("dictionary/location_list.dic",'w','utf-8')
	locDictList = []
	for i in range(5):
		locDictList.append({})
	for item in locList:
		print locList.index(item)
		length = 5
		if len(item) < 7:
			length = len(item) - 1
		for i in range(length):
			j = 0
			while locDictList[i].has_key(item[:i+2]+codecs.encode(" "+str(j),'utf-8')):
				j += 1
			(locDictList[i])[item[:i+2]+codecs.encode(" "+str(j),'utf-8')] = item[:-1]
	LOC.write(str(locDictList[0]))
	LOC.write(str(locDictList[1]))
	LOC.write(str(locDictList[2]))
	LOC.write(str(locDictList[3]))
	LOC.write(str(locDictList[4]))
	commonList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	commonList = commonList.readlines()
	commonDict = {}
	for item in commonList:
		commonDict[item[0:-2]] = 0
	wordsList = codecs.open("dictionary/main.dic",'r','utf-8')
	wordsList = wordsList.readlines()
	sent = segment(uid)
	get_location(sent, locDictList)
