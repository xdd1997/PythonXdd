import sys
from EnergyForm import Ui_Form  # Timer2为ui对于py文件的名字
from PyQt5 import QtCore, QtWidgets




# pyinstaller -F -w "ZhaoEnergyApp.py"

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法

    def initUI(self):  # 定义初始化界面的方法
        # ----------信号连接自定义的槽---------
        self.pushButton_start.clicked.connect(self.btn_start_click)

    def btn_start_click(self):
        # 粘贴程序的地方
        # 搜一搜版本

        import os
        import time
        from appium import webdriver
        from appium.webdriver.common.touch_action import TouchAction
        import winsound
        # ------------------ 在能量球可能出现的地方疯狂点击 -------------------
        def collect_energy(driver):
            name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
            if name == "蚂蚁森林":
                print('退出程序了')
                winsound.Beep(1000, 1000)
                os._exit(0)
            else:
                print('正在查看{0}'.format(name))
                # 能量球可能出现的区域坐标
                start_x = 200
                end_x = 1080
                start_y = 620
                end_y = 800
                for y in range(start_y, end_y, 100):
                    for x in range(start_x, end_x, 100):
                        driver.tap([(x, y), (x, y)], 3000)
                        dx = int(x)
                        dy = int(y)
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置

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
                os._exit(0)  # stop program

            time.sleep(4)
            print('正在打开蚂蚁森林')
            try:
                driver.find_elements_by_id('com.alipay.android.phone.openplatform:id/home_app_view')[7].click()
                print("id进入蚂蚁森林")
            except:
                driver.find_element_by_xpath("//*[@text='蚂0蚁森林']").click()  # 点击蚂蚁森林
                print("xpath进入蚂蚁森林")
            time.sleep(2)
            ''' ---------- 收取自己的能量 ---------- '''

            try:
                # 能量球可能出现的区域坐标
                start_x = 200
                end_x = 1080
                start_y = 620
                end_y = 800
                for y in range(start_y, end_y, 100):
                    for x in range(start_x, end_x, 100):
                        driver.tap([(x, y), (x, y)], 3000)
                        dx = int(x)
                        dy = int(y)
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置
                TouchAction(driver).press(x=dx, y=dy).release().perform()  # 小树装饰位置

            except:
                pass
            print('正在搜一搜')
            time.sleep(2)
            # ----------- 进入偷能量界面 ---------- '''
            while True:
                # driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click()
                TouchAction(driver).press(x=920, y=1582).release().perform()  # 找能量位置
                time.sleep(1)
                TouchAction(driver).press(x=920, y=1582).release().perform()  # 找能量位置

                time.sleep(2)  # 等一会让系统进入这个界面

                try:
                    collect_energy(driver)
                except:
                    pass

        main()


if __name__ == '__main__':  # 四句话：继承-实例化-显示-退出

    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  # 实例化,类的名字,可更改等号前面名字 MyPyQT_Form()继承自Ui_Form
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 窗口置顶
    main_form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)  # 禁止窗口最大化
    main_form.setFixedSize(main_form.width(), main_form.height());  # 禁止拉伸窗口
    main_form.show()
    sys.exit(app.exec_())