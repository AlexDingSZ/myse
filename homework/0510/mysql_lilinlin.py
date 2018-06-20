import pymysql
dbconfig = {"host":"localhost","port":3306,"user":"root","password":"123456","database":"testdb" }
db=pymysql.connect(**dbconfig)

cursor = db.cursor()
sql = "select * from user "
result = cursor.execute(sql)
result_dict = cursor.fetchall()
print(result_dict)
cursor.close()
db.close()