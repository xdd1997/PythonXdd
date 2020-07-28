 # Timer2为ui对于py文件的名字
import os
import sys
from PyQt5 import QtCore, QtWidgets
from TimerSetup import Ui_Form
import tkinter.messagebox
import tkinter as tk

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    # 下面这个方法自动执行，相当于初始化,但是可以自定义一个初始化函数 initUI()
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.initUI()   ## 此处给出了调用一般函数的方法


    def initUI(self):
        self.makecomboxBox()
        self.pushButton_save.clicked.connect(self.btn_save_click)

    def makecomboxBox(self):
        self.comboBox_1.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_1.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_1.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_1.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_1.addItem("偶数日")  # 先添加一个下拉菜单空位
        self.comboBox_1.currentIndexChanged.connect(self.comboBoxChange)
        print('*******************')

        self.comboBox_2.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_2.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_2.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_2.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_2.addItem("偶数日")  # 先添加一个下拉菜单空位

        self.comboBox_3.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_3.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_3.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_3.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_3.addItem("偶数日")  # 先添加一个下拉菜单空位

        self.comboBox_4.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_4.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_4.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_4.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_4.addItem("偶数日")  # 先添加一个下拉菜单空位

        self.comboBox_5.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_5.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_5.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_5.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_5.addItem("偶数日")  # 先添加一个下拉菜单空位

        self.comboBox_6.addItem("每天")  # 先添加一个下拉菜单空位
        self.comboBox_6.addItem("每小时")  # 先添加一个下拉菜单空位
        self.comboBox_6.addItem("仅一次")  # 先添加一个下拉菜单空位
        self.comboBox_6.addItem("奇数日")  # 先添加一个下拉菜单空位
        self.comboBox_6.addItem("偶数日")  # 先添加一个下拉菜单空位

    def btn_save_click(self):
        print('************------------------**********')
        txt1 = self.lineEdit_set1.text(); time1 = self.timeEdit_1.text(); box1 = self.comboBox_1.currentText()
        txt2 = self.lineEdit_set2.text(); time2 = self.timeEdit_2.text(); box2 = self.comboBox_2.currentText()
        txt3 = self.lineEdit_set3.text(); time3 = self.timeEdit_3.text(); box3 = self.comboBox_3.currentText()
        txt4 = self.lineEdit_set4.text(); time4 = self.timeEdit_4.text(); box4 = self.comboBox_4.currentText()
        txt5 = self.lineEdit_set5.text(); time5 = self.timeEdit_5.text(); box5 = self.comboBox_5.currentText()
        txt6 = self.lineEdit_set6.text(); time6 = self.timeEdit_6.text(); box6 = self.comboBox_6.currentText()
        list1 = [time1, '***',txt1 , '***', box1];list2 = [time2,'***',txt2,'***',box2];list3 = [time3,'***',txt3,'***',box3];
        list4 = [time4, '***',txt4, '***', box4];list5 = [time5,'***',txt5,'***',box5];list6 = [time6,'***',txt6,'***',box6];
        list=[list1,list2,list3,list4,list5,list6]
        listReal = []
        for li in list:
            print(li)
            if li[2] not in ['',' ','  ']:
                listReal.append(li)
        listWrite = sorted(listReal, key=lambda l: (l[0].split(':')[0], l[0].split(':')[1]))
        with open("c:\\timerXdd\\setupTime.txt", mode='w', encoding='utf-8') as ff:
            for li in listWrite:
                ff.writelines(li)
                ff.writelines('\n')
        self.showInformation('已经保存成功')


    def showInformation(self,txtShow):

        window = tk.Tk()
        print('-----------------')
        width = 300
        height = 100
        window.title('温馨提示')
        l = tk.Label(window, text=txtShow, bg='green', font=('Arial', 12), width=30, height=2)

        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window.geometry(alignstr)
        window.wm_attributes('-topmost', 1)  # 窗口置顶
        l.pack()
        window.mainloop()

    def panDuan(self):
        pass





    def comboBoxChange(self):
        box1 = self.comboBox_1.currentText()
        print(self.comboBox_1.currentText())
        return box1


if __name__ == '__main__':  # 四句话：继承-实例化-显示-退出

    app = QtWidgets.QApplication(sys.argv)
    main_form = MyPyQT_Form()  #实例化,类的名字,可更改等号前面名字 MyPyQT_Form()继承自Ui_Form
    main_form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)   # 窗口置顶
    main_form.show()
    sys.exit(app.exec_())
