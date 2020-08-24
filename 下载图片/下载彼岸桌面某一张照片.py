# write by xdd1997  xdd2026@qq.com

import os
import random
import requests
import urllib.request
from bs4 import BeautifulSoup
#微信下载图片的网址
num = random.randint(1,9999)
url = "http://www.netbian.com/desk/{}.htm".format(num)
#url = "http://www.netbian.com/desk/22152.htm"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
piclist = []
for link in soup.find_all('img'):
    link_list = link.get('src')
    if link_list != None:
        piclist.append(link_list)

# -------------递归创建的目录-----------
path = "F:\desktop\爬取的图片"
if not os.path.exists(path):
    os.makedirs(path)

http = piclist[2]
print(http)
filesavepath = os.path.join(path, 'pic.jpg')
urllib.request.urlretrieve(http, filesavepath)
print('下载完成,保存路径为' + path)

