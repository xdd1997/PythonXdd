import re
import urllib
import urllib.request

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

def getImage(html,x):
	reg = r'src="(https://img.*?wx_co=1)"'
	image = re.compile(reg)
	imlist = re.findall(reg,html.decode('utf-8'))

	print(imlist)
	for i in imlist:
		print(i)
		print(x)
		urllib.request.urlretrieve(i,'%s.jpg' % x)
		x +=1
	return x
x=1
url = 'https://mp.weixin.qq.com/s/MVDcn0O3093OlIhMYkqBIA'
html = getHtml(url)
x = getImage(html,x)




