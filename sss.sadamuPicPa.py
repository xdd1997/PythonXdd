'''
pip install requests
pip install urllib.request
pip install requests BeautifulSoup4
'''


#添加头部信息
import requests
import urllib.request
from bs4 import BeautifulSoup
url = "https://www.sssam.com/5734.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)

#r = requests.get(url)
r = urllib.request.urlopen(req).read(url)
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

piclist = []

for link in soup.find_all('img'):
    link_list = link.get('src')
    if link_list != None:
        piclist.append(link_list)
print(piclist)
# print(type(link_list))

x = 0
for http in piclist:
    print(http)

    # F:\桌面\pa 是存储路径，需要先建立文件夹
    filesavepath = r'F:\desktop\一见倾心系列\pa\%s.jpg' % x

    urllib.request.urlretrieve(http, filesavepath)
    x += 1
    print('正在保存第{:.0f}张图片'.format(x))

print('下载完成')   
