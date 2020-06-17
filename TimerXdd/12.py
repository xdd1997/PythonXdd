def startTimer (self):
    #发出计时信号
    self.timer.start(0)
# #如果self. pause-flag为假,更新开始时间
# #否则,更新重启时间
    if not self.pause_flag:
        self.start_time = self.current_time
     else:
         self.restart_time = self.current_time
         #设置按钮状态
    self.setPushButton(btn1=False, btn2=True, btn3=True)
def pauseTimer(self):
    self.pause_flag = True
    self.pause_time = self.current_time#停止发送信号
    self.timer.stop()
    self.setPushButton(btn1=True, btn2=False, btn3=True)
def clearTimer(self):#还原至初始状态
    self.init_setting()
    self.timer.stop()
    self.setPushButton()