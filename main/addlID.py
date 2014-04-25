#encoding=utf-8
import codecs
import sys
import math
import MySQLdb as mysql

database = sys.argv[1]
db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db=database)
db.query("select * from wb_beijing_location")
r = db.store_result()
num = r.num_rows()
i = 1
while i < num:
	line = (r.fetch_row())[0]
	lid = str(line[0])
	print i
	db.query("UPDATE wb_beijing_location SET lid="+str(i)+" WHERE lid = "+lid)
	i+=1
