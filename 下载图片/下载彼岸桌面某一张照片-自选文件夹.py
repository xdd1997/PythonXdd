# write by xdd1997  xdd2026@qq.com

import os
import random
import requests
import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

#打开选择文件夹对话框
root = tk.Tk()
root.withdraw()
Folderpath = filedialog.askdirectory() #获得选择好的文件夹
str2 = Folderpath.replace('/','\\')

#微信下载图片的网址

num = random.randint(1,9999)
url = "http://www.netbian.com/desk/{}.htm".format(num)

#url = "https://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&pn=0"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
piclist = []
for link in soup.find_all('img'):
    link_list = link.get('src')
    if link_list != None:
        piclist.append(link_list)



http = piclist[2]
print(http)
filesavepath = os.path.join(str2,'pic.jpg')
urllib.request.urlretrieve(http, filesavepath)
print('下载完成,保存路径为' + str2)

