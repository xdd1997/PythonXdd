# write by xdd1997  xdd2026@qq.com

import os
import requests
import urllib.request
from bs4 import BeautifulSoup
#微信下载图片的网址
url = "http://www.netbian.com/desk/22152.htm"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
piclist = []
for link in soup.find_all('img'):
    link_list = link.get('src')
    if link_list != None:
        piclist.append(link_list)

# -------------递归创建的目录-----------
path = r"D:\桌面\爬取的图片"   # 若此为第20行，要和第27行一起更改
if not os.path.exists(path):
    os.makedirs(path)

http = piclist[2]
print(http)
filesavepath = r'D:\桌面\爬取的图片\pic.jpg'
urllib.request.urlretrieve(http, filesavepath)
print('下载完成,保存路径为'+ path)

