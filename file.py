#功能：测试文件
#引入os
import os

file = open('info.txt','w')

file.write("hello\n")
file.tell()
print(file.tell())

file.write("good")
file.tell()
print(file.tell())

file = open('info.txt','r')
file.seek(0)
print(file.tell())

print(file.read())
print(file.tell())
#删除文件
os.remove('info.txt')
