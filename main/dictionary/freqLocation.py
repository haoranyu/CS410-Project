#encoding=utf-8

import codecs

commonDic = codecs.open("geo_dict_main.dic",'r','utf-8')
commonDic = commonDic.readlines()
locationDic = codecs.open('geo_dict_locations.dic','r', 'utf-8')
locationDic = locationDic.readlines()
cleanedDic = codecs.open("cleaned.dic",'w','utf-8')

threshold = 5
C = 0
i = 0
filterList = {u"北京",u"北京市",u"中国",u"人民"}

for cw in commonDic:
	if i % 100 == 0:
		print i
	count = 0
	if cw in filterList:
		continue
	for lw in locationDic:
		if cw in lw:
			count+=1
	if count>threshold:
		print cw
		C += 1
	else:
		cleanedDic.write(cw)
	i+=1
print C
