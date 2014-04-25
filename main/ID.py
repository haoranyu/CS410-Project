#encoding=utf-8

import sys
from mmseg import SEG
import codecs

seg = SEG()
filterList = [u'北京市',u'北京',u'朝阳区']

def segment(text):
	wlist = seg.do_seg(text)
	wlist.reverse()
	wlist = word_combine(wlist)

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
		if len(words[i]) == 1:
			while len(words[j]) == 1:
				combine += words[j]
				j += 1
				if j == len(words):
					break
				if len(combine) < 5:
					print combine
					#new_wlist.append(combine)
					output.write(combine+"\n")
			#i = j-1
		else:
			z = i
			combined = u""
			while len(combined) < 5:
				if len(combined) + len(words[z]) > 5:
					break
				combined += words[z]
				if z != len(words) -1:
					z += 1
				else:
					break
			output.write(combined+"\n")
		i += 1
	return new_wlist
if __name__=="__main__":
	out = sys.argv[1]
	locList = codecs.open("dictionary/geo_dict_locations.dic",'r','utf-8')
	locList = locList.readlines()	
	wordsList = codecs.open("dictionary/geo_dict_main.dic",'r','utf-8')
	wsrdsList = wordsList.readlines()
	standby = open('dictionary/geo_dict_locations.dic','r')
	standby = standby.readlines()
	output = codecs.open(out,'w','utf-8')
	for one in standby:
		segment(one)
