# run.py

from PyQt5 import QtWidgets
from untitled import Ui_Dialog
from information_ok import Ui_Form as form_ok
from information_no import Ui_Form as form_no


class mywindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.printState)

    def printState(self):
        # 显示状态
        #        if self.lineEdit_username.text == "1" and self.lineEdit_password.text == "1":
        if self.lineEdit_username.text().strip() == "1" and self.lineEdit_password.text() == "1":
            words = "Login successful!"
            self.w1 = window_ok()
            self.w1.show()
            self.close()
        else:
            words = "Login faild!"
            self.w2 = window_no()
            self.w2.show()
            self.close()
        self.label_state.setText(words)


class window_ok(QtWidgets.QWidget, form_ok):
    def __init__(self):
        super(window_ok, self).__init__()
        self.setupUi(self)


class window_no(QtWidgets.QWidget, form_no):
    def __init__(self):
        super(window_no, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    #    input("input something")
    sys.exit(app.exec_())