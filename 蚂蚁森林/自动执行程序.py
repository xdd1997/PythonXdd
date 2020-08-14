# edit by xdd1997
# 2020-08-14
# 自动执行程序偷取蚂蚁森林能量

from PyQt5.QtCore import QTime, Qt
import time as t

while True:
    time = QTime.currentTime()
    time1 = time.toString(Qt.DefaultLocaleLongDate)
    time2 = time1.split(':')
    hour = int(time2[0]);
    minute = int(time2[1]);
    sec = int(time2[2])
    if hour !=7:
        t.sleep(1200) # 20分钟
        print(str(hour) + ':' + str(minute) + '不执行')
    elif (hour ==7) & (minute >27) :
        from 摘_偷_喂.py import *
        break
    else:
        print(str(hour) + ':' + str(minute) + '不执行')
        t.sleep(50)