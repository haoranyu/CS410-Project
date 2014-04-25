import codecs
import sys

cleanID = sys.argv[1]
raw = sys.argv[2]
raw = codecs.open(raw,'r','utf-8')
filt = [u"(",u")",u"-"," "]
raw = raw.readlines()
dic = {}
cleanID = codecs.open(cleanID,'w','utf-8')
for line in raw:
	i = 0
	for x in filt:
		if x in line:
			i = 1
	if (not dic.has_key(line)) and i == 0 and len(line) > 2:
		cleanID.write(line)
		dic[line] = len(line)
