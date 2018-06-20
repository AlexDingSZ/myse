#创建一个config。txt文件，w为权限
f = open("config.txt","w")
#文件写入字符串
f.write("username=xiaoming\n")
f.write("password=123456\n")
f.write("mobile=1581864666\n")
f = open("config.txt","r+")
content_list = f.readlines()
print (content_list)
a_dict = {}
for eachvalue in content_list:
    split_list= eachvalue.split("=")
    print(split_list)
    if  split_list[0]=="password":
        a_dict[ split_list[0]]="654321"
        content_list[content_list.index(eachvalue)]="password=654321\n"
    else:
        a_dict[split_list[0]]= split_list[1][:-1]
        print(a_dict)
f.seek(0)
f.truncate()
f.writelines( content_list)
f.close()



# dict ={}
# for line in f.readline():
#     a = line.split("=")
#     if a[0]=="password":
#         dict[a[0]]=="654321"
#         a[a.index(line)]="password=654321\n"
#     else:
#         dict[a[0]]=a[0][:-1]
#         print d