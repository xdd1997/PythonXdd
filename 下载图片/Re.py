import re
import os
import urllib
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImage(html,x):
    #https://mmbiz.qpic.cn/mmbiz_jpg/ib55rg6wzUc3B16KIY3uU53nkcTTDic8uEA4WWBPaHJ8LpibvAnkpS2FZtyjrv7w7dbEeNrhfvPuuyReNAxsLdgJA/640?wx_fmt=jpeg
    #https://mmbiz.qpic.cn/mmbiz_jpg/ib55rg6wzUc3B16KIY3uU53nkcTTDic8uEHqocI7r86nehl2NeForAqvcTiaEAIuWjTWPKNXnnXIPuUuqnuJeFKYw/640?wx_fmt=jpeg
    #此处正则为重点
    reg = 'data-src="(.*?)"'
    image = re.compile(reg)
    imlist = re.findall(reg,html.decode('utf-8'))

    print(imlist)
    for i in imlist:
        print(i)
        print(x)
        # 下载内容与.py一起
        #urllib.request.urlretrieve(i,'%s.jpg' % x)
        # 下载位置自定义
        urllib.request.urlretrieve(i, r'F:\desktop\爬取的图片\%s.jpg' % x)
        x +=1
    return x
# -------------递归创建的目录-----------
path = r"F:\desktop\爬取的图片"
if not os.path.exists(path):
    os.makedirs(path)
#-----------存储目录创建结束------------
# main 下载结果与此.py文件在同一目录'
x=1
url = 'https://mp.weixin.qq.com/s/MVDcn0O3093OlIhMYkqBIA'
html = getHtml(url)
x = getImage(html,x)
print('下载完成')

