import  pymysql
dbconfig={"host":"localhost",
          "port":3306,
          "user":"root",
          "password":"123456",
          "database":"testdb"
          }
db = pymysql.connect(**dbconfig)
cursor = db.cursor()
sql = "update user set id = 15 , name ='aaa' where name ='haha' "
result = cursor.execute(sql)
db.commit()
cursor.close()
db.close()

# 插入
#insert into user(id,name) VALUES(17,"1717")
#查询
#select * from user
#修改
# update user set name='111',id = 16 where id =15
#删除
#delete from user where id =15