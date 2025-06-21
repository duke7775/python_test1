
file = open('info.txt','w')

file.write("hello\n")
file.write("good")

file = open('info.txt','r')
print(file.read())
 
#删除文件