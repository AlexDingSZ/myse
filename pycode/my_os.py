import os

#os.rename("a/a.txt","a/b.txt")
#os.renames("a/a.txt","c/b.txt")
path = os.getcwd()
print(os.chdir("c:\\"))
print(os.listdir())
print(os.getcwd())
print(os.chdir(path))
os.mkdir("d")
print(os.listdir())
os.rmdir("d")
print(os.listdir())
os.makedirs("d/e/f/g")
print(os.listdir())
os.removedirs("d/e/f/g")
print(os.listdir())


path = r"E:\软件资料\temp.txt"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join("c","dir","name","temp.txt"))
print(os.path.getatime(path))
print(os.path.getctime(path))
print(os.path.getmtime(path))
print(os.path.getsize(path))
print(os.path.exists(path))
print(os.path.exists("xkd.txt"))
print(os.path.isabs(path))
print(os.path.isabs("a/b/c"))
print(os.path.isfile("a/b.txt"))
print(os.path.getsize(path))
print(os.path.isdir("a"))
print(os.path.isdir("xa"))



s="你好"
s_encode = s.encode("utf-8")
print(s_encode)
print(type(s_encode))
s_decode = s_encode.decode("utf-8")
print(s_decode)

