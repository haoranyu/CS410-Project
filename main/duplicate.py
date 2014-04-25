#encoding=utf-8
import codecs
import sys
ra = sys.argv[1]
raw = codecs.open(ra, 'r', 'utf-8')
raw = raw.readlines()
output = codecs.open(ra,'w','utf-8')
dic = {}
c = 0
ori = 0
for x in raw:
	ori += 1
	if not dic.has_key(x):
		output.write(x)
		dic[x] = len(x)-1
		c += 1
print "Dictionary has "+str(c)+" words and has "+str(ori-c)+" duplicates"

