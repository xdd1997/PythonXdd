#encoding = utf8
# write by xdd1997  xdd2026@qq.com
# 2020-08-21

'''还是不建议一次爬取多个页面，容易被封，解封时长未知'''
import requests
from bs4 import BeautifulSoup
ii = 130
url = "https://scholar.paodekuaiweixinqun.com/scholar?start={}&q=Cylindrical+Shells&hl=zh-CN&as_sdt=0,5&as_ylo=2016".format(ii)
# https://scholar.paodekuaiweixinqun.com/scholar?start=140&q=Cylindrical+Shells&hl=zh-CN&as_sdt=0,5&as_ylo=2016
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
paperlist = []
for ss in soup.find_all('a',{"target":"_blank"}): # 查找<ul class="f-hide"> ...</ul>  ,{"target":"_blank"}
    tex = ss.get_text().replace('  ','').split('\n')
    texp = ''
    if len(tex) >= 6:
        for t in tex:
            if t !=None:
                texp = texp + t
        paperlist.append(texp)
#print(paperlist)
for paper in paperlist:
    if len(paper)>30:  # 排除类似于[PDF] researchgate.net一样的文本
        print(paper)

