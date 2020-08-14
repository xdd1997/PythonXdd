# edit by xdd
# Before running this script, open appium.exe
# Reference site:https://www.cnblogs.com/deliaries/archive/2020/03/18/12410835.html

import time
from tkinter.messagebox import *
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
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
print('正在打开蚂蚁森林')
TouchAction(driver).press(x=544, y=706).release().perform()     # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多
# 点击蚂蚁森林（以id打开，这种较好，但是appium有些故障，刷新不出来
# driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
time.sleep(5)
def getSelfEnergy():
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
                    print('收取{0}的{1}'.format(name, i.text.replace('收集', ''))) # i.text为“收集能量5克”
                    time.sleep(1)
    except:
        pass
def raiseChicken():
    ''' ---------- 喂小鸡 ---------- '''
    # 小鸡不在也不召回了，有没有粮食
    time.sleep(5)
    TouchAction(driver).press(x=886, y=1264).release().perform()  # 点击小鸡，进入喂小鸡界面
    print('正在打开喂小鸡界面')
    time.sleep(5)
    TouchAction(driver).press(x=931, y=1973).release().perform()  # 点击饲料
    time.sleep(1)
    TouchAction(driver).press(x=400, y=1477).release().perform()  # 点第一只鸡
    time.sleep(2)
    TouchAction(driver).press(x=237, y=1272).release().perform()  # 请走Ta
    time.sleep(5)
    TouchAction(driver).press(x=843, y=1478).release().perform()  # 点第二只鸡
    time.sleep(2)
    TouchAction(driver).press(x=686, y=1262).release().perform()  # 请走Ta
    time.sleep(2)
    TouchAction(driver).press(x=995, y=129).release().perform()  # 右上角退出喂小鸡界面，回到蚂蚁森林
    '''
    print('正在打开喂小鸡界面')
    TouchAction(driver).press(x=886, y=1264).release().perform()  # 点击小鸡，进入喂小鸡界面
    time.sleep(5)
    TouchAction(driver).press(x=931, y=1973).release().perform()    # 点击饲料
    time.sleep(2)
    TouchAction(driver).press(x=561, y=1285).release().perform()    # 找小鸡
    time.sleep(5)
    TouchAction(driver).press(x=400, y=1455).release().perform()    # 点击找到左边的小鸡
    time.sleep(2)
    TouchAction(driver).press(x=561, y=1314).release().perform()    # 请回家
    time.sleep(5)
    TouchAction(driver).press(x=931, y=1973).release().perform()    # 点击饲料
    time.sleep(2)
    
    TouchAction(driver).press(x=995, y=129).release().perform()     # 右上角退出喂小鸡界面，回到蚂蚁森林
    time.sleep(2)
    '''

def stealFriendEnergy():
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
    driver.find_element_by_xpath("//*[@text='查看更多好友']").click()  # 点击查看更多好友
    time.sleep(1)
    # ----------- 进入偷能量界面 ---------- '''
    while True:
        TouchAction(driver).press(x=345, y=668).release().perform() # 第一个蚂蚁好友框框的坐标，随着滑动，每一个好友都会出现在这个坐标点
        time.sleep(0.5) #等一会让系统进入这个界面

        name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
        print('正在查看{0}'.format(name))
        if name in ['陈欣的蚂蚁森林','崔鼎正的蚂蚁森林']:      # 填写最后一个好友昵称，程序不会遍历到最后一个，因为到最后的时候，界面不能滑动；可先填最后一个，看能遍历到哪一个好友，再修改即可.
            break

        items = driver.find_elements_by_class_name("android.widget.Button")
    #    print(len(items)，'\n',items)
        if len(items) > 5:
            try:
                for i in items:
                    if ('我的大树' not in i.text) & ('看林区' not in i.text) & ('成就' not in i.text) & ('发消息' not in i.text) & ('弹幕' not in i.text) & ('浇水' not in i.text):
                  #      print('正在收/替{0}收能量'.format(name))
                        i.click()
                   #     print('我点了一下')
                        time.sleep(0.2)

                time.sleep(0.2)
                TouchAction(driver).press(x=69, y=138).release().perform()  # 左上角返回
                time.sleep(0.2)
            except:
                pass

        start_x = 500
        start_y = 1910
        distance = 195  # 一个框的高度
        driver.swipe(start_x, start_y, start_x, start_y - distance)    # 向上滑动一个框的高度   # driver.swipe（分别表示滑动的起始和终点位置的 x/y 坐标）
        time.sleep(0.5)     # 系统反应也需要时间，此处sleep()不可省略

    TouchAction(driver).press(x=995, y=129).release().perform()  # 右上角退出,蚂蚁森林
    time.sleep(2)
    print('正在打开蚂蚁森林')
    TouchAction(driver).press(x=544, y=706).release().perform()


def waterTogetherPlant():

    items = driver.find_elements_by_class_name("android.widget.Button")
    for i in items:
        if '合种' in i.text:
            i.click()
            time.sleep(0.5)
            break
    time.sleep(1)
    TouchAction(driver).press(x=942, y=1992).release().perform()  # 点击去浇水(2015064)
    time.sleep(1)
    for ii in range(1,52):
        TouchAction(driver).press(x=330, y=1159).release().perform()  # 减号，到10克
        time.sleep(0.1)
    time.sleep(1)
    TouchAction(driver).press(x=715, y=1356).release().perform()  # 确定浇水2015064
    time.sleep(3)
    TouchAction(driver).press(x=656, y=2017).release().perform()    # 下一个合种
    time.sleep(2)
    TouchAction(driver).press(x=942, y=1992).release().perform()    # 点击去浇水(小梦雨)
    time.sleep(1)
    for ii in range(1,52):
        TouchAction(driver).press(x=750, y=1155).release().perform()    # 加号，加到520g
        time.sleep(0.1)
    time.sleep(1)
    TouchAction(driver).press(x=715, y=1356).release().perform()    # 确定浇水（小梦雨）
    time.sleep(3)
    TouchAction(driver).press(x=69, y=138).release().perform()      # 左上角返回，退出合种界面

''' -------------- 修改处 ------------- '''

SelfEnergyID = 1        # 取自己能量
FriendEnergy = 1        # 偷好友能量
RaiseChicken = 1        # 给小鸡喂食
WaterPlantHZ = 10        # 给合种浇水

start = time.perf_counter()         # 计算程序运行时间

if SelfEnergyID == 1:
    getSelfEnergy()
if FriendEnergy == 1:
    stealFriendEnergy()
if RaiseChicken == 1:
    raiseChicken()
if WaterPlantHZ == 1:
    waterTogetherPlant()

end = time.perf_counter()
tim = end - start
txtshow = '偷能量完成，运行这段代码用时：{:.6f}秒'.format(tim)
print(txtshow)
showinfo(title='提示', message=txtshow)