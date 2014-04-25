import codecs
import sys

raw= sys.argv[1]
output = raw[:-3]+"dic"
raw = codecs.open(raw,'r','utf-8')
#raw = open(raw,'r')
output = codecs.open(output,'w','utf-8')

lines = raw.readlines()
for line in lines:
	print line
	word = (line.split(' '))[1]
	print word
	output.write(word)
