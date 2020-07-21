import os
import random
import sys
import urllib
import winreg
#from tkinter import filedialog
import requests
from PIL import Image
from Timer2_2 import Ui_Form  # Timer2为ui对于py文件的名字
from PyQt5.QtWidgets import QDialog,QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime
#import time
import tkinter as tk
from PyQt5.QtGui import QPixmap, QImage
from bs4 import BeautifulSoup


class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法

    def initUI(self):  # 定义初始化界面的方法
        # ----------信号连接自定义的槽---------
        self.pushButton_start.clicked.connect(self.btn_start_click)
        self.pushButton_stop.clicked.connect(self.btn_stop_click)
        self.pushButton_stopAndStart.clicked.connect(self.btn_stopAndStart_click)
        self.pushButton_randompic.clicked.connect(self.btn_randompic_click)
        self.pushButton_downloadpic.clicked.connect(self.btn_downloadpic_click)
        self.pushButton_Shang.clicked.connect(self.btn_Shang_click)



        self.pushButton_pause.setEnabled(False)
        self.pushButton_Shang.setEnabled(False)


        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        time2 = QTimer(self)
        time2.setInterval(1000)
        time2.timeout.connect(self.refresh2)
        time2.start()

        self.btn_randompic_click()
    def showEatTime(self):
        pass

    def btn_Shang_click(self):
        pass


    def btn_downloadpic_click(self):
        self.download_img_desktop()

    def btn_randompic_click(self):
        '''
        url = "http://img.netbian.com/file/2019/0910/7efdc8e60d36329c404005c3c34f7af8.jpg"
        res = requests.get(url)
        img = QImage.fromData(res.content)
        tt = self.label_img.setPixmap(QPixmap.fromImage(img))
        '''
        global filesavepath
        self.download_img()
        self.pic_cut()
        self.pic_SuoFang()
        pix = QPixmap(filesavepath)
        self.label_img.setPixmap(pix)

    def btn_start_click(self):
        self.label_time.setText('ILOVEYOU')
        self.count = int(self.spinBox.text()) * 60
        # self.lineEdit.setReadOnly(True)  # 设置为只读
        print(self.count)

        if self.pushButton_start.isEnabled():
            self.time.start()

    def btn_stop_click(self):
        self.time.stop()

    def btn_stopAndStart_click(self):
        self.btn_stop_click()
        self.btn_start_click()

    def Refresh(self):
        if self.count > 0:

            sec = self.count
            hour = int(sec / 3600)
            min = int(sec % 3600 / 60)
            s = sec % 60
            if hour < 10: hour = '0' + str(hour)
            if min < 10:  min = '0' + str(min)
            if s < 10:    s = '0' + str(s)
            stringTime = str(hour) + ':' + str(min) + ':' + str(s)

            self.label_time.setText(stringTime)
            self.count -= 1
        else:
            self.time.stop()
            self.pushButton_start.setEnabled(True)
            self.label_time.setText('00:00:00')

            window = tk.Tk()
            window.title('My Window')
            l = tk.Label(window, text='你好,计时时间到了!', bg='blue', font=('Arial', 12), width=30, height=2)
            l.pack()
            window.mainloop()

    def refresh2(self):
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2020, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
           # self.lcd.display(intervals)
            self.label_time.setText(stringTime)
            print(days,hour)




    def download_img(self):
        # 微信下载图片的网址
        global http
        global filesavepath
        global http_save
        try:
            num = random.randint(1, 22222)
            url = "http://www.netbian.com/desk/{}.htm".format(num)
            r = requests.get(url)
            demo = r.text
            soup = BeautifulSoup(demo, "html.parser")
            piclist = []
            for link in soup.find_all('img'):
                link_list = link.get('src')
                if link_list != None:
                    piclist.append(link_list)
            http = piclist[2]
        except:
            url = "http://www.netbian.com/desk/22152.htm"
            r = requests.get(url)
            demo = r.text
            soup = BeautifulSoup(demo, "html.parser")
            piclist = []
            for link in soup.find_all('img'):
                link_list = link.get('src')
                if link_list != None:
                    piclist.append(link_list)
            http = piclist[2]

        print(http)
        # -------------递归创建的目录-----------
        path = "c:\\timerXdd"
        if not os.path.exists(path):
            os.makedirs(path)
        filesavepath = os.path.join(path, 'pic.jpg')
        urllib.request.urlretrieve(http, filesavepath)
        print('暂存完成')

    def download_img_desktop(self):
        # 获取桌面路径
        global http
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        path = winreg.QueryValueEx(key, "Desktop")[0]
        # -------------递归创建目录-----------
        path = os.path.join(path.replace('/', '\\'), 'TimerXdd')
        if not os.path.exists(path):
            os.makedirs(path)
        filesavepath = os.path.join(path, 'pic.jpg')
        urllib.request.urlretrieve(http, filesavepath)

        window = tk.Tk()
        window.title('My Window')
        l = tk.Label(window, text='图片已下载到桌面 TimerXdd', bg='green', font=('Arial', 12), width=30, height=2)
        l.pack()
        window.mainloop()

    def pic_cut(self):
        global filesavepath
        img = Image.open(filesavepath)
        (picW, picH) = img.size
        # 欲裁剪为4*3
        bili = 16 / 9
        if picW / picH >= bili:
            print('weight pic')
            picW2 = picH * bili
            left = (picW - picW2) / 2
            right = left + picH * bili
            upper = 0
            lower = picH
            cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
            # print(left, upper, right, lower)
        else:
            picH2 = picW / bili
            left = 0
            upper = (picH - picH2) / 2
            right = picW
            lower = upper + picW / bili
            cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
        cropped.save(filesavepath)

    def pic_SuoFang(self):
        global filesavepath
        mwidth = 320
        mheight = 202
        image = Image.open(filesavepath)
        w, h = image.size
        if w <= mwidth and h <= mheight:
            print(filesavepath, 'is OK.')
            return
        if (1.0 * w / mwidth) > (1.0 * h / mheight):
            scale = 1.0 * w / mwidth
            new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
        else:
            scale = 1.0 * h / mheight
            new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
        new_im.save(filesavepath)
        new_im.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字,可更改等号前面名字
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    w = QDialog()
    main_form.show()
    sys.exit(app.exec_())
