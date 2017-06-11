# 一个HTML文件，找出里面的链接

import re, requests
from bs4 import BeautifulSoup

url = 'http://linyii.com'
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')
urls = soup.a
print(urls)
urls = soup.findAll('a')
for u in urls:
    print(u['href'])
#for u in urls:
    #print(u['href'])