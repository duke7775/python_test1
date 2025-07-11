#说明：文件读写
import random


def read_random(file_path):
    result = {}
    with open(file_path) as file:
        file.seek(0)
        file_content = file.read()
        max_pos = min(1000,len(file_content) - 1)
        for _ in range(10):
            pos = random.randint(1, max_pos)
            result[pos] = file_content[pos]
    return result


 
def read_row(file_path):
    result = {}
    with open(file_path) as file:
        file.seek(0)
        file_content = file.readlines()
        for index, line in enumerate(file_content):
            result[index] = line.strip()
    return result
 

def write_random(file_path):
    result = {}
    with open(file_path, 'w') as file:
        for _ in range(10):
            pos = random.randint(1, 1000)
            char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            result[pos] = char
            file.seek(pos)
            file.write(char)
    return result



file_path = "D:\python\content.txt"
print(read_random(file_path))
print(read_row(file_path))
print(write_random(file_path))