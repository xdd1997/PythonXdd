# edit by xdd
# Before running this script, open appium.exe
# Reference site:https://www.cnblogs.com/deliaries/archive/2020/03/18/12410835.html

import time
import tkinter.messagebox
from appium import webdriver
#from selenium import webdriver   ## 可以代替上一行
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
driver.close_app()
time.sleep(2)
TouchAction(driver).press(x=715, y=1065).release().perform()     # 点击小米商城
time.sleep(10)
TouchAction(driver).press(x=927, y=1049).release().perform()     # 点击秒杀
time.sleep(2)

start_x = 500
start_y = 1500
distance = 1000
driver.swipe(start_x, start_y, start_x, start_y - distance)

for i in range(20):
    try:
        print(i)

        driver.find_element_by_xpath("//*[@text='日常元素抽纸 青春版 24包/箱']").click()  # 点击 小米公司十周年纪念T恤 十年款 白色 L i5 8GB内存 1T+128GB 1050Ti

        #TouchAction(driver).press(x=618, y=1533).release().perform()  # 点击衣服 # deltaH=590
        time.sleep(2)
        driver.find_element_by_xpath("//*[@text='立即抢购']").click()
        time.sleep(2)
        print('000')
    #    driver.find_element_by_xpath("//*[@text='结算(1)']").click()  # 结算  结算(1)   868 2022
        TouchAction(driver).press(x=868, y=2022).release().perform()
        time.sleep(1)
    #    driver.find_element_by_xpath("//*[@text='去付款']").click()  912 2048
        TouchAction(driver).press(x=912, y=2048).release().perform()
      #  driver.find_element_by_id("//*[@text='去付款']").click()
        print('111')
        break

    except:
        pass

print('***222')