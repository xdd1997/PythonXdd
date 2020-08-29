# edit by xdd
# Before running this script, open appium.exe
# Reference site:https://www.cnblogs.com/deliaries/archive/2020/03/18/12410835.html

import time
import tkinter.messagebox
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

start = time.perf_counter()         # 计算程序运行时间

''' ---------- 打开支付宝 ---------- '''
desired_caps = {
                "platformName": "Android",
                "deviceName": "MI 6X",
                "appPackage": "com.eg.android.AlipayGphone",
                "appActivity": "com.eg.android.AlipayGphone.AlipayLogin",
                "noReset": "true",
                "fullReset": "false",
                "automationName": "UiAutomator1"
}
server = 'http://localhost:4723/wd/hub'
print('正在打开支付宝')
driver = webdriver.Remote(server, desired_caps)  # 启用两次，是因为锁屏打开手机一次有可能打不开
time.sleep(5)
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
print('正在打开蚂蚁森林')
#TouchAction(driver).press(x=544, y=706).release().perform()     # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多
driver.find_element_by_xpath("//*[@text='蚂蚁森林']").click()  # 点击蚂蚁森林
# 点击蚂蚁森林（以id打开，这种较好，但是appium有些故障，刷新不出来
# driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
time.sleep(5)
''' ---------- 收取自己的能量 ---------- '''
try:
    print('正在偷自己能量')
    items = driver.find_elements_by_class_name("android.widget.Button")
 #   print(items)
    name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
    if len(items) > 14:
        for i in items:
            if '能量' in i.text:
                i.click()
                print('我点')
                time.sleep(0.5)
except:
    pass

''' 在蚂蚁森林界面，向下滑，找到更多好友，点击 '''
print('正在打开更多好友')
time.sleep(2)
n = 0
while n <= 5:
    start_x = 500
    start_y = 1500
    distance = 1000
    driver.swipe(start_x, start_y, start_x, start_y - distance)
    n = n + 1
    time.sleep(0.2)
driver.find_element_by_xpath("//*[@text='查看更多好友']").click()  # 点击查看更多好友
time.sleep(1)
driver.find_element_by_xpath("//*[@text='总排行榜']").click()  # 点击总排行榜
# ----------- 进入偷能量界面 ---------- '''
while True:
    TouchAction(driver).press(x=345, y=481).release().perform() # 第一个蚂蚁好友框框的坐标，随着滑动，每一个好友都会出现在这个坐标点
   # time.sleep(0.5) # 等一会让系统进入这个界面

    name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
    print('正在查看{0}'.format(name))
    if name in ['陈欣的蚂蚁森林','崔鼎正的蚂蚁森林']:      # 填写最后一个好友昵称，程序不会遍历到最后一个，因为到最后的时候，界面不能滑动；可先填最后一个，看能遍历到哪一个好友，再修改即可.
        break

    items = driver.find_elements_by_class_name("android.widget.Button")
   # print(len(items),'\n',items)
    if len(items) > 6:      # 执行此项是界面界面有东西（能量或者不可点能量）在自己的名字栏，因len(items）=0<5,会直接向上划过
        try:
            for i in items:
                if '能量' in i.text:
                    print('我点点')
                    i.click()
                    time.sleep(0.5)
            TouchAction(driver).press(x=69, y=138).release().perform()  # 左上角返回
            time.sleep(0.2)
        except:
            pass
    elif len(items) > 1: # 执行此项的是能量界面为空的好友；
        TouchAction(driver).press(x=69, y=138).release().perform()  # 左上角返回
        time.sleep(0.2)
    else:               # 加执行此项的是 点击无反应的界面,和自己的名字栏，(len=0)不能左上角返回
        pass
    start_x = 500
    start_y = 1910
    distance = 187  # 一个框的高度
    driver.swipe(start_x, start_y, start_x, start_y - distance)    # 向上滑动一个框的高度   # driver.swipe（分别表示滑动的起始和终点位置的 x/y 坐标）
    time.sleep(0.5)     # 系统反应也需要时间，此处sleep()不可省略

TouchAction(driver).press(x=995, y=129).release().perform()  # 右上角退出,蚂蚁森林
time.sleep(2)
print('正在打开蚂蚁森林')
TouchAction(driver).press(x=544, y=706).release().perform()

end = time.perf_counter()
tim = end - start
txtshow = '偷能量完成，运行这段代码用时：{:.6f}秒'.format(tim)
print(txtshow)
tkinter.messagebox.showinfo('提示',txtshow)
