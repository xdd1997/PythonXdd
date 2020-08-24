'''
@Time    : 2019/11/20 15:10
@Author  : XXXX
@Software: PyCharm
'''
import urllib
import requests
import os
import lxml
from lxml import etree

items=[]

class item:
    title =''
    music_url = ''
    def __init__(self,title,music_url):
        self.title = title
        self.music_url = music_url

    def get_title(self):
        return  self.title

    def get_music_url(self):
        return self.music_url


def start_request(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cache-Control':'max-age=0',
        'Host': 'www.tukuppt.com',
        'Referer': 'https://www.tukuppt.com/yinxiao/j109/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res=requests.get(url,headers=headers,timeout=5)
    res.encoding='utf-8'
    html=lxml.etree.HTML(res.text)
    get_item(html)
    next_pages = html.xpath("//a[contains(text(),'下一页')]/@href") #  https://www.tukuppt.com
    return next_pages

def get_item(html):
    for box in html.xpath('//dl[@class="cbox audio-box "]'):
        title=box.xpath('.//dt[@class="info"]//a[1]/text()')[0]
        music_url = "https:" + box.xpath('.//audio[@preload="none"]//source/@src')[0]
        it= item(title,music_url)
        items.append(it)

def run(start_url):
    next_pages=start_request(start_url)
    while len(next_pages) > 0:
        print(next_pages[0])
        page=start_request("https://www.tukuppt.com"+next_pages[0])
        next_pages = page

def download_music(path):
    if not os.path.exists(path):
        os.makedirs(path)
    for it in items:
        try:
            print("*"*10 + "正在下载——"+it.get_title()+"——"+"*"*10)
            content=urllib.request.urlopen(it.get_music_url(),timeout=5).read()
            with open(path+it.get_title()+'.MP3','wb') as file:
                file.write(content)
                file.close()
        except Exception as e:
            print("*"*15+str(e))
            print('')
            continue


if __name__ == "__main__":
    start_url="https://www.tukuppt.com/yinxiao/j110/"   #起始链接
    path="F://file//music//"   #存储地址
    run(start_url)
    download_music(path)
