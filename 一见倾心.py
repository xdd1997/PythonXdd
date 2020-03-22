'''
pip install requests
pip install urllib.request
pip install requests BeautifulSoup4
'''
import requests
import urllib.request
from bs4 import BeautifulSoup

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

x = 0
for http in piclist:
    print(http)

    # F:\桌面\pa 是存储路径，需要先建立文件夹
    filesavepath = r'H:\desktop\一见倾心系列\壁纸\xx期\%s.jpg' % x

    urllib.request.urlretrieve(http, filesavepath)
    x += 1
    print('正在保存第{:.0f}张图片'.format(x))

print('下载完成')   
