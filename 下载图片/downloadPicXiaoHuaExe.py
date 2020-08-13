import os
from tkinter import *


# pyinstaller -F -w "CreatCodeTimerXDD.py"
# pyinstaller -F "downloadPicXiaoHuaExe.py"
class App:
    def __init__(self, master):

        # 使用Frame添加容器
        frame2 = Frame(master)
        btn_zhuce = Button(frame2, text=u'下载',padx=10, bg='light blue', font=('微软雅黑', 15, ), fg='white',command=self.ZhuCeBtn)
        btn_zhuce.grid(row=2, column=1, sticky=W,padx=60,pady=5)
    #    btn_zhuce1 = Button(frame2, text=u'退出', padx=10, bg='light blue', font=('微软雅黑', 15,), fg='white',command=win.destroy)
    #    btn_zhuce1.grid(row=3, column=1, sticky=W,padx=60, pady=5)
        l1 = Label(frame2, text=u'可能要多点几次叉号才会退出', padx=10, bg='light pink', font=('微软雅黑', 10,), fg='black')
        l1.grid(row=4, column=1, sticky=W, pady=10)
        frame2.pack(pady=0)




    def ZhuCeBtn(self):
        # write by xdd1997  xdd2026@qq.com
        # 2020-08-07

        import time
        import os
        import winreg
        import requests
        import urllib.request
        from bs4 import BeautifulSoup
        import shutil


        if os.path.exists("D:\桌面\校花贴吧图片"):
            shutil.rmtree("D:\桌面\校花贴吧图片")
            print('文件夹中文件已清除')

        # 获取桌面路径
        def desktop_path():
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
            path = winreg.QueryValueEx(key, "Desktop")[0]
            return path

        # -------------递归创建目录-----------
        def CreatPath():
            path = os.path.join(desktop_path().replace('/', '\\'), '校花贴吧图片')
            if not os.path.exists(path):
                os.makedirs(path)
            self.path = path
            return path

        index = 0
        len_Piclist = 240  #240 = 150/3*80  每页大概80张图片
        for i in range(0,150, 50):  ## N 100=50*2，表明下载2页，可改为150，300...
            url = "https://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&pn={}".format(i)
            print(url)
            r = requests.get(url)
            demo = r.text
            soup = BeautifulSoup(demo, "html.parser")
            piclist = []
            for link in soup.find_all('img'):
                link_list = link.get('bpic')
                if link_list != None:
                    piclist.append(link_list)

            for http in piclist:
                print(http)

                name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(time.perf_counter())
                filesavepath = os.path.join(CreatPath(), name + '.jpg')
                urllib.request.urlretrieve(http, filesavepath)
                index = index + 1
                str11 = '正在保存第{:.0f}/{}张图片（大致）'.format(index,len_Piclist) + '-->文件路径为：' + self.path
                print(str11)

                time.sleep(0.2)
            print('下载完成')

win = Tk()
win.title("校花贴吧图片")
app = App(win)
screenwidth = win.winfo_screenwidth()  # 窗口居中
screenheight = win.winfo_screenheight()
W = 250
H = W * 9 / 16
alignstr = '%dx%d+%d+%d' % (W, H, (screenwidth - W) / 2, (screenheight - H) / 2)
win.geometry(alignstr)
win.wm_attributes('-topmost', 1)  # 窗口置顶
win.mainloop()
