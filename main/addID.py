import sys
import codecs
from mmseg import SEG

seg = SEG()

fname = sys.argv[1]
output = codecs.open("IDLocations.dic",'w','utf-8')
little_dic = codecs.open("locations.dic",'w','utf-8')
f = codecs.open(fname,'r','utf-8')
lines = f.readlines()
i = 1
for line in lines:
	little_dic.write(str(i) + ","+ line)
	output.write(str(i)+", "+line)
	i+=1
