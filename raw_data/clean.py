import sys
import codecs
import glob

for raw in glob.glob("geo*"):
	clean = "clean/"+raw+".clean"
	raw = open(raw, 'r')
	clean = codecs.open(clean,'w','utf-8')
	lines = raw.readlines()
	for line in lines[1:]:
		line = line.decode('utf-8', 'ignore')
		if ('(' in line) and not(')' in line):
			mainBody = (line[0:line.index('(')])
			clean.write(mainBody)
		else:
			clean.write(line)
