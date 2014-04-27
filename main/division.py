import json
import codecs

#words = codecs.open('output.txt','r','utf-8')
words = open('output.txt','r')
words = words.readline()
words = json.loads(words)
for i in range(20):
	if i == 19:
		a = json.dumps(words[1900000:])
	else:
		a = json.dumps(words[100000*i:100000*(i+1)-1])
	wordsList = open('wordsList/wordsList_'+str(i), 'w')
	wordsList.write(a)
