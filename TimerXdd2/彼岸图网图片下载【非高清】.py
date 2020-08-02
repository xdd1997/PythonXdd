# 下载彼岸图网图片，http://pic.netbian.com/
# 2020-08-01

import winreg
from bs4 import BeautifulSoup
import os
import urllib
import random
import requests
num = random.randint(1, 22222)
print(num)
num2 = 15966
#url = "http://pic.netbian.com/tupian/{}.html".format(num)
#url = "http://www.netbian.com/desk/{}.htm".format(num)
#
url = "http://pic.netbian.com/tupian/15966.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
piclist = []
print(piclist)
for link in soup.find_all('img'):
    link_list = link.get('src')
    if link_list != None:
        piclist.append(link_list)
print(piclist)
http = "http://pic.netbian.com/" + piclist[0]
print(http)



# -------------递归创建的目录-----------
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
path = winreg.QueryValueEx(key, "Desktop")[0]
# -------------递归创建目录-----------
path = os.path.join(path.replace('/', '\\'), '001')
if not os.path.exists(path):
    os.makedirs(path)

filesavepath = os.path.join(path, 'pic.jpg')
urllib.request.urlretrieve(http, filesavepath)
print('下载模块 downloadpic 正常')