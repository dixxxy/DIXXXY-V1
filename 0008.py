# 一个HTML文件，找出里面的正文

import requests, re
from bs4 import BeautifulSoup


url = 'http://weibo.com/u/1848474693/home?wvr=5&lf=reg'
data = requests.get(url)
r = re.findall(r'<body>[\s\S]*</body>', data.text)
print(r[0])

print('-------------------------')
soup = BeautifulSoup(data.text,'html.parser')
print(soup.body.text)


