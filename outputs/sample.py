#encoding=utf8

import json
import codecs
import glob

i = 0
skip = 0
output = codecs.open('samples.txt','w','utf-8')
dic = open('location_list/location.dic','r')
dic = dic.readlines()
dictionary = {}
for word in dic:
	word = json.loads(word)
	dictionary[word[0]] = word[1]
print dictionary.keys()
j = 146
for filename in glob.glob('post_all/*.txt'):
	if j%11 != 0:
		print "no"
		j+=1
		continue
	posts = open(filename,'r')
	posts = posts.readlines()
	for post in posts:
		x = u''
		post = json.loads(post)
		print post
		skip = 0
		for word in post[1]:
			if dictionary.has_key(word):
				x += word+", "
				#output.write(line)
				#output.write("\n")
				print str(post[0]) +": "+str(i)
				if skip == 0:
					i+=1
				skip = 1
			if i == 1000:
				print 'done'
				while 1 == 1:
					i+=1
		if skip==1:
			output.write(x+": ")
			for x in post[1]:
				output.write(x)
				output.write(" ")
			output.write('\n')
	j+=1
