import os
import random
import sys
import time
import urllib
import winreg
import requests
from PIL import Image
from Timer2 import Ui_Form  # Timer2为ui对于py文件的名字
from TimerSetup import Ui_Form as UISetup  # Timer2为ui对于py文件的名字
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime, Qt, QUrl
import tkinter as tk
from PyQt5.QtGui import QPixmap,  QDesktopServices
from bs4 import BeautifulSoup
import uuid
from Cryptodome.Cipher import DES
import binascii
import tkinter.messagebox
import winsound


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
        self.pushButton_pause.clicked.connect(self.btn_pause_click)
        self.pushButton_stop.clicked.connect(self.btn_stop_click)
      #  self.pushButton_stopAndStart.clicked.connect(self.btn_stopAndStart_click)
        self.pushButton_randompic.clicked.connect(self.btn_randompic_click)
        self.pushButton_downloadpic.clicked.connect(self.btn_downloadpic_click)
        self.pushButton_Shang.clicked.connect(self.btn_Shang_click)
        self.pushButton_talk.clicked.connect(self.btn_talk_click)
        self.pushButton_showpic.clicked.connect(self.btn_showPic_click)
        self.pushButton_ZhiDing.clicked.connect(self.btn_ZhiDing_click)
        self.pushButton_setupMore.clicked.connect(self.btn_setupMore_click)

        # ---------- 设置logo -------
        '''
        try:
            if os.path.exists('c:\\timerXdd\\TimerLogo.jpg'):
                print('001')
                self.setWindowIcon(QIcon('C:\\timerXdd\\004.ico'))

            else:
                http = 'https://pic.downk.cc/item/5f237f5814195aa5946d1309.jpg'
                path = "c:\\timerXdd"

                if not os.path.exists(path):
                    os.makedirs(path)
                filesavepath = os.path.join(path, 'TimerLogo.jpg')
                urllib.request.urlretrieve(http, filesavepath)
                print('002')
                self.setWindowIcon(QIcon(filesavepath))

        except:
            print('设置logo不成功')

        '''

        self.OpenZhuCe()

        self.time = QTimer(self)                           # 设置第一个计时器用以倒计时
        self.time.setInterval(1000)                       # 每隔1000毫秒发射一次信号（即执行一次timeout)
        self.time.timeout.connect(self.Refresh)         # timeout事件的绑定

        self.time2 = QTimer(self)
        self.time2.setInterval(1000)
        self.time2.timeout.connect(self.refresh2)
        self.time2.start()

        self.setWindowTitle('Timer-xdd1997 ')   #设置窗口标题
        try:      #若有网，下载图片
            self.btn_randompic_click()                      # 执行随机显示照片
        except:  #若没有网，禁用除置顶外所有的按钮
            self.pushButton_randompic.setEnabled(False)
            self.pushButton_downloadpic.setEnabled(False)
            self.pushButton_Shang.setEnabled(False)
            self.pushButton_talk.setEnabled(False)
            self.pushButton_showpic.setEnabled(False)


        self.pushButton_pause.setEnabled(False)
        self.pushButton_Shang.setEnabled(False)     #启动时上一张按钮不可用
        self.pushButton_Ready.setEnabled(False)
        self.pushButton_ZhiDing.setText('取消置顶')  #默认置顶（在if __main__设置的），此处设置置顶按钮默认显示文字
        self.tabWidget.setCurrentIndex(0)   #设置默认tab显示

        self.lineEdit_zhifubao.setReadOnly(True)  # 设置为只读
        self.lineEdit_lianxi.setReadOnly(True)

        with open("c:\\timerXdd\\此文件夹重要，请阅读.txt", mode='w', encoding='utf-8') as ff:
            ff.writelines('此文件夹为TimerXDD软件的缓存目录，请勿随意改动文件名名及内容！\n')
            ff.writelines('如果改错，请删除本文件夹timerXdd,可重新注册使用.\n code.txt文件的内容为本机注册码')

    def btn_setupMore_click(self):

        self.mySetup = winSetup()
        self.mySetup.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 窗口置顶
        self.mySetup.show()
        self.close


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
        try:
            QDesktopServices.openUrl(QUrl("https://support.qq.com/products/173442"))
        except:
            self.tabWidget.setCurrentIndex(1)

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
        #self.label_time.setText('ILOVEYOU')
        self.count = int(self.spinBox.text()) * 60
        self.pushButton_pause.setEnabled(True)
        print(self.count)

        if self.pushButton_start.isEnabled():
            self.time.start()

    def btn_pause_click(self):

        btnTxt = self.pushButton_pause.text()
        if btnTxt == '暂停':
            self.time.stop()
            self.pushButton_pause.setText('继续')
        else:
            self.time.start()
            self.pushButton_pause.setText('暂停')


    def btn_stop_click(self):
        self.time.stop()
        self.label_time.setText('LOVE YU')
    '''
    def btn_stopAndStart_click(self):
        self.btn_stop_click()
        self.btn_start_click()
    '''
    # 第一个计时器每一秒发射的信号
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

            self.txtShow = '你好,计时时间到了!'
            winsound.Beep(440, 1500)
            self.showLast2min()



    # 第2个计时器每一秒发射的信号
    def refresh2(self):
        """左下角的时间显示，限制三天"""
        now = QDate.currentDate()
        nowtxt = now.toString(Qt.ISODate)
        date = nowtxt.split('-')
        year = int(date[0]); mount = int(date[1]); day = int(date[2])

        time = QTime.currentTime()
        time1 = time.toString(Qt.DefaultLocaleLongDate)
        time2 = time1.split(':')
        hour = int(time2[0]);minute = int(time2[1]);sec = int(time2[2])
        #  程序停止运行，用于三天试用
        '''
        if (day!=22) & (day!=23) & (day!=24):
            quit()
            
        '''
        # 判断是否启用喝水1提醒
        if os.path.exists('c:\\timerXdd\\setupcheckboxDrank.txt'):

            with open('c:\\timerXdd\\setupcheckboxDrank.txt', mode='r', encoding='utf-8') as ff:
                checkbox2val = ff.readline()
                if checkbox2val =='1':
                    self.checkBox_drank.setChecked(True)
                else:
                    self.checkBox_drank.setChecked(False)
        else:
            self.checkBox_drank.setChecked(True)

        if self.checkBox_drank.isChecked():
            with open("c:\\timerXdd\\setupcheckboxDrank.txt", mode='w', encoding='utf-8') as ff:
                ff.writelines('1')
            if  (hour > 8) & (hour < 22) & (minute == 0) & (sec == 0):
                self.txtShow = '学习1个小时，喝口水，休息下眼睛吧'
                self.showLast2min()
        else:
            with open("c:\\timerXdd\\setupcheckboxDrank.txt", mode='w', encoding='utf-8') as ff:
                ff.writelines('0')


        startDate = QDateTime.currentMSecsSinceEpoch()


        if os.path.exists('c:\\timerXdd\\setupcheckbox1.txt'):

            with open('c:\\timerXdd\\setupcheckbox1.txt', mode='r', encoding='utf-8') as ff:
                checkbox1val = ff.readline()

        else:
            checkbox1val='1'

        if checkbox1val=='1':    # 勾选了默认窗口

            if hour<11:
                endDate = QDateTime(QDate(year, mount, day), QTime(11, 0, 0)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离吃午饭还有')
            elif hour<17:
                endDate = QDateTime(QDate(year, mount, day), QTime(17, 0, 0)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离吃晚饭还有')
            elif  ((day % 2) == 0) & (hour < 20) & (minute<30):
                endDate = QDateTime(QDate(year, mount, day), QTime(20, 30, 0)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离8:30跑步还有')

            elif hour < 22 :
                endDate = QDateTime(QDate(year, mount, day), QTime(22, 0, 0)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离下班还有')
            else:
                endDate = QDateTime(QDate(year, mount, day), QTime(24, 0, 0)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离今天结束')

        else: # 没有勾选了默认窗口

            if os.path.exists('c:\\timerXdd\\setupTime.txt'):
                with open('c:\\timerXdd\\setupTime.txt', mode='r', encoding='utf-8') as ff:
                    timetxt = ff.readlines()
            L = len(timetxt)

            hmTPlist = []

            for tt in timetxt:
                tth = (tt.split('***')[0]).split(':')[0]
                ttm = (tt.split('***')[0]).split(':')[1]
                ttTxt = tt.split('***')[1]
                ttPin = tt.split('***')[2].replace('\n', '')
                hmTPlist.append((tth, ttm, ttTxt, ttPin))

            #  设置
            if L == 0:
                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                self.label_eatTxt.setText('距离今天结束')
            if L == 1:
                h1 = int(hmTPlist[0][0]);
                m1 = int(hmTPlist[0][1]);
                p1 = hmTPlist[0][3];
                if (((hour == h1) & (minute < m1)) | (hour < h1)):

                    if p1 == '每天':

                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')

                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')
            if L == 2:
                h1 = int(hmTPlist[0][0]);
                h2 = int(hmTPlist[1][0]);

                m1 = int(hmTPlist[0][1]);
                m2 = int(hmTPlist[1][1]);

                p1 = hmTPlist[0][3];
                p2 = hmTPlist[1][3];

                if (((hour == h1) & (minute < m1)) | (hour < h1)):
                    if p1 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(1, L):
                            if hmTPlist[i][3] != p1:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')

                elif ((hour == h2) & (minute < m2)) | (hour < h2):

                    if p2 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')

                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')

            if L == 3:  # 有三件事
                h1 = int(hmTPlist[0][0]);
                h2 = int(hmTPlist[1][0]);
                h3 = int(hmTPlist[2][0]);

                m1 = int(hmTPlist[0][1]);
                m2 = int(hmTPlist[1][1]);
                m3 = int(hmTPlist[2][1]);

                p1 = hmTPlist[0][3];
                p2 = hmTPlist[1][3];
                p3 = hmTPlist[2][3];

                if (((hour == h1) & (minute < m1)) | (hour < h1)):
                    if p1 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(1, L):
                            if hmTPlist[i][3] != p1:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')

                elif ((hour == h2) & (minute < m2)) | (hour < h2):

                    if p2 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(2, L):
                            if hmTPlist[i][3] != p2:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h3) & (minute < m3)) | (hour < h3):
                    if p3 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')
                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')

            if L == 4:
                h1 = int(hmTPlist[0][0]);
                h2 = int(hmTPlist[1][0]);
                h3 = int(hmTPlist[2][0]);
                h4 = int(hmTPlist[3][0]);

                m1 = int(hmTPlist[0][1]);
                m2 = int(hmTPlist[1][1]);
                m3 = int(hmTPlist[2][1]);
                m4 = int(hmTPlist[3][1]);

                p1 = hmTPlist[0][3];
                p2 = hmTPlist[1][3];
                p3 = hmTPlist[2][3];
                p4 = hmTPlist[3][3];

                if (((hour == h1) & (minute < m1)) | (hour < h1)):
                    if p1 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(1, L):
                            if hmTPlist[i][3] != p1:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')

                elif ((hour == h2) & (minute < m2)) | (hour < h2):

                    if p2 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(2, L):
                            if hmTPlist[i][3] != p2:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h3) & (minute < m3)) | (hour < h3):
                    if p3 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(3, L):
                            if hmTPlist[i][3] != p3:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h4) & (minute < m4)) | (hour < h4):
                    if p4 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')
                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')
            if L == 5:
                h1 = int(hmTPlist[0][0]);
                h2 = int(hmTPlist[1][0]);
                h3 = int(hmTPlist[2][0]);
                h4 = int(hmTPlist[3][0]);
                h5 = int(hmTPlist[4][0]);

                m1 = int(hmTPlist[0][1]);
                m2 = int(hmTPlist[1][1]);
                m3 = int(hmTPlist[2][1]);
                m4 = int(hmTPlist[3][1]);
                m5 = int(hmTPlist[4][1]);

                p1 = hmTPlist[0][3];
                p2 = hmTPlist[1][3];
                p3 = hmTPlist[2][3];
                p4 = hmTPlist[3][3];
                p5 = hmTPlist[4][3];

                if (((hour == h1) & (minute < m1)) | (hour < h1)):
                    if p1 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(1, L):
                            if hmTPlist[i][3] != p1:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')

                elif ((hour == h2) & (minute < m2)) | (hour < h2):

                    if p2 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(2, L):
                            if hmTPlist[i][3] != p2:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h3) & (minute < m3)) | (hour < h3):
                    if p3 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(3, L):
                            if hmTPlist[i][3] != p3:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h4) & (minute < m4)) | (hour < h4):
                    if p4 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(4, L):
                            if hmTPlist[i][3] != p4:
                                endDate = QDateTime(QDate(year, mount, day),
                                                    QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),
                                                          0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h5) & (minute < m5)) | (hour < h5):
                    if p5 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p5 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p5 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')
                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')
            if L == 6:
                h1 = int(hmTPlist[0][0]);h2 = int(hmTPlist[1][0]);h3 = int(hmTPlist[2][0]);
                h4 = int(hmTPlist[3][0]);h5 = int(hmTPlist[4][0]);h6 = int(hmTPlist[5][0]);

                m1 = int(hmTPlist[0][1]);m2 = int(hmTPlist[1][1]);m3 = int(hmTPlist[2][1]);
                m4 = int(hmTPlist[3][1]);m5 = int(hmTPlist[4][1]);m6 = int(hmTPlist[5][0]);

                p1 = hmTPlist[0][3];p2 = hmTPlist[1][3];p3 = hmTPlist[2][3];p4 = hmTPlist[3][3];p5 = hmTPlist[4][3];p6 = hmTPlist[5][3];

                if (((hour == h1) & (minute < m1)) | (hour < h1)):
                    if p1 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '奇数日') &  (day%2==1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p1 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h1, m1, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[0][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(1,L):
                            if hmTPlist[i][3]!=p1:
                                endDate = QDateTime(QDate(year, mount, day), QTime(int((hmTPlist[i][0])),int((hmTPlist[i][1])), 0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')

                elif ((hour == h2) & (minute < m2)) | (hour < h2):

                    if p2 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '奇数日') &  (day%2==1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p2 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h2, m2, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[1][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(2, L):
                            if hmTPlist[i][3] != p2:
                                endDate = QDateTime(QDate(year, mount, day),QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h3) & (minute < m3)) | (hour < h3):
                    if p3 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p3 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h3, m3, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[2][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(3, L):
                            if hmTPlist[i][3] != p3:
                                endDate = QDateTime(QDate(year, mount, day),QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h4) & (minute < m4)) | (hour < h4):
                    if p4 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p4 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h4, m4, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[3][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(4, L):
                            if hmTPlist[i][3] != p4:
                                endDate = QDateTime(QDate(year, mount, day),QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])), 0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h5) & (minute < m5)) | (hour < h5):
                    if p5 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p5 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p5 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h5, m5, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[4][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        for i in range(5, L):
                            if hmTPlist[i][3] != p5:
                                endDate = QDateTime(QDate(year, mount, day),QTime(int((hmTPlist[i][0])), int((hmTPlist[i][1])),0)).toMSecsSinceEpoch()
                                str1 = '距离' + hmTPlist[i][2] + '还有'
                                self.label_eatTxt.setText(str1)
                                break
                            else:
                                endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                                self.label_eatTxt.setText('距离今天结束')
                elif ((hour == h6) & (minute < m6)) | (hour < h6):
                    if p6 == '每天':
                        endDate = QDateTime(QDate(year, mount, day), QTime(h6, m6, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[5][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p6 == '奇数日') & (day % 2 == 1):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h6, m6, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[5][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    elif (p6 == '偶数日') & (day % 2 == 0):
                        endDate = QDateTime(QDate(year, mount, day), QTime(h6, m6, 0)).toMSecsSinceEpoch()
                        str1 = '距离' + hmTPlist[5][2] + '还有'
                        self.label_eatTxt.setText(str1)
                    else:
                        endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                        self.label_eatTxt.setText('距离今天结束')
                else:
                    endDate = QDateTime(QDate(year, mount, day), QTime(23, 59, 59)).toMSecsSinceEpoch()
                    self.label_eatTxt.setText('距离今天结束')





        interval = endDate - startDate

        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals =  str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)


            if   interval<121000 and interval>120000 : # 两分钟提醒
                self.txtShow = '收拾下东西吧，还有2分钟'
                winsound.Beep(440, 1500)  # 440赫兹  2000豪秒
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

        window = tk.Tk()
        width = 300
        height = 100
        window.title('温馨提示')
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
            #url = "http://pic.netbian.com/tupian/{}.html".format(num)
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


        # -------------递归创建的目录-----------
        path = "c:\\timerXdd"
        if not os.path.exists(path):
            os.makedirs(path)
        filesavepath = os.path.join(path, 'pic.jpg')
        urllib.request.urlretrieve(http, filesavepath)
        print('下载模块 downloadpic 正常')

    def download_img_desktop(self):
        # 获取桌面路径
        global http
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        path = winreg.QueryValueEx(key, "Desktop")[0]
        # -------------递归创建目录-----------
        path = os.path.join(path.replace('/', '\\'), 'TimerXdd')
        if not os.path.exists(path):
            os.makedirs(path)

        name0 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        name = name0 + '.jpg'
        filesavepath = os.path.join(path, name)
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
        print('下载到桌面模块 downloadpic_desktop 正常')

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
        print('裁剪模块 pic_cut 正常')

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
        print('缩放模块 SuoFang 正常')

    def get_ZhuCeId(self):
        # 获取本机 Mac  加密Mac
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        # 对 Mac 加密
        mac2 = mac.replace(":", '6')
        if len(mac2) == 17:
            mac3 = mac2[0:17:2]
            mac3 = mac2[0:8]
        else:
            if len(mac2) % 8 != 0:
                mac3 = mac2 + "+" * (8 - len(mac2) % 8)
        macID = mac3
        return macID

    def get_ZhuCeCode(self):
        macID = self.get_ZhuCeId()
        if len(macID) % 8 != 0:
            macID = macID + "+" * (8 - len(macID) % 8)
        print('注册ID：',macID)
        # 密钥：必须为8字节
        key = b'xdd19976'
        # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
        des = DES.new(key, DES.MODE_ECB)
        # 加密
        result = des.encrypt(macID.encode())
        # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
        tt = binascii.b2a_hex(result)
        # 转为字符串
        zhuceCode = str(tt, 'utf-8')
        return zhuceCode

    def ZhuCeBtn(self):
        global e1
        global e2
        global flag
        flag = 0
        txt = e2.get()
        macCode = self.get_ZhuCeCode()
        if txt == macCode:
            tkinter.messagebox.showinfo('提示', '注册成功,请关闭注册窗口')
            flag = 1
            with open("c:\\timerXdd\\code.txt", mode='w', encoding='utf-8') as ff:
                ff.write(macCode)
        else:
            tkinter.messagebox.showinfo('提示', '注册码错误')
            flag = 0

    def ZhuCeclean(self):

        global e2
        e2.delete(0, 'end')

    def ZhuCehelp(self):
        try:
            QDesktopServices.openUrl(QUrl("https://support.qq.com/products/173442"))
            print('正在打开帮助网站')
        except:
            tkinter.messagebox.showinfo('提示', '无网络，请联网')

    def ShowZhuCeFig(self):
        global e1
        global e2
        # 第1步，实例化object，建立窗口window
        window = tk.Tk()
        # 第2步，给窗口的可视化起名字
        window.title('欢迎来到注册世界')
        # 第3步，设定窗口的大小(长 * 宽)
        window.geometry('300x200')  # 这里的乘是小x
        window.wm_attributes('-topmost', 1)  # 置顶
        tk.Label(window, text='注册窗口', font=('微软雅黑', 14)).place(x=90, y=4)
        tk.Label(window, text='注册ID:', font=('微软雅黑', 12)).place(x=10, y=37)
        tk.Label(window, text='注册码:', font=('微软雅黑', 12)).place(x=10, y=80)
        tk.Label(window, bg='lightblue', text='发送ID至 xdd2026@qq.com 获取激活码', font=('微软雅黑', 8)).place(x=20, y=120)
        e1 = tk.Entry(window, show=None)
        e1.place(x=120, y=40)  # 显示成明文形式    输入框

        e2 = tk.Entry(window, show=None)
        e2.place(x=120, y=85)  # 显示成明文形式    输入框

        b1 = tk.Button(window, text='注册', bg='lightblue', width=7, height=1,font=('微软雅黑', 10) ,command=self.ZhuCeBtn).place(x=30, y=150)  # 方法要在这条语句前面
        b2 = tk.Button(window, text='清空', bg='lightblue', width=7, height=1,font=('微软雅黑', 10), command=self.ZhuCeclean).place(x=120, y=150)  # 方法要在这条语句前面
        b3 = tk.Button(window, text='帮助', bg='lightblue', width=7, height=1, font=('微软雅黑', 10),command=self.ZhuCehelp).place(x=210,y=150)  # 方法要在这条语句前面

        macID = self.get_ZhuCeId()
        e1.insert(0, macID)

        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (300, 200, (screenwidth - 300) / 2, (screenheight - 200) / 2)
        window.geometry(alignstr)
        window.mainloop()

    def OpenZhuCe(self):
        global flag
        flag = 0
        if os.path.exists('c:\\timerXdd\\code.txt'):
            with open('c:\\timerXdd\\code.txt', mode='r', encoding='utf-8') as ff:
                codeRead = ff.readline()
                realCode = self.get_ZhuCeCode()
                if codeRead == realCode:
                    print('配对成功')
                else:
                    self.ShowZhuCeFig()
                    if flag != 1:
                        os._exit(0)
        else:
            folder = os.path.exists("c:\\timerXdd")
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs("c:\\timerXdd")  # makedirs 创建文件时如果路径不存在会创建这个路径
            with open("c:\\timerXdd\\code.txt", mode='w', encoding='utf-8') as ff:
                print("文件创建成功！")
            self.ShowZhuCeFig()
            if flag != 1:
                os._exit(0)

class winSetup(QtWidgets.QWidget, UISetup):
    def  __init__ (self):
        super(winSetup, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.makecomboxBox()
        self.pushButton_save.clicked.connect(self.btn_save_click)
        self.pushButton_exit.clicked.connect(self.close)
        self.checkBox_1.stateChanged.connect(self.checkBox_1_choose)
        self.setTimeTxt()
        try:
            http = 'https://pic.downk.cc/item/5f21263214195aa5944c759e.jpg'
            path = "c:\\timerXdd"
            if not os.path.exists(path):
                os.makedirs(path)
            filesavepath = os.path.join(path, 'weixin.jpg')
            urllib.request.urlretrieve(http, filesavepath)
            pix = QPixmap('c:\\timerXdd\\weixin.jpg')
            #pix = QPixmap('D:\\桌面\\2.jpg')
            self.label_setimg.setPixmap(pix)

        except:
            print('无网络吧')

    def setTimeTxt(self):
        if os.path.exists('c:\\timerXdd\\setupTime.txt'):
            with open('c:\\timerXdd\\setupTime.txt', mode='r', encoding='utf-8') as ff:
                timetxt = ff.readlines()
            L = len(timetxt)
            hmTPlist = []
            for tt in timetxt:
                tth = tt.split('***')[0].split(':')[0]
                ttm = (tt.split('***')[0]).split(':')[1]
                ttTxt = tt.split('***')[1]
                ttPin = tt.split('***')[2].replace('\n', '')
                hmTPlist.append((tth, ttm, ttTxt, ttPin))
            print('0002')
            if L==1:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime( QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                # 设置频次1显示
                if hmTPlist[0][3] == '每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3] == '奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
            elif L==2:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime(QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                self.lineEdit_set2.setText(hmTPlist[1][2])
                self.timeEdit_2.setTime( QtCore.QTime(int(hmTPlist[1][0]), int(hmTPlist[1][1])))
                # 设置频次1显示
                if hmTPlist[0][3] == '每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3] == '奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
                # 2
                if hmTPlist[1][3] == '每天':
                    self.comboBox_2.setCurrentIndex(0)
                elif hmTPlist[1][3] == '奇数日':
                    self.comboBox_2.setCurrentIndex(1)
                else:
                    self.comboBox_2.setCurrentIndex(2)
            elif L==3:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime(QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                self.lineEdit_set2.setText(hmTPlist[1][2])
                self.timeEdit_2.setTime(QtCore.QTime(int(hmTPlist[1][0]), int(hmTPlist[1][1])))
                self.lineEdit_set3.setText(hmTPlist[2][2])
                self.timeEdit_3.setTime(QtCore.QTime(int(hmTPlist[2][0]), int(hmTPlist[2][1])))
                # 设置频次1显示
                if hmTPlist[0][3] == '每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3] == '奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
                # 2
                if hmTPlist[1][3] == '每天':
                    self.comboBox_2.setCurrentIndex(0)
                elif hmTPlist[1][3] == '奇数日':
                    self.comboBox_2.setCurrentIndex(1)
                else:
                    self.comboBox_2.setCurrentIndex(2)
                # 3
                if hmTPlist[2][3] == '每天':
                    self.comboBox_3.setCurrentIndex(0)
                elif hmTPlist[2][3] == '奇数日':
                    self.comboBox_3.setCurrentIndex(1)
                else:
                    self.comboBox_3.setCurrentIndex(2)
            elif L==4:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime(QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                self.lineEdit_set2.setText(hmTPlist[1][2])
                self.timeEdit_2.setTime(QtCore.QTime(int(hmTPlist[1][0]), int(hmTPlist[1][1])))
                self.lineEdit_set3.setText(hmTPlist[2][2])
                self.timeEdit_3.setTime(QtCore.QTime(int(hmTPlist[2][0]), int(hmTPlist[2][1])))
                self.lineEdit_set4.setText(hmTPlist[3][2])
                self.timeEdit_4.setTime(QtCore.QTime(int(hmTPlist[3][0]), int(hmTPlist[3][1])))
                # 设置频次1显示
                if hmTPlist[0][3] == '每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3] == '奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
                # 2
                if hmTPlist[1][3] == '每天':
                    self.comboBox_2.setCurrentIndex(0)
                elif hmTPlist[1][3] == '奇数日':
                    self.comboBox_2.setCurrentIndex(1)
                else:
                    self.comboBox_2.setCurrentIndex(2)
                # 3
                if hmTPlist[2][3] == '每天':
                    self.comboBox_3.setCurrentIndex(0)
                elif hmTPlist[2][3] == '奇数日':
                    self.comboBox_3.setCurrentIndex(1)
                else:
                    self.comboBox_3.setCurrentIndex(2)
                # 4
                if hmTPlist[3][3] == '每天':
                    self.comboBox_4.setCurrentIndex(0)
                elif hmTPlist[3][3] == '奇数日':
                    self.comboBox_4.setCurrentIndex(1)
                else:
                    self.comboBox_4.setCurrentIndex(2)
            elif L==5:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime(QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                self.lineEdit_set2.setText(hmTPlist[1][2])
                self.timeEdit_2.setTime(QtCore.QTime(int(hmTPlist[1][0]), int(hmTPlist[1][1])))
                self.lineEdit_set3.setText(hmTPlist[2][2])
                self.timeEdit_3.setTime(QtCore.QTime(int(hmTPlist[2][0]), int(hmTPlist[2][1])))
                self.lineEdit_set4.setText(hmTPlist[3][2])
                self.timeEdit_4.setTime(QtCore.QTime(int(hmTPlist[3][0]), int(hmTPlist[3][1])))
                self.lineEdit_set5.setText(hmTPlist[4][2])
                self.timeEdit_5.setTime(QtCore.QTime(int(hmTPlist[4][0]), int(hmTPlist[4][1])))
                # 设置频次1显示
                if hmTPlist[0][3] == '每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3] == '奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
                # 2
                if hmTPlist[1][3] == '每天':
                    self.comboBox_2.setCurrentIndex(0)
                elif hmTPlist[1][3] == '奇数日':
                    self.comboBox_2.setCurrentIndex(1)
                else:
                    self.comboBox_2.setCurrentIndex(2)
                # 3
                if hmTPlist[2][3] == '每天':
                    self.comboBox_3.setCurrentIndex(0)
                elif hmTPlist[2][3] == '奇数日':
                    self.comboBox_3.setCurrentIndex(1)
                else:
                    self.comboBox_3.setCurrentIndex(2)
                # 4
                if hmTPlist[3][3] == '每天':
                    self.comboBox_4.setCurrentIndex(0)
                elif hmTPlist[3][3] == '奇数日':
                    self.comboBox_4.setCurrentIndex(1)
                else:
                    self.comboBox_4.setCurrentIndex(2)
                # 5
                if hmTPlist[4][3] == '每天':
                    self.comboBox_5.setCurrentIndex(0)
                elif hmTPlist[4][3] == '奇数日':
                    self.comboBox_5.setCurrentIndex(1)
                else:
                    self.comboBox_5.setCurrentIndex(2)
            elif L == 6:
                self.lineEdit_set1.setText(hmTPlist[0][2])
                self.timeEdit_1.setTime(QtCore.QTime(int(hmTPlist[0][0]), int(hmTPlist[0][1])))
                self.lineEdit_set2.setText(hmTPlist[1][2])
                self.timeEdit_2.setTime(QtCore.QTime(int(hmTPlist[1][0]), int(hmTPlist[1][1])))
                self.lineEdit_set3.setText(hmTPlist[2][2])
                self.timeEdit_3.setTime(QtCore.QTime(int(hmTPlist[2][0]), int(hmTPlist[2][1])))
                self.lineEdit_set4.setText(hmTPlist[3][2])
                self.timeEdit_4.setTime(QtCore.QTime(int(hmTPlist[3][0]), int(hmTPlist[3][1])))
                self.lineEdit_set5.setText(hmTPlist[4][2])
                self.timeEdit_5.setTime(QtCore.QTime(int(hmTPlist[4][0]), int(hmTPlist[4][1])))
                self.lineEdit_set6.setText(hmTPlist[5][2])
                self.timeEdit_6.setTime(QtCore.QTime(int(hmTPlist[5][0]), int(hmTPlist[5][1])))
                # 设置频次1显示
                if hmTPlist[0][3]=='每天':
                    self.comboBox_1.setCurrentIndex(0)
                elif hmTPlist[0][3]=='奇数日':
                    self.comboBox_1.setCurrentIndex(1)
                else:
                    self.comboBox_1.setCurrentIndex(2)
                #2
                if hmTPlist[1][3]=='每天':
                    self.comboBox_2.setCurrentIndex(0)
                elif hmTPlist[1][3]=='奇数日':
                    self.comboBox_2.setCurrentIndex(1)
                else:
                    self.comboBox_2.setCurrentIndex(2)
                #3
                if hmTPlist[2][3] == '每天':
                    self.comboBox_3.setCurrentIndex(0)
                elif hmTPlist[2][3] == '奇数日':
                    self.comboBox_3.setCurrentIndex(1)
                else:
                    self.comboBox_3.setCurrentIndex(2)
                #4
                if hmTPlist[3][3] == '每天':
                    self.comboBox_4.setCurrentIndex(0)
                elif hmTPlist[3][3] == '奇数日':
                    self.comboBox_4.setCurrentIndex(1)
                else:
                    self.comboBox_4.setCurrentIndex(2)
                #5
                if hmTPlist[4][3] == '每天':
                    self.comboBox_5.setCurrentIndex(0)
                elif hmTPlist[4][3] == '奇数日':
                    self.comboBox_5.setCurrentIndex(1)
                else:
                    self.comboBox_5.setCurrentIndex(2)
                #6
                if hmTPlist[5][3] == '每天':
                    self.comboBox_6.setCurrentIndex(0)
                elif hmTPlist[5][3] == '奇数日':
                    self.comboBox_6.setCurrentIndex(1)
                else:
                    self.comboBox_6.setCurrentIndex(2)
            else:
                pass
        else:
            pass
    def makecomboxBox(self):

        showList = ["每天","奇数日","偶数日"]
   #     self.showList = showList
       # showList = ["每天"]
        self.comboBox_1.addItems(showList)
        self.comboBox_2.addItems(showList)
        self.comboBox_3.addItems(showList)
        self.comboBox_4.addItems(showList)
        self.comboBox_5.addItems(showList)
        self.comboBox_6.addItems(showList)


    def btn_save_click(self):

        txt1 = self.lineEdit_set1.text(); time1 = self.timeEdit_1.text(); box1 = self.comboBox_1.currentText()
        txt2 = self.lineEdit_set2.text(); time2 = self.timeEdit_2.text(); box2 = self.comboBox_2.currentText()
        txt3 = self.lineEdit_set3.text(); time3 = self.timeEdit_3.text(); box3 = self.comboBox_3.currentText()
        txt4 = self.lineEdit_set4.text(); time4 = self.timeEdit_4.text(); box4 = self.comboBox_4.currentText()
        txt5 = self.lineEdit_set5.text(); time5 = self.timeEdit_5.text(); box5 = self.comboBox_5.currentText()
        txt6 = self.lineEdit_set6.text(); time6 = self.timeEdit_6.text(); box6 = self.comboBox_6.currentText()
        list1 = [time1, '***',txt1 , '***', box1];list2 = [time2,'***',txt2,'***',box2];list3 = [time3,'***',txt3,'***',box3];
        list4 = [time4, '***',txt4, '***', box4];list5 = [time5,'***',txt5,'***',box5];list6 = [time6,'***',txt6,'***',box6];
        list=[list1,list2,list3,list4,list5,list6]
        listReal = []
        for li in list:
            if li[2] not in ['',' ','  ']:
                listReal.append(li)
        listWrite = sorted(listReal, key=lambda l: (int(l[0].split(':')[0]), int(l[0].split(':')[1])))
        with open("c:\\timerXdd\\setupTime.txt", mode='w', encoding='utf-8') as ff:
            for li in listWrite:
                ff.writelines(li)
                ff.writelines('\n')
        with open("c:\\timerXdd\\setupcheckbox1.txt", mode='w', encoding='utf-8') as ff:
            ff.writelines('0')
        self.showInformation('已经保存成功')


    def showInformation(self,txtShow):

        window = tk.Tk()
        width = 300
        height = 100
        window.title('温馨提示')
        l = tk.Label(window, text=txtShow, bg='green', font=('Arial', 12), width=30, height=2)

        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window.geometry(alignstr)
        window.wm_attributes('-topmost', 1)  # 窗口置顶
        l.pack()
        window.mainloop()

    def panDuan(self):
        pass
    def checkBox_1_choose(self):
        if self.checkBox_1.isChecked():
            with open("c:\\timerXdd\\setupcheckbox1.txt", mode='w', encoding='utf-8') as ff:
                ff.writelines('1')
            '''
            with open("c:\\timerXdd\\setupTime.txt", mode='w', encoding='utf-8') as ff:
                ff.write('11:00***吃午饭***每天\n17:00***吃晚饭***每天\n20:30***跑步***偶数日\n22:00***下班***奇数日')
            print('勾选')
            '''
            self.lineEdit_set1.setText('吃午饭')
            self.lineEdit_set2.setText('吃晚饭')
            self.lineEdit_set3.setText('跑步')
            self.lineEdit_set4.setText('下班')
            self.timeEdit_1.setTime(QtCore.QTime(11,0))
            self.timeEdit_2.setTime(QtCore.QTime(17,0))
            self.timeEdit_3.setTime(QtCore.QTime(20, 30))
            self.timeEdit_4.setTime(QtCore.QTime(22,0))
            self.comboBox_1.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_3.setCurrentIndex(2)
            self.comboBox_4.setCurrentIndex(1)

        else:
            with open("c:\\timerXdd\\setupcheckbox1.txt", mode='w', encoding='utf-8') as ff:
                ff.writelines('0')

            print('未勾选')


    '''
    def comboBoxChange(self):
        box1 = self.comboBox_1.currentText()
        print(self.comboBox_1.currentText())
        return box1
    '''

if __name__ == '__main__':  # 四句话：继承-实例化-显示-退出

    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字,可更改等号前面名字 MyPyQT_Form()继承自Ui_Form
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)   # 窗口置顶
    main_form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)  # 禁止窗口最大化
    main_form.setFixedSize(main_form.width(), main_form.height());  # 禁止拉伸窗口
    main_form.show()
    sys.exit(app.exec_())
