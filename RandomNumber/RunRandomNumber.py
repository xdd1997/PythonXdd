import sys
import random
from PyQt5 import QtWidgets
from RandomNum_ui import Ui_Form

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def btnCreat_click(self):
     #  self.textdisplay.setText("你点击了按钮\n")
     try:
        min = eval(self.editMin.text())
        max = eval(self.editMax.text())
        counter = eval(self.editCounter.text())
        #print(min ,max ,counter)
      #  random.seed(622)  # 加上这一句会发现每次运行产生的随机数相同，数值是任意的
        result=''
        for i in range(counter):
            a = random.randint(min, max)
            result = result+ str(a)+'\t'
        print(result)
        self.textdisplay.setText(result)

        #\033[显示方式;前景色;背景色m要打印的字符串\033[0m
        #'  1    \033[1;;42m result  \033[0m '

     except:
        self.textdisplay.setText('请正确输入整数')

    def editCounter_Finish(self):
        try:
            counter = int(self.editCounter.text())

            if counter == 1:
                print('xdd')
                self.rbtnChongFu.setEnabled(False)
                self.rbtnSingle.setEnabled(False)
                #setEnabled(False)
                #if self.single_radioButton.isChecked():
            else:
                self.rbtnChongFu.setEnabled(True)
                self.rbtnSingle.setEnabled(True)
        except:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())