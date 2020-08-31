# write by xdd1997  xdd2026@qq.com
# 2020-08-31
# encoding=utf-8

import os
import re
import time
import urllib.request

file = open('D:\\桌面\\爱情美图 - 在线壁纸.txt', mode='r', encoding='utf-8')
p1 = re.compile(r'http://p.*.jpg')
list =[]
for line in file:
  #  print(line)
    match1 = re.findall(p1, line)
    if (match1 != None) & (match1 != []) :
        list.append(match1)

piclist = []
for ii in list[0]:
    tex = ii.split(' ')
    for jj in tex:
        if "__85" in jj:
            piclist.append(jj)
print(piclist)
picHttp = []
for ii in piclist:
    link = ii.split('"')[1]
    picHttp.append(link)

# -------------递归创建的目录-----------
path = "D:\桌面\爬取的图片"
if not os.path.exists(path):
    os.makedirs(path)
i = 0
for http in picHttp:
    name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(i)
    filesavepath = os.path.join(path, name + '.jpg')
    urllib.request.urlretrieve(http, filesavepath)
    i = i+1
    print('正在下载---')
print('{}张图片下载完成,保存路径为'.format(i) + path)



