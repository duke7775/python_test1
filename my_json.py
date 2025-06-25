#说明 
#功能：测试json文件
#引入模块
import json
import os

#定义数据
data = {"language":"Python","os":"Windows","keywords":["del","print"]}

#写入
with open("data.json", "w+") as f:
    json.dump(data,f)
    f.seek(0)
    content = json.load(f)
    print(content)

#删除文件
os.remove("data.json")
