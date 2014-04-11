import codecs
from mmseg import SEG

def segment(text):
	wlist = seg.do_seg(text)
	#wlist = word_combine(wlist)
	wlist.reverse()
	for thing in wlist:
		print thing
	print "-----------------------------------------------------------------"
	#wlist = word_combine(wlist)
	print " ".join(wlist)
	return wlist


#locations = codecs.open("geo_dict_locations.dic",'r','utf-8')
locations = open("geo_dict_locations.dic",'r')
common = codecs.open("geo_dict_main.dic",'r','utf-8')
locations = locations.readlines()
common = common.readlines()
seg = SEG()
for location in locations:
	print segment(location)

