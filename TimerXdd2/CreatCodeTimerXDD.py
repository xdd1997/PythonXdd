
from tkinter import *
from Cryptodome.Cipher import DES
import binascii
import pyperclip
import tkinter.messagebox
import webbrowser

# pyinstaller -F -w "CreatCodeTimerXDD.py"
class App:
    def __init__(self, master):

        # 使用Frame添加容器
        frame0 = Frame(master)
        lb_time0 = Label(frame0, text=u'注册机', font=('微软雅黑', 20), padx=7)
        # 采用grid网格布局，添加控件
        lb_time0.grid(row=0, column=0, sticky=E)  # W 西对齐（左对齐）
        frame0.pack(side=TOP, padx=0)

        frame1 = Frame(master)
        # 采用grid网格布局，添加控件
        lb_id = Label(frame1, text=u'注册ID：', font=('微软雅黑', 12), padx=7)
        lb_id.grid(row=0, column=0, sticky=W)        # W 西对齐（左对齐）
        lb_code = Label(frame1, text=u'注册码：', font=('微软雅黑', 12), padx=7)
        lb_code.grid(row=1, column=0, sticky=W)


        self.en_id = Entry(frame1, font=('微软雅黑', 13), width=15, show=None)
        self.en_code = Entry(frame1, font=('微软雅黑', 13), width=15, show=None)
        self.en_id.grid(row=0, column=1, columnspan=2,sticky=W)
        self.en_code.grid(row=1, column=1, columnspan=2,sticky=W)
        frame1.pack()

        frame2 = Frame(master)
        btn_zhuce = Button(frame2, text=u'注册',padx=10, bg='light blue', font=('微软雅黑', 15, ), fg='white',command=self.ZhuCeBtn)
        btn_zhuce.grid(row=2, column=1, sticky=W, pady=10)
        btn_help = Button(frame2, text="帮助", padx=10,bg='pink', font=('微软雅黑', 15), fg='white', command=self.ZhuCehelp)
        btn_help.grid(row=2, column=2, sticky=E, pady=5)
        btn_exit = Button(frame2, text="退出", bg='cyan', font=('微软雅黑', 15), fg='white', command=self.exit_btn)
        btn_exit.grid(row=2, column=3, sticky=E, pady=5)
        frame2.pack(pady=0)

    def ZhuCehelp(self):
        try:
            webbrowser.open("https://support.qq.com/products/173442")
            print('正在打开帮助网站')
        except:
            tkinter.messagebox.showinfo('提示', '无网络，请联网')

    def exit_btn(self):
        root.destroy()

    def get_ZhuCeCode(self):
        macID = self.en_id.get()
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
            self.zhuceCode =zhuceCode
        except:
            zhuceCode = '注册ID应为8位'
            self.zhuceCode =zhuceCode

    def ZhuCeBtn(self):
        self.get_ZhuCeCode()
        self.en_code.delete(0, 'end')
        self.en_code.insert(0, self.zhuceCode)
        pyperclip.copy(self.zhuceCode)
        if (self.zhuceCode !='') & (self.zhuceCode!='注册ID应为8位'):
            tkinter.messagebox.showinfo('提示', '注册码已经复制到粘贴板')
        else:
            tkinter.messagebox.showinfo('提示', '请输入注册ID')


win = Tk()
win.title("TimerXdd 注册机")
app = App(win)
screenwidth = win.winfo_screenwidth()  # 窗口居中
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (300, 180, (screenwidth - 300) / 2, (screenheight - 200) / 2)
win.geometry(alignstr)
win.wm_attributes('-topmost', 1)  # 窗口置顶
win.mainloop()
