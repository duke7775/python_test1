#说明：文件读写
import random


def read_random(file_path):
    result = {}
    with open(file_path, encoding='utf-8') as file:
        file.seek(0)
        file_content = file.read()
        max_pos = min(1000,len(file_content) - 1)
        for _ in range(10):
            pos = random.randint(0, max_pos)
            result[pos] = file_content[pos]
    return result


 
def read_row(file_path):
    result = {}
    with open(file_path, encoding='utf-8') as file:
        file.seek(0)
        file_content = file.readlines()
        for index, line in enumerate(file_content):
            result[index] = line.strip()
    return result
 

def write_random(file_path):
    result = {}
    with open(file_path, 'r+', encoding='utf-8') as file:
        file_content = file.read()
        max_pos = min(1000, len(file_content) - 1)
        if len(file_content) < 1:
            print("文件为空")
            return result
        
        for _ in range(10):
            pos = random.randint(1, 1000)
            char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            result[pos] = char
            file.seek(pos)
            file.write(char)
    return result



def process_file(file_path):
    print("Random Read:", read_random(file_path))
    print("Row Read:", read_row(file_path))
    print("Write Random:", write_random(file_path))
 
if __name__ == "__main__":
    file_path = r"D:\python\content.txt"
    process_file(file_path)
