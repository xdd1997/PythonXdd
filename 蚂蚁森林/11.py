from appium import webdriver
import time

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'MI 6X'
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = 'AlipayLogin'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)


def get_screen_size():
    x = driver.get_window_size()['width']  # 获取屏幕宽度
    y = driver.get_window_size()['height']  # 获取屏幕高度
    return (x, y)


# 在首页找到【蚂蚁森林】的入口，点击进入
def get_home_view_by_text_then_click(driver, tag):
    home_app_view_list = driver.find_elements_by_id('com.alipay.android.phone.openplatform:id/home_app_view')
    home_len = len(home_app_view_list)
    for i in range(0, home_len):
        home_app_view_text = home_app_view_list[i].find_element_by_id(
            'com.alipay.android.phone.openplatform:id/app_text').text
        print(home_app_view_text)
    for i in range(0, home_len):
        home_app_view_text = home_app_view_list[i].find_element_by_id(
            'com.alipay.android.phone.openplatform:id/app_text').text
        if home_app_view_text == tag:
            print('-------------------------------------')
            print(str(tag) + '->' + str(i))
            print('点击【' + home_app_view_text + '】')
            home_app_view_list[i].click()
            break


# 通用的查找指定元素并点击的方法
def get_common_view_by_class_then_click(driver, tag):
    common_app_view_list = driver.find_elements_by_class_name('android.view.View')
    common_len = len(common_app_view_list)
    # for i in range(0,common_len):
    #     common_app_view_text = common_app_view_list[i].get_attribute('name')
    #     if common_app_view_text:
    #         print(common_app_view_text)
    for i in range(0, common_len):
        common_app_view_text = common_app_view_list[i].get_attribute('name')
        if common_app_view_text == tag:
            print('-------------------------------------')
            print(str(tag) + '->' + str(i))
            print('点击【' + common_app_view_text + '】')
            common_app_view_list[i].click()
            break


# 实现一次按坐标进行的点击
def tap_alone(x, y, duration=1000):
    l = get_screen_size()
    width = int(l[0])  # 获取屏幕宽度
    height = int(l[1])  # 获取屏幕高度
    tap_x1 = int((int(x) / width) * width)
    tap_y1 = int((int(y) / height) * height)
    print('点击坐标:[' + str(tap_x1) + ', ' + str(tap_y1) + ']')
    driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], duration)


# 实现一次收取能量
def tap_get_energy():
    # 能量球可能出现的区域坐标
    start_x = 120
    start_y = 470
    end_x = 920
    end_y = 870

    print('开始收取能量>>>')
    # 依次点击指定区域内的等距离坐标点
    for i in range(start_y, end_y, 80):
        for j in range(start_x, end_x, 80):
            print('[' + str(j) + ', ' + str(i) + ']', "\t", end="")
            tap_alone(j, i)
        print()


# 遍历获取好友列表
def get_friend_view_by_class_then_click(driver):
    time.sleep(1)
    for i in range(0, 16):
        print(str(i))
        swipeUp(2000, 500, 3000)
    for i in range(0, 16):
        print(str(i))
        swipeDown(500, 2000, 3000)
    time.sleep(1)

    swipeUp(2000, 1800)
    time.sleep(1)

    friend_view_square = driver.find_element_by_id('J_rank_list')
    friend_view_list = friend_view_square.find_elements_by_class_name('android.view.View')
    common_len = len(friend_view_list)
    print(common_len)
    print('-------------------------------------')
    count = 0
    for i in range(0, common_len):
        friend_view_view_text = friend_view_list[i].get_attribute('name')
        if friend_view_view_text:
            # print(friend_view_view_text)
            if count % 10 == 0 and count != 0:
                count = 0
                print('向上划一页')
                swipeUp(2000, 120)
                time.sleep(1)
            # if '获得了' in friend_view_view_text and count<10:
            if 'g' in friend_view_view_text:
                print('-------------------------------------')
                print('收取【' + friend_view_list[i - 2].get_attribute('name') + '】的能量>>>')
                friend_view_list[i].click()
                count += 1
                # print(count)
                time.sleep(1)
                tap_get_energy()
                driver.press_keycode(4)

    # for i in range(0,common_len):
    #     friend_view_view_text = friend_view_list[i].get_attribute('name')
    #     if friend_view_view_text:
    #         print('-------------------------------------')
    #         print(str(friend_view_view_text) + '->' + str(i))
    #         print('点击【' + friend_view_view_text + '】')
    #         friend_view_list[i].click()


# 实现安坐标精准滑动：向上滑动
def swipeUp(y1, y2, duration=5000):
    l = get_screen_size()
    width = int(l[0])  # 获取屏幕宽度
    height = int(l[1])  # 获取屏幕高度
    x1 = int(width * 0.5)
    y1_start = int((int(y1) / height) * height)
    y2_end = int((int(y2) / height) * height)
    driver.swipe(x1, y1_start, x1, y2_end, duration)
    print('向上滑动【' + str(y1_start - y2_end) + '】')


# 实现安坐标精准滑动：向下滑动
def swipeDown(y1, y2, duration=5000):
    l = get_screen_size()
    width = int(l[0])  # 获取屏幕宽度
    height = int(l[1])  # 获取屏幕高度
    x1 = int(width * 0.5)
    y1_start = int((int(y1) / height) * height)
    y2_end = int((int(y2) / height) * height)
    driver.swipe(x1, y1_start, x1, y2_end, duration)
    print('向下滑动【' + str(y2_end - y1_start) + '】')


# 点击【蚂蚁森林】
get_home_view_by_text_then_click(driver, '蚂蚁森林')
time.sleep(5)

# 收取自己的能量
tap_get_energy()
time.sleep(3)

# 滑动屏幕，找到【好友排行榜】
swipeUp(2000, 100)
time.sleep(1)
swipeUp(2000, 1100)
time.sleep(1)
# 点击进入【好友排行榜】
get_common_view_by_class_then_click(driver, '查看更多好友')
# 开始收取好友列表中好友的能量
get_friend_view_by_class_then_click(driver)

time.sleep(5)
driver.quit()