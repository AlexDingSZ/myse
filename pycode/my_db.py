import  pymysql
dbconfig={"host":"localhost",
          "port":3306,
          "user":"root",
          "password":"666666",
          "database":"testdb"
          }
#db = pymysql.connect("localhost","root","666666","testdb")
db = pymysql.connect(**dbconfig)
cursor = db.cursor()
#sql = 'INSERT INTO USER (id,NAME) VALUES(2,"Rose")'
sql = 'INSERT INTO USER (id,NAME) VALUES(%d,"%s")' % (22,"haha")

cursor.execute(sql)
db.commit()
db.close()

import  pymysql
dbconfig={"host":"localhost",
          "port":3306,
          "user":"root",
          "password":"666666",
          "database":"testdb"
          }
db = pymysql.connect(**dbconfig)
cursor = db.cursor()
sql = "select * from user"
result = cursor.execute(sql)
result_tuple = cursor.fetchall()
print(result_tuple)
cursor.close()
db.close()


import  pymysql
dbconfig={"host":"localhost",
          "port":3306,
          "user":"root",
          "password":"666666",
          "database":"testdb"
          }
db = pymysql.connect(**dbconfig)
cursor = db.cursor()
sql = "update user set id = 6 , name ='aaa' where name ='haha' "
result = cursor.execute(sql)
db.commit()
cursor.close()
db.close()