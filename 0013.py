# 用 Python 写一个爬图片的程序
import requests
import os
from bs4 import BeautifulSoup

url = requests.get('http://tieba.baidu.com/p/2166231880')
soup = BeautifulSoup(url.text, 'html.parser')
img_urls = soup.findAll('img',bdwater='杉本有美吧，1280,860')
#img_urls = soup.findAll('img', bdwater='杉本有美吧, 1280, 860')
print(img_urls)
for img_url in img_urls:
    img_src = img_url['src']
    os.path.split(img_src)[1]
    with open('D:\python project'+os.path.split(img_src)[1], 'wb') as f:
        f.write(requests.get(img_src).content)
