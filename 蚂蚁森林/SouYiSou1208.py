# 搜一搜版本
import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import winsound
# ------------------ 在能量球可能出现的地方疯狂点击 -------------------
def collect_energy(driver):
    name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
    if name=="蚂蚁森林":
        print('退出程序了')
        winsound.Beep(1000, 1000)
        os._exit(0)
    else:
        print('正在查看{0}'.format(name))
    # 获取手机屏幕宽高
    width = int(driver.get_window_size()['width'])
    height = int(driver.get_window_size()['height'])
    # 能量球可能出现的区域坐标
    start_x = 200
    end_x = 870
    start_y = 620
    end_y = 780
    for i in range(start_y, end_y, 100):
        for j in range(start_x, end_x, 100):
            tap_x1 = int((int(j) / width) * width)
            tap_y1 = int((int(i) / height) * height)
            # 点击指定坐标
            driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], 1000)
        driver.tap([(732, 942), (732, 942)], 1000)    # 关闭点开的小树装饰


# ---------- 打开支付宝，点击搜能量 ----------
def main():

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
    print('正在打开支付宝01')
    try:
        driver = webdriver.Remote(server, desired_caps)  # 启用两次，是因为锁屏打开手机一次有可能打不开
    except:
        print('查看Appium是否开启')
        os._exit(0)   # stop program

    time.sleep(4)
    print('正在打开蚂蚁森林')
    try:
        driver.find_elements_by_id('com.alipay.android.phone.openplatform:id/home_app_view')[7].click()
        print("id进入蚂蚁森林")
    except:
        driver.find_element_by_xpath("//*[@text='蚂0蚁森林']").click()  # 点击蚂蚁森林
        print("xpath进入蚂蚁森林")
        # TouchAction(driver).press(x=544, y=706).release().perform()  # 蚂蚁森林的图标位置,
    time.sleep(2)
    ''' ---------- 收取自己的能量 ---------- '''
    try:
        width = int(driver.get_window_size()['width'])
        height = int(driver.get_window_size()['height'])
        # 能量球可能出现的区域坐标
        start_x = 200
        end_x = 870
        start_y = 620
        end_y = 780
        for i in range(start_y, end_y, 100):
            for j in range(start_x, end_x, 100):
                tap_x1 = int((int(j) / width) * width)
                tap_y1 = int((int(i) / height) * height)
                # 点击指定坐标
                driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], 1000)
            driver.tap([(732, 942), (732, 942)], 1000)  # 关闭点开的小树装饰
    except:
        pass

    print('正在搜一搜')
    time.sleep(2)
    iiquit = 0    # 用于控制无能量的次数
    # ----------- 进入偷能量界面 ---------- '''
    flag = 0
    while True:
        #driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
        TouchAction(driver).press(x=991, y=1582).release().perform() # 找能量位置
        time.sleep(2) # 等一会让系统进入这个界面
        try:
            collect_energy(driver)
        except:
            pass


# ----------------- run script --------------------
main()


