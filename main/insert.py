#coding:utf-8

import codecs
import sys
import math
import MySQLdb as mysql
#sys.setdefaultencoding('utf-8')

def distance((lat1,lon1),(lat2,lon2)):
	return math.fabs(math.fabs(lat1-lat2)+math.fabs(lon1-lon2))

#db1, db2 = sys.argv[1],sys.argv[2]
db1= (sys.argv[1]).encode('utf-8')
maxDis = 0.0035
dic = {}
c = 0
ori = 0

db1 = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db=db1)
db1.query("select * from wb_beijing_location")
#db2 = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db=db2)
#db2.query("select * from wb_beijing_location")
db3 = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="wb_beijing_location")
r1 = db1.store_result()
#r2 = db2.store_result()

num = r1.num_rows()
for i in range(num):
	ori+=1
	line = (r1.fetch_row())[0]
	lname = line[1]
	sname = ((codecs.decode(line[2],'utf-8')).lower()).encode('utf-8')
	saddr = line[3]
	lat, lon = line[4], line[5]
	j = 0
	skip = 0
	while dic.has_key(sname + codecs.encode(" "+str(j),'utf-8')):
		dis = distance(dic[sname+codecs.encode(" "+str(j),'utf-8')],(lat,lon))
		if dis <= maxDis:
			print "OFF"+str(i) + "-> "+sname+": "+str(dis)
			skip = 1
			c += 1
			break
		j += 1
	if skip == 0:
		dic[sname+" "+str(j)] = (lat,lon)
		#print "insert into wb_beijing_location ('lname', 'sname', 'saddr', 'lat', 'long') VALUES ("+lname+","+sname+","+saddr+","+str(lat)+", "+str(lon)+")"

		#db3.query("insert into wb_beijing_location ('lname', 'sname', 'saddr', 'lat', 'long') VALUES ('"+"hi"+"','"+"hello"+"','"+saddr+"',"+str(lat)+", "+str(lon)+")")
	print "INSERT INTO `wb_beijing_location`(`lname`, `sname`, `saddr`, `lat`, `lon`) VALUES ('"+lname+"','"+sname+"','"+saddr+"',"+str(lat)+","+str(lon)+")"
	db3.query("INSERT INTO `wb_beijing_location`(`lname`, `sname`, `saddr`, `lat`, `lon`) VALUES ('"+lname+"','"+sname+"','"+saddr+"',"+str(lat)+","+str(lon)+")")
		#db3.query("insert into wb_beijing_location (lname sname saddr lat lon) VALUES ("+lname.encode('utf-8')+","+sname.encode('utf-8')+","+saddr.encode('utf-8')+","+lat.encode('utf-8')+","+lon.encode('utf-8')+")")
		
print ori
print c
print len(dic)
