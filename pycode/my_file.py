import time
f = open("a/b.txt","w")
f.write("write line1\n" )
f.close()
f = open("a/b.txt","a+")
f.writelines(["listaa ","listbb ","listcc\n"])
f.write("write line2" )
f.close()
f = open("a/b.txt","ab+")
f.write((str("\n"+time.asctime( time.localtime(time.time()))+" line3").encode('UTF-8')))
f.close()
f = open("a/b.txt","r")
print(f.read())
print(f.tell())
f.seek(0)
print(f.readlines())
f.close()
f = open("a/b.txt","r")
for i in f:
    print(i,end="")
f.close()





