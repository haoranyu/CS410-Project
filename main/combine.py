import codecs
import sys

a = sys.argv[1]
af = codecs.open(a,'r','utf-8')
c = codecs.open("dictionary/geo_beijing_area.dic",'a','utf-8')

af = af.readlines()
print a+": "+str(len(af))
dic = {}
count = 0
fiveCount = 0
for x in af:
	if not dic.has_key(x):
		dic[x] = len(x)
		count += 1
		c.write(x)
		if len(x)<7:
			fiveCount += 1
print "total: "+str(count)+" words<6: "+str(fiveCount)
