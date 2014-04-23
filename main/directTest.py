#encoding=utf-8

import sys
from mmseg import SEG
import codecs

seg = SEG()

#filterList = [u'北京市',u'北京',u'朝阳区']
filterList = []

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
	i = 0
	for i in range(len(sentence)):
		word = sentence[i]
		skip = 0
		for x in filterList:
			if x == word:
				skip = 1
		if skip == 1:
			continue
		dirty = 0
		if len(word) < 3:
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
				print location[0:-1]

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
	line = sys.argv[1]
	locList = codecs.open("dictionary/geo_dict_locations.dic",'r','utf-8')
	#locLists = open("locations.dic",'r')
	locList = locList.readlines()	
	wordsList = codecs.open("dictionary/geo_main.dic",'r','utf-8')
	wsrdsList = wordsList.readlines()
	#locationDic = {}
	#for locations in locLists:
#		ws = segment(locations)
	sent = segment(line)
	get_location(sent, locList)
