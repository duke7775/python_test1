#功能：测试文件
#说明 引入os
import os

file = open('info.txt','w')

file.write("hello\n")
file.write("good")

file = open('info.txt','r')
print(file.read())
 
#删除文件
os.remove('info.txt')
