import sys
import time as t
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from TimerXdd import Ui_Form  # TimerXdd为ui对于py文件的名字
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIntValidator




class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法

    def initUI(self):  # 定义初始化界面的方法
        #----------在右下角显示日期----------
        timeText =  t.strftime("%Y-%m-%d ", t.localtime())
        self.label_date.setText(timeText)
        # ---------- 计时器初始化 -------

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.show()

        # ---------- 设置窗口标题 图标(未成功） ---------
        self.setWindowTitle('Xdd Timer')
        #self.setWindowIcon(QIcon('https://images.cnblogs.com/cnblogs_com/xdd1997/1555655/t_myu.jpg?a=1592404473552'))  # 设置窗体标题图标
        #self.setWindowIcon(QIcon('/视频水印2.png'))


        #----------信号连接自定义的槽---------
        self.pushButton_start1.clicked.connect(self.StartTime)
        self.pushButton_clean1.clicked.connect(self.btn_clean1_click)
        self.pushButton_cleanAndStart1.clicked.connect(self.btn_cleanAndStart1_click)

        self.pushButton_start2.clicked.connect(self.btn_start2_click)
        self.pushButton_clean2.clicked.connect(self.btn_clean2_click)
        self.pushButton_cleanAndStart2.clicked.connect(self.btn_cleanAndStart2_click)
        # ---------- 文本框限制只能输入整数 -----------
        self.lineEdit.setValidator(QIntValidator(0, 622))
    # ----------  在此处定义函数（槽）  ----------
    def StartTime(self):
        self.textBrowser_jishi.setText('ILOVEYOU')


    def btn_clean1_click(self):
        self.textBrowser_jishi.setText("")
        self.pushButton_start1.setEnabled(True)

    def btn_cleanAndStart1_click(self):
        self.textBrowser_jishi.setText("")
        self.pushButton_start1.setEnabled(True)

    # -----------  倒计时的自定义槽  -----------


    def Refresh(self):
        if self.count > 0:

            sec = self.count
            hour = int(sec / 3600)
            min = int(sec % 3600 / 60)
            s = sec % 60
            if hour < 10: hour = '0' + str(hour)
            if min < 10:  min = '0' + str(min)
            if s < 10:    s = '0' + str(s)
            stringTime = str(hour) + ':' + str(min) + ':' + str(s)

            self.textBrowser_daojishi.setText(stringTime)
            self.count -= 1
        else:
            self.time.stop()
            self.pushButton_start2.setEnabled(True)
            self.textBrowser_daojishi.setText('00:00:00')


    def btn_start2_click(self):
        '''
        if self.lineEdit.text().isEmpty():    #为空
            self.textBrowser_jishi.setText("请输入分钟")
            return
        else:
            '''
        self.textBrowser_daojishi.setText('ILOVEYOU')
        self.count = int(self.lineEdit.text() )* 60
        self.lineEdit.setReadOnly(True)  # 设置为只读
        print(self.count)

        if self.pushButton_start2.isEnabled():
            self.time.start()
            self.pushButton_start2.setEnabled(False)

    def btn_clean2_click(self):
        self.time.stop()
        self.textBrowser_daojishi.setText("")
        self.pushButton_start2.setEnabled(True)
        self.lineEdit.setReadOnly(False)  # 设置为只读
    def btn_cleanAndStart2_click(self):
        self.textBrowser_daojishi.setText("")
        self.time.stop()
        self.pushButton_start2.setEnabled(True)
        self.lineEdit.setReadOnly(False)  # 设置为只读
        self.btn_start2_click()

    #获取当前时间数字 修饰成00:00:00 格式以写入计时器文本框
    def num2hms(self):
        sec = self.count
        hour = int(sec / 3600)
        min = int(sec % 3600 / 60)
        s = sec % 60
        if hour<10:
            hour= '0'+str(hour)
        if min<10:
            min = '0'+str(min)
        if s<10:
            s = '0'+str(s)

        stringTime = str(hour) +':' +str(min) +':'+str(s)
        return  stringTime

    def restart_program():
        python = sys.executable
        os.execl(python, python, *sys.argv)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字
    main_form.show()
    sys.exit(app.exec_())
