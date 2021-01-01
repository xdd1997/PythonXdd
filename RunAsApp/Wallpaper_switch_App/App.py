import sys
from wallpaper_switch import Ui_Wallpaper  # Timer2为ui对于py文件的名字
from PyQt5 import QtCore, QtWidgets




# pyinstaller -F -w "App.py"

class MyPyQT_Form(QtWidgets.QWidget,Ui_Wallpaper):
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
        import random
        import urllib.request
        import requests
        import os.path
        import ctypes
        import time
        from bs4 import BeautifulSoup

        def get_img_url():

            try:
                print("---------- 正在获取下载链接 ----------")
                num = random.randint(1, 26000)
                url = "http://www.netbian.com/desk/{}.htm".format(num)
                r = requests.get(url)
                demo = r.text
                soup = BeautifulSoup(demo, "html.parser")
                piclist = []
                for link in soup.find_all('img'):
                    link_list = link.get('src')
                    if link_list != None:
                        piclist.append(link_list)
                img_url = piclist[2]
                print('img_url:', img_url)
            except:
                img_url = "http://pic.netbian.com/uploads/allimg/190824/212516-15666531161ade.jpg"
            return img_url

        def save_img(img_url, dirname):
            try:
                if not os.path.exists(dirname):
                    print('文件夹', dirname, '不存在，重新建立')
                    # os.mkdir(dirname)
                    os.makedirs(dirname)
                # 获得图片文件名，包括后缀
                tt = time.strftime("%Y%m%d-%H%M", time.localtime())
                basename = tt + ".jpg"
                # 拼接目录与文件名，得到图片路径
                filepath = os.path.join(dirname, basename)
                # 下载图片，并保存到文件夹中
                print("---------- downloading ----------")
                urllib.request.urlretrieve(img_url, filepath)
            except:
                pass

            print("Save", filepath, "successfully!")

            return filepath

        def set_img_as_wallpaper(filepath):
            print("---------- 正在设置壁纸中 ---------")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)

        def main():
            dirname = "C:/wallpaper_switch/"  # 图片要被保存在的位置
            img_url = get_img_url()
            filepath = save_img(img_url, dirname)  # 图片文件的的路径
            print(filepath)
            set_img_as_wallpaper(filepath)

        main()


if __name__ == '__main__':  # 四句话：继承-实例化-显示-退出

    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  # 实例化,类的名字,可更改等号前面名字 MyPyQT_Form()继承自Ui_Form
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 窗口置顶
    main_form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)  # 禁止窗口最大化
    main_form.setFixedSize(main_form.width(), main_form.height())  # 禁止拉伸窗口
    main_form.show()
    sys.exit(app.exec_())