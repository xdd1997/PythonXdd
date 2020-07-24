# 2020-07-24     xdd2026@qq.com   TimerXdd的生成激活码窗口
#  pyinstaller -F -w "CreatCode.py"
import tkinter as tk  # 使用Tkinter前需要先导入
from Cryptodome.Cipher import DES
import binascii


def get_ZhuCeCode():
    macID = e1.get()
    print(macID)
    try:
        # 密钥：必须为8字节
        key = b'xdd19976'
        # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
        des = DES.new(key, DES.MODE_ECB)
        # 加密
        result = des.encrypt(macID.encode())
        # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
        tt = binascii.b2a_hex(result)
        # 转为字符串
        zhuceCode = str(tt, 'utf-8')
        print(zhuceCode)
        return zhuceCode
    except:
        zhuceCode = '注册ID为8位,请重新获取ID'
        return zhuceCode

def ZhuCeBtn():
    global e1
    global e2
    macCode = get_ZhuCeCode()
    e2.delete(0, 'end')
    e2.insert(0, macCode)

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
    window.geometry('300x180')  # 这里的乘是小x
    tk.Label(window, text='注册窗口', font=('华文行楷', 16)).place(x=80, y=5)
    tk.Label(window, text='注册ID:', font=('华文行楷', 14)).place(x=10, y=37)
    tk.Label(window, text='注册码:', font=('华文行楷', 14)).place(x=10, y=80)
    e1 = tk.Entry(window, show=None)
    e1.place(x=120, y=40)  # 显示成明文形式    输入框
    e2 = tk.Entry(window, show=None)
    e2.place(x=120, y=85)  # 显示成明文形式    输入框
    b1 = tk.Button(window, text='生成', width=10, height=2, command=ZhuCeBtn).place(x=60, y=120)  # 方法要在这条语句前面
    b2 = tk.Button(window, text='清空', width=10, height=2, command=ZhuCeclean).place(x=180, y=120)  # 方法要在这条语句前面
    window.mainloop()

ShowZhuCeFig()




