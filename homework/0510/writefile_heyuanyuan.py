#coding:utf-8


configdict={}
file_w=open("config.txt","w")
file_w.truncate(0)
file_w.writelines(["username=xiaoming\n","password=123456\n","mobile=15818646666\n"])
print (file_w)
file_w.close()
file_w=open("config.txt","r")
file_r=file_w.readlines()
for each in file_r:
    #去掉每行结尾的"\n"
    each=each.strip('\n')
    configtxt=each.split("=")
    if configtxt[0]=="password":
        configdict[configtxt[0]]='654321'
    else:
        configdict[configtxt[0]]=configtxt[1]
print (configdict)
file_w=open("config.txt","w")
file_w.truncate(0)
file_w.writelines(list(configdict))
file_w.close()