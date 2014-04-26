import MySQLdb as mysql

id = 3
while id < 8:
	iid = str(id)
	uidFile = open("../outputs/uid/uid"+iid+".txt",'w')
	db = mysql.connect(host="localhost",user="root",passwd="CrAcK146",db="weibo")
	db.query("select * from wb_post_beijing_"+iid)
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
	id+=1
