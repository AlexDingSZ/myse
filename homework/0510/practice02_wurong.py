#以写的模式打开，覆盖原文件
f = open("config.txt","w")

#截取文件到最大的size
f.truncate(0)

#写文件（写入类型为字符串）
f.write("username=xiaoming ")
f.write("password=123456 ")
f.write("mobile=15818646666")

#关闭文件
f.close()

#以读写的模式打开文件
f = open("config.txt","r+")

#读取所有内容，每一行为一个元素，返回读取的字节
content_str = f.readline()

#将读取的字节转换为列表
content_list1 = content_str.split()

f_dict = {}
for each_value in content_list1:
    split_list = each_value.split("=")
    if split_list[0] == "password":
        f_dict[split_list[0]] = "654321"
        # print(content_list1.index(each_value))
        # i = content_list1.index(each_value)
        # content_list1[i] = "password=654321"
        # print(content_list1[i])
        content_list1[content_list1.index(each_value)] = "password=654321"
    else:
        f_dict[split_list[0]] = split_list[1]
print(f_dict)
print(content_list1)

#移动光标
f.seek(0)
f.truncate()

content_str1 = content_str.replace("123456","654321")
content_str2 = content_str1.replace(" ","\n")

#列表写入
f.writelines(content_str2)
f.close()
