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
        # ������ʽ��ʾҪ��ȡ����<a href="��"�е�����,"��'������,����ǰҳ�������е�����url,�����б�
        pagelinks = re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')', pagetext)
        for link in pagelinks:
            try:
                respose=request.urlopen(link)
                f.write(link + "\n")
            except:
                print(link + ":is not url")
if __name__ == "__main__":
    crawb()