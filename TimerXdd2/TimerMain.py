
import sys
from Timer2 import Ui_Form  # Timer2为ui对于py文件的名字
from PyQt5.QtWidgets import QDialog,QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import  time
import tkinter as tk

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法

    def initUI(self):  # 定义初始化界面的方法
        # ----------信号连接自定义的槽---------
        self.pushButton_start.clicked.connect(self.btn_start_click)
        self.pushButton_stop.clicked.connect(self.btn_stop_click)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)


    def btn_start_click(self):
        self.label_time.setText('ILOVEYOU')
        self.count = int(self.spinBox.text()) * 60
        # self.lineEdit.setReadOnly(True)  # 设置为只读
        print(self.count)

        if self.pushButton_start.isEnabled():
            self.time.start()


    def btn_stop_click(self):
        self.time.stop()


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

            self.label_time.setText(stringTime)
            self.count -= 1
        else:
            self.time.stop()
            self.pushButton_start.setEnabled(True)
            self.label_time.setText('00:00:00')

            window = tk.Tk()
            window.title('My Window')
            l = tk.Label(window, text='你好,计时时间到了!', bg='blue', font=('Arial', 12), width=30, height=2)
            l.pack()
            window.mainloop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字,可更改等号前面名字
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    w = QDialog()
    main_form.show()
    sys.exit(app.exec_())
