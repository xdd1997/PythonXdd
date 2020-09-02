# -*- coding: GBK -*-

from urllib import request
import re
import requests
def crawb():
    url="https://xydh.fun/xdd1997"
    file = "url"
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
    with open(file, 'w') as f:
        r = requests.get(url, headers=kv)
        r.encoding = r.apparent_encoding
        pagetext = r.text
        # 正则表达式表示要爬取的是<a href="和"中的内容,"或'都可以,即当前页面下所有的链接url,返回列表
        pagelinks = re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')', pagetext)
        for link in pagelinks:
            try:
                respose=request.urlopen(link)
                f.write(link + "\n")
            except:
                print(link + ":is not url")
if __name__ == "__main__":
    crawb()