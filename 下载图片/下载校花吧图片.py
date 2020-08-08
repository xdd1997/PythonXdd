# write by xdd1997  xdd2026@qq.com
# 2020-08-07

import time
import os
import winreg
import requests
import urllib.request
from bs4 import BeautifulSoup


# 获取桌面路径
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
# -------------递归创建目录-----------
def CreatPath():
    path = os.path.join(desktop_path().replace('/','\\'),'校花贴吧图片')
    if not os.path.exists(path):
        os.makedirs(path)
    return path

index = 0
for i in range(0,200,50):  ## 100=50*2，表明下载2页，可改为150，300...
    url = "https://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&pn={}".format(i)
    print(url)
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    piclist = []
    for link in soup.find_all('img'):
        link_list = link.get('bpic')
        if link_list != None:
            piclist.append(link_list)

    for http in piclist:
        print(http)
        name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filesavepath = os.path.join(CreatPath(), name + '.jpg')
        urllib.request.urlretrieve(http, filesavepath)
        index = index + 1
        print('正在保存第{:.0f}张图片'.format(index))

        time.sleep(2)
    print('下载完成')