#encoding=utf-8
#import psyco
#psyco.full()

import sys
from mmseg import SEG
seg = SEG()

def segment(text):
    wlist = seg.cut(text)
    wlist.reverse()
    print " ".join(wlist)
        
if __name__=="__main__":
	test = sys.argv[1]
	test = open(test, 'r')
	lines = test.readlines()
	for line in lines:
		segment(line)
