#encoding=utf-8
import codecs
import sys
import math
import MySQLdb as mysql
def distance((lat1,lon1),(lat2,lon2)):
	return math.fabs(math.fabs(lat1-lat2)+math.fabs(lon1-lon2))

#database,n,s,e,w = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
database = sys.argv[1]
output = open('beijing_range.txt','w')
N,S,W,E = 41.10, 39.50, 115.50, 117.35
#omid,obs,oup,odown = 0,0,1,1
#amid,abs,aup,adown = 1,1,1,1
maxDis = 0.0035
dic = {}
c = 0
#ori = 0
#x = 0
mid = 0

#for j in range(20):
#	omid,obs,oup,odown = 0,0,1,1
#	amid,abs,aup,adown = 1,1,1,1
#	for z in range(20):	
db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db=database)
db.query("select * from wb_beijing_location order by lat")
r = db.store_result()
num = r.num_rows()
for i in range(num):
#	ori+=1
	line = (r.fetch_row())[0]
	lid = str(line[0])
	name = ((codecs.decode(line[2],'utf-8')).lower()).encode('utf-8')
	addr = line[3]
	#if '?'in name:
	#	name = name.replace('?','')
	lat, lon = line[4], line[5]
	#j = 0
	skip = 0
	#while dic.has_key(name + codecs.encode(" "+str(j),'utf-8')):
	if lat > N or lat < S:
		skip = 1
	if lon > E or lon < W:
		skip = 1
	if "北京" in name or "北京" in addr:
		skip = 0
	if skip == 1:
		c += 1
		print str(i)+"<-"+name+": "+str(lat)+", "+str(lon)
		#dis = distance(dic[name+codecs.encode(" "+str(j),'utf-8')],(lat,lon))
				#print str(i)+"<-"+name+": "+str(dis)
				#if dis <= maxDis:
					#if dis >= 0.0035:
					#if j != 0:
		#db.query("delete from wb_beijing_location where lid = '"+lid+"'")
				#	print "OFF"+str(i) + "-> "+name+": "+str(dis)
print c
				#	skip = 1
				#	c += 1
				#	break
				#j += 1
			#if skip == 0:
				#dic[name+" "+str(j)] = (lat,lon)
		#print ori
#		output.write(str(c) + "<-"+str(n)+", "+str(s)+", "+str(e)+", "+str(w))
#		print (str(c) + "<-"+str(n)+", "+str(s)+", "+str(e)+", "+str(w))
#		print omid
#		#print len(dic)
#		if (n == 41.1) and (s == 39.4):
#			print "omid"
#			omid = 0
#			n = N
#			s = S
#		elif n == 39.9 and s == 39.6:
#			print "obs"
#			obs = 0
#			n = N
#			s = S
#		elif n == 39.9 and s == 39.4:
#			print "oup"
#			oup = 0
#			n = N
#			s = S
#		if omid == 1:
#			n+=0.02
#			s-=0.02
#		elif obs == 1:
#			n-=0.02
#			s+=0.02
#		elif oup == 1:
#			n-=0.02
#			s-=0.02
#		elif odown == 1:
#			n+=0.02
#			s+=0.02
#
#	if e == (E+0.1) and w == (W-0.1):
#		print "amid"
#		amid = 0
#		e = E
#		w = W
#	elif e == (E-0.1) and w == (W+0.1):
#		print "abs"
#		abs = 0
#		e = E
#		w = W
#	elif e == (E-0.1) and w == (W-0.1):
#		print "aup"
#		aup = 0
#		e = E
#		w = W
#	if amid == 1:
#		e+=0.02
#		w-=0.02
#	elif abs == 1:
#		e-=0.02
#		w+=0.02
#	elif aup == 1:
#		e-=0.02
#		w-=0.02
#	elif adown == 1:
#		e+=0.02
#		w+=0.02
#
