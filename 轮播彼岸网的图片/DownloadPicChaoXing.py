import os
import requests
import time
import urllib.request

#----获取时间----创建文件夹----
tt = time.strftime("%Y%m%d---%H%M", time.localtime())
#path = r"F:\desktop\爬取的图片"
path = r"F:\desktop"+'\\'+tt+'爬虫'
if not os.path.exists(path):
    os.makedirs(path)
    print('文件夹创建完成  '+path)
#--------------存储目录创建结束----
#------------Main------------------
piclist = []
for ii in range(1,500,1):
    #https://s3.ananas.chaoxing.com/doc/a1/f9/17/56f5788ce049ab01b512183cec6ce855/thumb/15.png
    url = 'https://s3.ananas.chaoxing.com/doc/a1/f9/17/56f5788ce049ab01b512183cec6ce855/thumb/%i.png' % ii
    piclist.append(url)
print(piclist)
try:
    x = 1
    for http in piclist:
        print(http)
       # filesavepath = r'F:\desktop\爬取的图片\%s.jpg' % x
        filesavepath = path+'\%s.jpg' % x
        urllib.request.urlretrieve(http, filesavepath)
        x += 1
        print('正在保存第{:.0f}张图片'.format(x))
        time.sleep(0.3)
except:
    print("下载结束")