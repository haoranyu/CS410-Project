#encoding=utf-8

from mmseg import SEG
import codecs
import MySQLdb as mysql
from time import gmtime, strftime

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

def get_location(sentence,locList):
	loc_bit = [0]*len(sentence)
	loc_list = []
	oriSent = ""
	for spword in sentence:
		oriSent += spword
	oriSent += "\n"
	i = 0
	for i in range(len(sentence)):
		word = sentence[i]
		skip = 0
		for x in filterList:
			if x == word:
				skip = 1
		#for comm in commonList:
		if commonDict.has_key(word):
			#if comm[0:-1] == word:
			skip = 1
		if skip == 1:
			continue
		dirty = 0
		if len(word) < 2:
			continue
		if i != 0 and loc_bit[i-1] == 1:
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
				loc_bit[i] = 1
				loc_list.append(word)
				#print location[0:-1]
				#output.append(location[0:-1])
				#output.write(word)
				output.write("exact: "+word+" location: "+location + "----------original: "+oriSent)
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
					output.write(u"acronym: "+word+"  location: "+location+ "----------original: "+oriSent)

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
			#	print "bcombine "+words[j]
				combine += words[j]
				j += 1
				if j == len(words):
					break
			for z in xrange(len(combine)-1,-1,-1):
				com += combine[z]
			#print "combine "+combine
			for word_com in wordsList:
				if combine == word_com[0:-2]:
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
if __name__=="__main__":
	uid = " 2034233260"
	#uid = " 2147234363"
	output = codecs.open('TestOutput.txt'+strftime(" %Y-%m-%d %H:%M:%S", gmtime())+uid,'w','utf-8')
	#line = sys.argv[1]
	locList = codecs.open("locations.dic",'r','utf-8')
	#locLists = open("locations.dic",'r')
	locList = locList.readlines()	
	locDict = {}
	for item in locList:
		locDict[item] = 0
	commonList = codecs.open("geo_dict_main.dic",'r','utf-8')
	commonList = commonList.readlines()
	commonDict = {}
	for item in commonList:
		commonDict[item[0:-2]] = 0
	#if commonDict.has_key(u'香山'):
	#	print u"香山"
	#a = 0
	#while(1==1):
	#	a+=1
	wordsList = codecs.open("main.dic",'r','utf-8')
	wsrdsList = wordsList.readlines()
	db.query("""SELECT * FROM wb_post_beijing_8 WHERE uid = 2034233260 AND zf = 0""")
	#db.query("""SELECT * FROM wb_post_beijing_8 WHERE uid = 2147234363 AND zf = 0""")
	r = db.store_result()
	num = r.num_rows()
	print num
	i = 0
	while(i<num):
		line = r.fetch_row()
		a = line[0]
		#locationDic = {}
		#for locations in locLists:
#		ws = segment(locations)
		print a[7]
		sent = segment(a[7])
		get_location(sent, locList)
		i+=1
		#print abcde
