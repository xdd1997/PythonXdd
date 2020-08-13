# edit by xdd
# Before running this script, open appium.exe
# Reference site:https://www.cnblogs.com/deliaries/archive/2020/03/18/12410835.html

import time
from tkinter.messagebox import *
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

start = time.perf_counter()         # 计算程序运行时间

''' 打开支付宝 '''
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
print('----- 正在打开支付宝 -----')
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
print('----- 正在打开蚂蚁森林 -----')
TouchAction(driver).press(x=544, y=706).release().perform()     # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多
# 点击蚂蚁森林（以id打开，这种较好，但是appium有些故障，刷新不出来
# driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
time.sleep(5)

''' 向下滑，找到更多好友，点击 '''
print('----- 正在打开更多好友 -----')
n = 0
while n <= 5:
    start_x = 500
    start_y = 1500
    distance = 1000
    driver.swipe(start_x, start_y, start_x, start_y - distance)
    n = n + 1
driver.find_element_by_xpath("//*[@text='查看更多好友']").click()  # 点击查看更多好友
time.sleep(1)
''' ----------- 进入偷能量界面 ---------- '''
while True:
    TouchAction(driver).press(x=345, y=668).release().perform() # 第一个蚂蚁好友框框的坐标，随着滑动，每一个好友都会出现在这个坐标点
   # time.sleep(0.5)

    name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
    print('正在查看{0}'.format(name))
  #  print(name)
    if name=='郭帅的蚂蚁森林':      # 填写最后一个好友昵称，程序不会遍历到最后一个，因为到最后的时候，界面不能滑动；可先填最后一个，看能遍历到哪一个好友，再修改即可.
        break

    items = driver.find_elements_by_class_name("android.widget.Button")
    if len(items) > 5:
        for i in items:
            #if '能量' in i.text:
            if ('能量' in i.text) | ('消失' in i.text):
                print('收取{0}的{1}'.format(name,i.text.replace('收集','')))
                i.click()

        time.sleep(0.1)
        driver.tap([(50, 130), (70, 150)], 100)
        time.sleep(0.1)

    start_x = 500
    start_y = 1910
    distance = 195  # 一个框的高度
    driver.swipe(start_x, start_y, start_x, start_y - distance)    # 向上滑动一个框的高度   # driver.swipe（分别表示滑动的起始和终点位置的 x/y 坐标）
    time.sleep(0.5)     # 系统反应也需要时间，此处sleep()不可省略


''' 重新进入蚂蚁森林喂小鸡 '''
print('----- 正在打开蚂蚁森林 -----')
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
TouchAction(driver).press(x=544, y=706).release().perform()     # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多

time.sleep(5)
TouchAction(driver).press(x=886, y=1264).release().perform()  # 点击小鸡，进入喂小鸡界面
print('----- 正在打开喂小鸡界面 -----')
time.sleep(5)
TouchAction(driver).press(x=931, y=1973).release().perform()    # 点击饲料
time.sleep(5)
TouchAction(driver).press(x=400, y=1477).release().perform()    # 赶小鸡 01
time.sleep(5)
TouchAction(driver).press(x=257, y=1267).release().perform()
time.sleep(5)
TouchAction(driver).press(x=518, y=1315).release().perform()





end = time.perf_counter()
tim = end - start
txtshow = '----- 偷能量，喂小鸡完成，运行这段代码用时：{:.6f}'.format(tim)
print(txtshow)
showinfo(title='提示', message=txtshow)