#encoding=utf-8

import codecs
import sys

filter_list = [u'北京市',u'北京']
protect_list = [u'北京站']

fname = sys.argv[1]
raw = codecs.open(fname, 'r', 'utf-8')
raw = raw.readlines()
for i in range(len(raw)):
	skip = 0
	for y in protect_list:
		if y in raw[i]:
			skip = 1
	if skip == 1:
		continue
	for y in filter_list:
		if y in raw[i]:
			print (raw[i])[:-1] + "   "
			raw[i] = raw[i].replace(y,'')
			print raw[i]
