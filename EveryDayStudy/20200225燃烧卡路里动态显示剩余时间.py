#2020-03-01
#edit by xdd
import time
import sys
print ("========燃烧你的卡路里========")
print (30 *"#")
weight=float(input("输入您的体重（KG）：") )
speed=float(input("速度（公里/小时）："))
times=int(input("跑步时间（分钟）："))
time2 = times * 60  #将输入时间转换为秒
for tt in range(1,time2):
    dista = speed * tt / (60*60)
    calor_tt = weight * 30 / (400 / (speed * 1000 / 60)) * tt /(60*60)
    (a,b) = divmod(time2-tt,60)
    leave_time = str(a)+'分'+str(b)+'秒'
    dista = tt/ 3600 * speed
   # print('剩余时间：',59-a,'分钟',b,'秒')
    sys.stdout.write('\r')
    sys.stdout.write('剩余时间:{}  跑步距离:{:.2f}公里  消耗热量:{:.2f} 千卡'.format(leave_time, dista, calor_tt))
    sys.stdout.flush
    time.sleep(0.01)



'''
import time
import sys
print ("==========虚拟跑步机=========")
print (30 *"#")
weight=float(input("输入您的体重（KG）：") )
speed=float(input("速度（公里/小时）："))
times=int(input("跑步时间（分钟）："))
times=times*60
leave=0
while leave<times :
    leave+=1
    min, sec = divmod(times-leave,60)
    leave_time=str(min)+'分'+str(sec)+'秒'
    dista=leave/3600 * speed
    calor =weight * 30/(400/(speed*1000/60)) * leave/60/60
    sys.stdout.write('\r')
    sys.stdout.write('剩余时间:{}  跑步距离:{:.2f}公里  消耗热量:{:.2f} 千卡'.format(leave_time,dista,calor))
    sys.stdout.flush
    time.sleep(0.3)
'''