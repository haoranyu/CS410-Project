import MySQLdb as mysql

uidFile = open("uid.txt",'w')
db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")
db.query("select * from wb_post_beijing_8")
r = db.store_result()
num = r.num_rows()
uidList = {}

for i in range(num):
	row = (r.fetch_row())[0]
	uid = row[2]
	if not uidList.has_key(uid):
		print uid
		uidList[uid] = 1
		uidFile.write(uid+'\n')
	else:
		uidList[uid] = uidList[uid]+1
