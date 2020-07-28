# untitled.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 322)
        self.label_state = QtWidgets.QLabel(Dialog)
        self.label_state.setGeometry(QtCore.QRect(20, 290, 191, 16))
        self.label_state.setObjectName("label_state")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(230, 230, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.lineEdit_username = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_username.setGeometry(QtCore.QRect(150, 50, 171, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(50, 50, 61, 16))
        self.label_username.setObjectName("label_username")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(150, 90, 171, 20))
        self.lineEdit_password.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(50, 90, 61, 16))
        self.label_password.setObjectName("label_password")

        self.retranslateUi(Dialog)
        self.btn_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_state.setText(_translate("Dialog", "TextLabel"))
        self.btn_ok.setText(_translate("Dialog", "ok"))
        self.btn_cancel.setText(_translate("Dialog", "cancel"))
        self.label_username.setText(_translate("Dialog", "User name"))
        self.label_password.setText(_translate("Dialog", "Password"))