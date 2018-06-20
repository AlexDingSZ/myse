import pymysql
dbconfig={"host":"localhost","port":3306,"user":"root","password":"123456","database":"testdb"}
db = pymysql.connect(**dbconfig)
cursor = db.cursor()
sql = "update user set id = 6,name ='aaaa' where name ='aaa'"
result = cursor.execute(sql)
db.commit()
cursor.close()
db.close()