# edit by xdd1997 2020-08-14
# 自动执行程序偷取蚂蚁森林能量

from PyQt5.QtCore import QTime, Qt
import time as t
import SouYiSou1208
print('进入自动执行程序')
# --------- -------------- -------------- --------#
isAuto = 1    # 1:按时间执行；   0：立刻执行           #
# --------- -------------- ------------- ---------#
if isAuto == 0:
    SouEnergy.main()
else:
    while True:
        time = QTime.currentTime()
        time1 = time.toString(Qt.DefaultLocaleLongDate)
        time2 = time1.split(':')
        hour = int(time2[0])
        minute = int(time2[1])
        sec = int(time2[2])
        if (hour != 7) & (hour != 0):
            print(str(hour) + ':' + str(minute) + '不执行,休息25分钟')
            t.sleep(1500) # 25分钟

        # 笔记本设置为27 才能收到行走的能量
        elif ((hour == 7) & (minute == 28)) | ((hour == 7) & (minute == 59))  | ((hour == 0) & (minute ==30)):
            try:
                print('时间到了，即将执行')
                SouYiSou1208.main()
                time.sleep(60)
            except:
                print('执行失败，可能是 Appium未打开 / 未连接手机')
        else:
            print(str(hour) + ':' + str(minute) + '不执行，休息{}s'.format(60-sec))
            t.sleep(60-sec)  # 35S