import os
import requests
import time
import urllib.request

#----获取时间----创建文件夹----
tt = time.strftime("%Y%m%d---%H%M", time.localtime())
#path = r"F:\desktop\爬取的图片"
path = 'F:\\desktop'+'\\'+tt+'爬虫'
if not os.path.exists(path):
    os.makedirs(path)
    print('文件夹创建完成  '+path)

#------------获取图片下载链接--1234----5648------------
piclist = []
for ii in range(1,500,1):
    url = 'https://s3.ananas.chaoxing.com/doc/1d/cc/2b/bc4c3ab388e75e8f42f9f7fedc087468/thumb/%i.png' % ii
    piclist.append(url)
print(piclist)

#------------主程序-------xdd--------
x = 1
for http in piclist:
    print(http)
   # filesavepath = r'F:\desktop\爬取的图片\%s.jpg' % x
    filesavepath = path+'\%s.jpg' % x
    urllib.request.urlretrieve(http, filesavepath)
    x += 1
    print('正在保存第{:.0f}张图片'.format(x))
    time.sleep(1)

