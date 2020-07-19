# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timer2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 345)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 211, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_time = QtWidgets.QLabel(self.tab)
        self.label_time.setGeometry(QtCore.QRect(72, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_time.setToolTipDuration(-1)
        self.label_time.setObjectName("label_time")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 61, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(622)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 191, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_start.setEnabled(True)
        self.pushButton_start.setObjectName("pushButton_start")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_start)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.pushButton_stop = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_stop)
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_time.setText(_translate("Form", "Hello Yu"))
        self.pushButton_start.setText(_translate("Form", "开始"))
        self.pushButton_3.setText(_translate("Form", "暂停"))
        self.pushButton_stop.setText(_translate("Form", "停止"))
        self.pushButton_4.setText(_translate("Form", "复位并开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "倒计时"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "正计时"))
