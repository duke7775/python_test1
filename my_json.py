#引入模块
import json
import os

#定义数据
data = {"name": "duke", "age":19, "days": 25}

#写入
with open("data.json", "w+") as f:
    json.write(data,f)
    f.seek(0)
    content = json.load(f)
    print(content)

#删除文件
os.remove("data.json")