#encoding=utf8

import json
import codecs
import glob

i = 0
skip = 0
x = u''
output = codecs.open('samples.txt','w','utf-8')
dic = open('location_list/location.dic','r')
dic = dic.readlines()
dictionary = {}
for word in dic:
	word = json.loads(word)
	dictionary[word[0]] = word[1]
print dictionary.keys()
for filename in glob.glob('user_1/*.txt'):
	posts = open(filename,'r')
	posts = posts.readlines()
	for post in posts:
		post = json.loads(post)
		skip = 0
		for word in post[1]:
			if dictionary.has_key(word):
				x = word
				#output.write(line)
				#output.write("\n")
				print str(post[0]) +": "+str(i)
				skip = 1
				i+=1
			if i == 1000:
				print 'done'
				while 1 == 1:
					i+=1
			if skip == 1:
				break
		if skip==1:
			output.write(x+": ")
			for x in post[1]:
				output.write(x)
			output.write('\n')