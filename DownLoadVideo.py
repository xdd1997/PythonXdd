
import requests
import os
video_url ='http://upos-sz-mirrorhw.bilivideo.com/dspxcode/m200104ws38ev9vpy8bbrh1eq2zzcz0l-1-56.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1578135782&gen=playurl&os=hwbv&oi=3396757456&trid=7818c4daf4044b3b8110b7124d0778c2s&platform=html5&upsig=3adbecc2b2bcc29733c65c2ef3280cd6&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&wsTime=1578135782'
titlename = '2'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
response = requests.get(video_url, headers=headers, stream=True)

if not os.path.exists('videoxdd'):  # 如果video目录不存在时
    os.mkdir('videoxdd')             # 创建该目录

if os.path.exists('videoxdd'):
    with open('videoxdd/'+titlename+'.mp4', 'wb')as f:                     # 将视频写入指定位置
        for data in response.iter_content(chunk_size=1024):             # 循环写入，实现一段一段的写
            f.write(data)                                                # 写入视频文件
            f.flush()                                                    # 刷新缓存
        print('下载完成！')


