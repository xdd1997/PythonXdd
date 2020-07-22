import os
import random
import sys
import urllib
import winreg
import requests
from PIL import Image
from Timer2_2 import Ui_Form  # Timer2为ui对于py文件的名字
from PyQt5.QtWidgets import QDialog,QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime, Qt, QUrl
import tkinter as tk
from PyQt5.QtGui import QPixmap, QImage, QDesktopServices
from bs4 import BeautifulSoup

# pyinstaller -F -w "TimerMain.py"

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
        self.pushButton_talk.clicked.connect(self.btn_talk_click)
        self.pushButton_showpic.clicked.connect(self.btn_showPic_click)
        self.pushButton_ZhiDing.clicked.connect(self.btn_ZhiDing_click)


        self.pushButton_pause.setEnabled(False)
        self.pushButton_Shang.setEnabled(False)


        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.time2 = QTimer(self)
        self.time2.setInterval(1000)
        self.time2.timeout.connect(self.refresh2)
        self.time2.start()

        self.setWindowTitle('Timer-xdd1997 三天试用版')
        try:      #若有网，下载图片
            self.btn_randompic_click()
        except:  #若没有网，禁用除置顶外所有的按钮
            self.pushButton_randompic.setEnabled(False)
            self.pushButton_downloadpic.setEnabled(False)
            self.pushButton_Shang.setEnabled(False)
            self.pushButton_talk.setEnabled(False)
            self.pushButton_showpic.setEnabled(False)



        self.pushButton_ZhiDing.setText('取消置顶')



    def btn_ZhiDing_click(self):
        btnTxt = self.pushButton_ZhiDing.text()
        if btnTxt=='取消置顶':

            self.setWindowFlags(QtCore.Qt.Widget)  # 取消置顶
            self.pushButton_ZhiDing.setText('置顶')
        else:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 置顶
            self.pushButton_ZhiDing.setText('取消置顶')
        self.show()

    def btn_showPic_click(self):
        try:
            global filesavepath
            global http
            path = "c:\\timerXdd"
            urllib.request.urlretrieve(http, filesavepath)
            img = Image.open(filesavepath)
            img.show()
        except:
            pass

    def btn_talk_click(self):
        QDesktopServices.openUrl(QUrl("https://support.qq.com/products/173442"))

    def btn_Shang_click(self):
        self.pushButton_Shang.setEnabled(False)


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
    #    self.pushButton_Shang.setEnabled(True)
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
            l = tk.Label(window, text='你好,计时时间到了!', bg='green', font=('Arial', 12), width=30, height=2)
            screenwidth = window.winfo_screenwidth()
            screenheight = window.winfo_screenheight()
            width = 300;height = 200
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            window.geometry(alignstr)
            window.wm_attributes('-topmost', 1)  # 窗口置顶
            l.pack()
            window.mainloop()

    def refresh2(self):
        now = QDate.currentDate()
        nowtxt = now.toString(Qt.ISODate)
        date = nowtxt.split('-')
        year = int(date[0]); mount = int(date[1]); day = int(date[2])

        time = QTime.currentTime()
        time1 = time.toString(Qt.DefaultLocaleLongDate)
        time2 = time1.split(':')
        hour = int(time2[0])
        #  程序停止运行

        if (day!=21) & (day!=22) & (day!=22):
            quit()


        startDate = QDateTime.currentMSecsSinceEpoch()
        if hour<11:
            endDate = QDateTime(QDate(year,mount,day), QTime(11, 0, 0)).toMSecsSinceEpoch()
        elif hour<17:
            endDate = QDateTime(QDate(year, mount, day), QTime(17, 0, 0)).toMSecsSinceEpoch()
            self.label_eatTxt.setText('距离吃晚饭还有')
        elif hour<22:
            endDate = QDateTime(QDate(year, mount, day), QTime(22, 0, 0)).toMSecsSinceEpoch()
            self.label_eatTxt.setText('距离下班还有')
        else:
            endDate = QDateTime(QDate(year, mount, day), QTime(24, 0, 0)).toMSecsSinceEpoch()
            self.label_eatTxt.setText('距离吃午饭还有')
        interval = endDate - startDate

        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals =  str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)
            print(interval)

            if   interval<121000 and interval>120000 : # 两分钟提醒
                self.txtShow = '收拾下东西吧，还有2分钟'
                self.showLast2min()

        else:
            pass
            '''
            #self.time2.stop()
            intervals = '00:00:00'
            self.lcd.display(intervals)

            self.txtShow = '下班时间到了！'
            self.showLast2min()
            '''
    def showLast2min(self):
        print('-----------------')
        window = tk.Tk()
        width = 300
        height = 100
        window.title('My Window')
        l = tk.Label(window, text=self.txtShow, bg='green', font=('Arial', 12), width=30, height=2)

        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window.geometry(alignstr)
        window.wm_attributes('-topmost', 1)  # 窗口置顶
        l.pack()
        window.mainloop()

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
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        width = 300; height = 100
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window.geometry(alignstr)
        window.wm_attributes('-topmost', 1)  # 窗口置顶
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


if __name__ == '__main__':  # 四句话：继承-实例化-显示-退出
    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字,可更改等号前面名字
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)   # 窗口置顶

    main_form.show()
    sys.exit(app.exec_())
