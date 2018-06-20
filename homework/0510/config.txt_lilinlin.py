file = open('C:/Users/Administrator/Desktop/config.txt','w')
file.write("usernae=xiaoming\n")
file.write("password=123456\n")
file.write("mobile=15818646666\n")
file.close()
file = open('C:/Users/Administrator/Desktop/config.txt','r')
configdict = {}
content_list = file.readlines()
for each_line in content_list:
    spilt_list = each_line.split("=")
    if spilt_list[0] =="password":
        configdict[spilt_list[0]] = "654321"
        content_list[content_list.index(each_line)] =  "password=654321\n"
    else:
        configdict[spilt_list[0]] = spilt_list[1][:-1]
print(configdict)
print(content_list)
file.seek(0)
#file.writelines(content_list)
file.close()