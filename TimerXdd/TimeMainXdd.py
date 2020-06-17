import sys
import time as t
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from TimerXdd import Ui_Form  # TimerXdd为ui对于py文件的名字
from PyQt5.QtCore import QTimer



class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法

    def initUI(self):  # 定义初始化界面的方法
        #----------在右下角显示日期----------
        timeText = '启动日期 ' + t.strftime("%Y-%m-%d ", t.localtime())
        self.label_date.setText(timeText)

        # ---------- 设置窗口标题 图标(未成功） ---------
        self.setWindowTitle('Xdd Timer')
        #self.setWindowIcon(QIcon('https://images.cnblogs.com/cnblogs_com/xdd1997/1555655/t_myu.jpg?a=1592404473552'))  # 设置窗体标题图标
        #self.setWindowIcon(QIcon('/视频水印2.png'))


        #----------信号连接自定义的槽---------
        self.pushButton_start1.clicked.connect(self.btn_start1_click)
        self.pushButton_clean1.clicked.connect(self.btn_clean1_click)
        self.pushButton_cleanAndStart1.clicked.connect(self.btn_cleanAndStart1_click)

        self.pushButton_start2.clicked.connect(self.btn_start2_click)
        self.pushButton_clean2.clicked.connect(self.btn_clean2_click)
        self.pushButton_cleanAndStart2.clicked.connect(self.btn_cleanAndStart2_click)

    # ----------  在此处定义函数（槽）  ----------
    def btn_start1_click(self):
        self.textBrowser_jishi.setText('ILOVEYOU')

    def btn_clean1_click(self):
        self.textBrowser_jishi.setText("")

    def btn_cleanAndStart1_click(self):
        self.textBrowser_jishi.setText("")

    # -----------  倒计时的自定义槽  -----------
    def btn_start2_click(self):
        self.textBrowser_daojishi.setText('ILOVEYOU')

    def btn_clean2_click(self):
        self.textBrowser_daojishi.setText("")

    def btn_cleanAndStart2_click(self):
        self.textBrowser_daojishi.setText("")

    #获取当前时间以写入计时器文本框







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字
    main_form.show()
    sys.exit(app.exec_())
