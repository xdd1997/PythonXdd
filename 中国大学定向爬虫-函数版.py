import requests
import re
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
print(r.text)
demo = r.text
soup = BeautifulSoup(demo,"html.parser") #熬一锅粥
for link in soup.find_all('a'):
    print(link.get('href'))
for clas in soup.find_all('a'):
    print(clas.get('class'))
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
