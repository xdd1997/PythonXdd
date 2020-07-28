import os
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import uuid
from Cryptodome.Cipher import DES
import binascii
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


def get_ZhuCeId():
   # 获取本机 Mac  加密Mac
   mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
   mac =  ":".join([mac[e:e+2] for e in range(0,11,2)])
   #对 Mac 加密
   mac2 = mac.replace(":", '6')
   if len(mac2) == 17:
       mac3 = mac2[0:17:2]
       mac3 = mac2[0:8]
   else:
       if len(mac2) % 8 != 0:
           mac3 = mac2 + "+" * (8 - len(mac2) % 8)
   macID = mac3
   return macID

def get_ZhuCeCode():
    macID = get_ZhuCeId()
    if len(macID) % 8 != 0:
        macID = macID + "+" * (8 - len(macID) % 8)
    print(macID)
    # 密钥：必须为8字节
    key = b'xdd19976'
    # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
    des = DES.new(key, DES.MODE_ECB)
    # 加密
    result = des.encrypt(macID.encode())
    print('加密后的数据：', result)
    # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
    tt = binascii.b2a_hex(result)
    # 转为字符串
    zhuceCode = str(tt, 'utf-8')
    print(zhuceCode)
    return zhuceCode

def ZhuCeBtn():
    global e1
    global  e2
    global flag

    txt = e2.get()
    macCode = get_ZhuCeCode()
    if txt==macCode:
        tkinter.messagebox.showinfo('提示', '注册成功,请关闭注册窗口')
        flag = 1
        with open("c:\\timerXdd\\code.txt", mode='w', encoding='utf-8') as ff:
            ff.write(macCode)
    else:
        tkinter.messagebox.showinfo('提示', '注册码错误')
        flag = 0

def ZhuCehelp():
    try:
        QDesktopServices.openUrl(QUrl("https://support.qq.com/products/173442"))
        print('正在打开帮助网站')
    except:
        tkinter.messagebox.showinfo('提示', '无网络，请联网')

def ZhuCeclean():

    global e2
    e2.delete(0, 'end')

def ShowZhuCeFig():
    global e1
    global e2
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    window.title('欢迎来到注册世界')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('300x200')  # 这里的乘是小x
    window.wm_attributes('-topmost', 1)  # 置顶
    tk.Label(window, text='注册窗口', font=('微软雅黑', 16)).place(x=80, y=5)
    tk.Label(window, text='注册ID:', font=('微软雅黑', 14)).place(x=10, y=37)
    tk.Label(window, text='注册码:', font=('微软雅黑', 14)).place(x=10, y=80)
    tk.Label(window,bg='lightblue',text='发送ID至 xdd2026@qq.com 获取激活码', font=('微软雅黑', 10)).place(x=10, y=120)
    e1 = tk.Entry(window, show=None)
    e1.place(x=120, y=40)  # 显示成明文形式    输入框

    e2 = tk.Entry(window, show=None)
    e2.place(x=120, y=85)  # 显示成明文形式    输入框

    b1 = tk.Button(window, text='注册', bg='lightblue', width=7, height=1, font=('微软雅黑', 12), command=ZhuCeBtn).place(x=30, y=150)  # 方法要在这条语句前面
    b2 = tk.Button(window, text='清空', bg='lightblue', width=7, height=1, font=('微软雅黑', 12),command=ZhuCeclean).place(x=120, y=150)  # 方法要在这条语句前面
    b3 = tk.Button(window, text='帮助', bg='lightblue', width=7, height=1, font=('微软雅黑', 12), command=ZhuCehelp).place(x=210, y=150)  # 方法要在这条语句前面


    macID = get_ZhuCeId()
    e1.insert(0, macID)
    screenwidth = window.winfo_screenwidth()     # 窗口居中
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (300, 200, (screenwidth - 300) / 2, (screenheight - 200) / 2)
    window.geometry(alignstr)
    window.mainloop()
def OpenZhuCe():
    global flag
    flag = 0
    if os.path.exists('c:\\timerXdd\\code.txt'):
        with open('c:\\timerXdd\\code.txt', mode='r', encoding='utf-8') as ff:
            codeRead = ff.readline()
            realCode = get_ZhuCeCode()
            if codeRead==realCode:
                print(codeRead)
                pass
            else:
                ShowZhuCeFig()
                if flag != 1:
                    os._exit(0)
    else:
        folder = os.path.exists("c:\\timerXdd")
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs("c:\\timerXdd")  # makedirs 创建文件时如果路径不存在会创建这个路径
        with open("c:\\timerXdd\\code.txt", mode='w', encoding='utf-8') as ff:
            print("文件创建成功！")
        ShowZhuCeFig()
        if flag != 1:
            os._exit(0)

OpenZhuCe()
# 主程序



