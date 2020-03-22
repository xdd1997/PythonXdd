import os
import requests
import urllib.request
from bs4 import BeautifulSoup
#微信下载图片的网址
url = "https://mp.weixin.qq.com/s/cm3Bua0UM1jbZnr2de7TWg"
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
path = r"F:\desktop\爬取的图片"
if not os.path.exists(path):
    os.makedirs(path)
#-----------存储目录创建结束------------
x = 0
for http in piclist:
    print(http)
    filesavepath = r'F:\desktop\爬取的图片\%s.jpg' % x
    urllib.request.urlretrieve(http, filesavepath)
    x += 1
    print('正在保存第{:.0f}张图片'.format(x))
print('下载完成')