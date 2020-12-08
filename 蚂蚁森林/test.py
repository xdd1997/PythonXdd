#  通过中间右下角“逛一逛‘’
import time
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
print('正在打开支付宝01')
driver = webdriver.Remote(server, desired_caps)  # 打开支付宝
time.sleep(4)
print('已打开支付宝，正在打开蚂蚁森林')
try:
    driver.find_element_by_xpath("//*[@text='蚂蚁森林']").click()  # 点击蚂蚁森林

    print('标签方式进入蚂蚁森林')
except:

    TouchAction(driver).press(x=535, y=750).release().perform()  # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多
    print('坐标方式进入蚂蚁森林')

# 点击蚂蚁森林（以id打开，这种较好，但是appium有些故障，刷新不出来
# driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
time.sleep(5)
''' ---------- 收取自己的能量 ---------- '''
items = driver.find_elements_by_class_name("android.widget.Button")
print(len(items))
print(items)




'''
try:
    print('正在收取自己能量')
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

# 在蚂蚁森林界面，向下滑，找到更多好友，点击 
print('正在搜一搜')
time.sleep(2)
iiquit = 0    # 用于控制无能量的次数
# ----------- 进入偷能量界面 ---------- 
flag = 0
while True:
    #driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
    TouchAction(driver).press(x=960, y=1580).release().perform()  # 搜一搜位置
    time.sleep(2) # 等一会让系统进入这个界面

    name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
    print('正在查看{0}'.format(name))
    items = driver.find_elements_by_class_name("android.widget.Button")
    print(len(items),'\n',items)

    if len(items) > 6:      # 执行此项是界面界面有东西（能量或者不可点能量）在自己的名字栏，因len(items）=0<5,会直接向上划过
        try:
            for i in items:
                if '能量' in i.text:
                    print('我点点')
                    i.click()
                    time.sleep(0.5)
                else:
                    iiquit = iiquit + 1
                    print(iiquit)
                    if iiquit > 150:
                        flag = 1
                        break
        except:
            pass
    else:
        break
    if flag == 1:
        break
driver = webdriver.Remote(server, desired_caps)  # 打开支付宝

end = time.perf_counter()
tim = end - start
txtshow = '偷能量完成，运行这段代码用时：{:.6f}秒'.format(tim)
print(txtshow)

'''