#中国大学定向爬虫
import requests
from bs4 import BeautifulSoup
import bs4

ulist = []
url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
	print("爬取失败")
html = r.text
soup = BeautifulSoup(html, "html.parser")
for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
       tds = tr('td')
       ulist.append([tds[0].string, tds[1].string, tds[3].string])
     
tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
print(tplt.format("排名","学校名称","总分",chr(12288))) #使得中文对齐
num = 20
for i in range(num): #打印前20名
    u=ulist[i]
    print(tplt.format(u[0],u[1],u[2],chr(12288)))

