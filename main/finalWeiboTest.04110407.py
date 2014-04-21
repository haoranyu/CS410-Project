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

def get_location(sentence,locList,uidWid,co,wbLen):
	wbLocationsCount = 0
	loc_bit = [0]*len(sentence)
	loc_list = []
	oriSent = ""
	for spword in sentence:
		oriSent += spword
	oriSent += "\n"
	i = 0
	wordCountOutput = u""
	output.write("((( ")
	for i in range(len(sentence)):
		wordLocationsCount = 0
		word = sentence[i]
		skip = 0
		for x in filterList:
			if x == word:
				skip = 1
		if skip == 1:
			continue
		dirty = 0
		if len(word) < 2:
			continue
		if i != 0 and (loc_bit[i-1] == 1):
			continue
		for locs in loc_list:
			if len(locs) < len(word):
				continue
			if word == locs[0:len(word)]:
				dirty = 1
		if dirty == 1:
			continue
		for location in locList:
			if word == location[0:len(word)]:
				if len(location) > 2 * len(word) + 1:
					continue
				loc_bit[i] = 1
				loc_list.append(word)
				#output.write("exact: "+word+" location: "+location + "----------original: "+oriSent)
				wbLocationsCount += 1
				wordLocationsCount += 1
				output.write("["+word+","+location[:-1]+","+uidWid+", "+wbLen+", {"+co[0:-2]+"}],")
			else:
				i, j = 0, 0
				acronym = 0
				lengthOfWord = len(word)
				if word[0] != location[0]:
					continue
				if len(word) > len(location):
					continue
				if len(location) < len(word)*2:
					continue
				firstLoc = []
				prevI = -1
				currI = 0
				for ff in range(len(word)*2):
					firstLoc.append(location[ff])
				for i in range(len(word)):
					if word[i] in firstLoc:
						acronym += 1
						currI = firstLoc.index(word[i])
						if prevI > currI:
							acronym = len(word)+1
						prveI = currI
						firstLoc.remove(word[i])
				if currI < 4:
					acronym = len(word)+1
				if acronym == len(word):
					loc_bit[i] = 1
					#output.write(u"acronym: "+word+"  location: "+location+ "----------original: "+oriSent)
					output.write("["+word+","+location[:-1]+","+uidWid+", "+wbLen+", {"+co[0:-2]+"}],")
					wbLocationsCount += 1
					wordLocationsCount += 1
		if wordLocationsCount > 0:
			#output.write(word+" generates "+str(wordLocationsCount) + " locations\n")
			wordCountOutput += (word + ": " + str(wordLocationsCount) + "; ")
	#output.write("Original Weibo: "+ oriSent + "\nTotal Locations found: " + str(wbLocationsCount) + "\n")
	output.write(" ))), {"+wordCountOutput+"}, "+ str(wbLocationsCount)+"\n\n")
	#output.write("\n"+oriSent[0:-2]+": " + str(wbLocationsCount)+"\n")
	#output.write("@_@---------------------------------------------------------------------------@_@\n")

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
	uid = str(sys.argv[1])
	output = codecs.open('../outputs/output.txt.'+strftime("%Y-%m-%d,%H:%M:%S,", gmtime())+uid,'w','utf-8')
	locList = codecs.open("dictionary/locations.dic",'r','utf-8')
	locList = locList.readlines()
	locDict = {}
	for item in locList:
		locDict[item] = 0
	commonList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	commonList = commonList.readlines()
	commonDict = {}
	for item in commonList:
		commonDict[item[0:-2]] = 0
	wordsList = codecs.open("dictionary/main.dic",'r','utf-8')
	wordsList = wordsList.readlines()
	db.query("SELECT * FROM wb_post_beijing_8 WHERE uid = "+uid+" AND zf = 0")
	#query = ("SELECT * FROM wb_post_beijing_8 WHERE uid = %s AND zf = 0")
	r = db.store_result()
	num = r.num_rows()
	print num
	i = 0
	while(i<num):
		line = r.fetch_row()
		a = line[0]
		print a[7]
		query = a[7]
		uw = a[0]+","+a[2]
		line = re.sub(r'href=[\'"]?([^\'" >]+)',"",query)
		line = re.sub(r'((&lt;a)|(target=&quot;_blank&quot;)|(&gt;))', '', line)
		sent = segment(line)
		for each in sent:
			if each == '':
				sent.remove(each)
		c,weiboLen = freq_count(sent)
		get_location(sent, locList, uw, c,weiboLen)
		i+=1
		#print abcde
	linesOutput = output.readlines()
	for lineO in linesOutput:
		if lineO[0:8] == "(((  )))":
			continue
		else:
			output.write(lineO)
