import os






if os.path.exists('c:\\timerXdd\\log4.txt'):
    with open('c:\\timerXdd\\log4.txt', mode='r', encoding='utf-8') as ff:
        print(ff.readlines())
else:
    folder = os.path.exists("c:\\timerXdd")
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs("c:\\timerXdd")  # makedirs 创建文件时如果路径不存在会创建这个路径
    with open("c:\\timerXdd\\log4.txt", mode='w', encoding='utf-8') as ff:
        print("文件创建成功！")