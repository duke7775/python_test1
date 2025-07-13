#功能：获取网页信息
import requests
from bs4 import BeautifulSoup
import chardet

url = 'https://cn.bing.com/'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# 获取文件编码
def get_encoding(response)-> str:
    encoding = chardet.detect(response.content)['encoding']
    print(encoding)
    response.encoding = encoding
    with open('bing.html', 'w', encoding=encoding) as f:
        f.write(response.text)
        print('文件已保存为bing.html')
        return encoding  

# 获取标题
def get_title(soup)-> None:
    title_tag = soup.find('title')
   
    # 打印标题文本
    if title_tag:
        print(title_tag.get_text())
    else:
        print("未找到<title>标签")

# 获取链接
def get_links(soup)-> None:
    first_link = soup.find('a')
    print(first_link)
    print("----------------------------")

    # 获取第一个 <a> 标签的 href 属性
    first_link_url = first_link.get('href')
    print(first_link_url)
    print("----------------------------")

    # 查找所有 <a> 标签
    all_links = soup.find_all('a')
    print(all_links)

def main():
    encoding = get_encoding(response)
    get_title(soup)
    get_links(soup)



if __name__ == "__main__":
    main()   
