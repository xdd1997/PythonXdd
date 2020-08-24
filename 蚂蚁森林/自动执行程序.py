# edit by xdd1997 2020-08-14
# 自动执行程序偷取蚂蚁森林能量

from PyQt5.QtCore import QTime, Qt
import time as t
print('进入自动执行程序')
while True:
    time = QTime.currentTime()
    time1 = time.toString(Qt.DefaultLocaleLongDate)
    time2 = time1.split(':')
    hour = int(time2[0]);
    minute = int(time2[1]);
    sec = int(time2[2])
    if (hour != 7) & (hour != 8)& (hour != 1):
        print(str(hour) + ':' + str(minute) + '不执行,休息25分钟')
        t.sleep(1500) # 25分钟

    elif ((hour ==7) & (minute ==0))| ((hour ==7) & (minute ==27)) | ((hour ==8) & (minute ==18)) | ((hour ==1) & (minute ==0)):
        try:
            print('时间到了，即将执行')
            from 偷能量快速版.py import *
        except:
            print('执行失败，可能是 Appium未打开 / 未连接手机')
    else:
        print(str(hour) + ':' + str(minute) + '不执行，休息25s')
        t.sleep(35)  # 35S