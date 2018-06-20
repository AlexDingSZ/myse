configdict={}
f=open("config.txt","r+")
f.truncate(0)
f.write("username=xiaoming\n")
f.write("password=123456\n")
f.write( "mobile=15818646666\n")
f.close()
f=open("config.txt","r+")
lines=f.readlines()
for everyline in lines:
    split_list=everyline.split("=")
    #print (split_list)
    configdict[split_list[0]]=split_list[1][:-1]
    if split_list[0]=="password":
        configdict[split_list[0]]="654321"
        lines[lines.index(everyline)]="password=654321\n"
print (configdict)
print (lines)
f.truncate()
f.close()