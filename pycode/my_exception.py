
try:
    f = open("tmp.txt","wb")
    f.write("write something")

except FileNotFoundError  as e:
    print("error info:",e)
finally:
    f.close()

