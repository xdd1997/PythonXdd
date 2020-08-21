#encoding = utf8
# write by xdd1997  xdd2026@qq.com
# 2020-08-21
'''容易被封，容易被封，容易被封'''
import requests
from bs4 import BeautifulSoup
import time
import random
for ii in range(100,180,10):  # 爬取90.html时会被禁
    url = "https://scholar.paodekuaiweixinqun.com/scholar?start={}&q=Cylindrical+Shells&hl=zh-CN&as_sdt=0,5&as_ylo=2016".format(ii)    #
    print(url)
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
    print('----------------------------------------------------------------------------------------------')
    for ss in soup.find_all('a',{"target":"_blank"}): # 查找<ul class="f-hide"> ...</ul>  ,{"target":"_blank"}
       # for ii in ss.find_all('b'):
        tex = ss.get_text().replace('  ','').split('\n')
        if len(tex) == 7:
            print(tex[1]+ ' ' + tex[3]+ ' '+ tex[6])
    time.sleep(random.random()*10 + 5)

