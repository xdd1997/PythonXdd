import requests
url = "https://item.jd.com/7437688.html"
try:
	r = requests.get(url)
	r.raise_for_status()  #若返回值不是202，则抛出一个异常
	r.encoding = r.apparent_encoding
	print(r.text[0:1000])
except:
	print("爬取失败")
