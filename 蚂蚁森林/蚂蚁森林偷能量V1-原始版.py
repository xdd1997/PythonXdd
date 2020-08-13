import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
TouchAction(driver).press(x=544, y=706).release().perform()     # 蚂蚁森林的图标位置,我的在首页，不在的话，要先打开更多
# driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click() #点击蚂蚁森林（以id打开，这种较好，但是appium有些故障，刷新不出来
time.sleep(5)
print('------------------')
def Swipe(driver):
    n=0
    while n<=5:
        start_x = 500
        start_y = 1500
        distance = 1000
        driver.swipe(start_x, start_y, start_x, start_y - distance)
        n=n+1
    driver.find_element_by_xpath("//*[@text='查看更多好友']").click() #点击查看更多好友
    time.sleep(1)

def run(driver):
    Swipe(driver)  #仅执行一次，向下滑，找到更多好友，点击
    while True:
        TouchAction(driver).press(x=345, y=668).release().perform() #第一个蚂蚁好友框框的坐标
        time.sleep(0.5)

        name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
        if name=='小姑':      #填写最后一个好友昵称，不一定是最后一个，先填最后一个，看能遍历到哪一个
            driver.tap([(50, 130), (70, 150)], 100) #返回周排行榜主页( < 蚂蚁森林 )    driver.tap（x坐标,y坐标,t(ms)）
            time.sleep(1)
            driver.tap([(50, 130), (70, 150)], 100) #返回蚂蚁森林主页
            Swipe(driver)
            continue
        print('正在查看{0}'.format(name))
        items = driver.find_elements_by_class_name("android.widget.Button")
        if len(items)>5:
            for i in items:
                if '能量' in i.text:
                    print('收取{0}的{1}'.format(name,i.text.replace('收集','')))
                    i.click()

            time.sleep(0.5)
            driver.tap([(50, 130), (70, 150)], 100)
            time.sleep(0.1)

        start_x = 500
        start_y = 1910
        distance = 195  # 一个框的高度
        driver.swipe(start_x, start_y, start_x, start_y - distance)    # 向上滑动一个框的高度   # driver.swipe（分别表示滑动的起始和终点位置的 x/y 坐标）

        time.sleep(0.5)

if __name__ == '__main__':
    run(driver)