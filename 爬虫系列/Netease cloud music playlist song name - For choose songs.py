#encoding = utf8
# write by xdd1997  xdd2026@qq.com
# 2020-08-20

import requests
from bs4 import BeautifulSoup
id = 979321026
url = "https://music.163.com/playlist?id={}".format(id)    # 注意直接复制的网址要去掉#号
try:
    kv = {'user-agent':'Mozilla/5.0'}   #应对爬虫审查
    r = requests.get(url,headers=kv)
    r.raise_for_status()      			#若返回值不是202，则抛出一个异常
    r.encoding = r.apparent_encoding
except:
    print("进入网站失败")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
#print(soup)

index = 0
for ss in soup.find_all('ul',{"class":"f-hide"}): # 查找<ul class="f-hide"> ...</ul>
    for ii in ss.find_all('a'):
       # print(ii.string)
       index = index + 1
       print( str(index) + '\n'+ '点歌 ' + ii.string)


'''
for i in soup.ul.descendants:
    print(i.string)
print('------------------------------------------')
for i in soup.ul.children:
    print(i.string)
'''


