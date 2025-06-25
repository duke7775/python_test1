#功能：测试文件
#引入os
import os

filepath ='info.txt'

file = open(filepath,'w+')
print(file.tell())

file.write("hello\n")
print(file.tell())

file.write("good")
print(file.tell())

file.seek(0)
print(file.tell())

print(file.read())
print(file.tell())
#删除文件
os.remove(filepath)
