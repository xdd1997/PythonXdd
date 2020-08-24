import os
import requests
import urllib.request
from bs4 import BeautifulSoup
#微信下载图片的网址
url = "https://mp.weixin.qq.com/s/J2ZmuTWTEJsM9GvJmUGSGA"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
piclist = []
for link in soup.find_all('img'):
    link_list = link.get('data-src')
    if link_list != None:
        piclist.append(link_list)
# print(piclist)
# print(type(link_list))
# -------------递归创建的目录-----------
path = "D:\桌面\爬取的图片"
if not os.path.exists(path):
    os.makedirs(path)
#-----------存储目录创建结束------------
x = 0
for http in piclist:
    L = len(piclist)
    print(http)
#    filesavepath = r'D:\桌面\爬取的图片\%s.jpg' % x
    filesavepath = os.path.join(path, str(x) + '.jpg')
    urllib.request.urlretrieve(http, filesavepath)
    x += 1
    print('正在保存第{}/{}张图片'.format(x,L))
print('下载完成')