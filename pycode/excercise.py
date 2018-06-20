f = open("config.txt","r+")
f.truncate(0)
f.write("username=xiaoming\n")
f.write("password=123456\n")
f.write("mobile=15818646666\n")
f.close()
f = open("config.txt","r+")
configdict = {}
content_list=f.readlines()
for each_line in content_list:
    spilt_list = each_line.split("=")
    if spilt_list[0] == "password":
        configdict[spilt_list[0]] = "654321"
        content_list[content_list.index(each_line)] = "password=654321\n"
    else:
        configdict[spilt_list[0]] = spilt_list[1][:-1]
print(configdict)
print(content_list)
f.seek(0)
f.truncate()
f.writelines(content_list)
f.close()

{'username': 'xiaoming', 'password': '654321', 'mobile': '15818646666'}
['username=xiaoming\n', 'password=654321\n', 'mobile=15818646666\n']