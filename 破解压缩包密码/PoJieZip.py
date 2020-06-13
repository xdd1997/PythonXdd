import sys
import zipfile
import rarfile
import threading
import datetime
import os
import subprocess
import getopt

i = 0
fileGet = ""

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def extractFile(fileExtr, password, fileType):
    try:
        encodestr = str.encode(password)
        if (fileType == "zip"):
            fileExtr.extractall(pwd=str.encode(password))
        else:
            fileExtr.extractall(pwd=password)
        global i
        i = i + 1
        print("search count : %d,real password is : %s" % (i, password))
        return password
    except:
        i = i + 1
        print("search count : %d,test password : %s, err:%s" % (i, password, sys.exc_info()[0]))
        pass


def mainStep():
    path = input("please input path:")
	#输入方式如：F:\desktop\123456\001.zip

    try:
        if os.path.exists(path) == False:
            print("%s : path error!" % (path))
            return
        type = os.path.splitext(path)[-1][1:]
        if type == "zip":
            fileGet = zipfile.ZipFile(path)
            with fileGet as z:
                for l in z.infolist():
                    is_encrypted = l.flag_bits & 0x1
                    if is_encrypted:
                        print("have password ")
                        break
                    else:
                        pass
            fileGet = zipfile.ZipFile(path)

        elif type == "rar":
            fileGet = rarfile.RarFile(path)
            with fileGet as z:
                if z.needs_password():
                    print("have password ")
                else:
                    print("no password")
                    return
        else:
            print("file not right")
            return

        pwdLists = open("D:\File_Git\PythonXdd\破解压缩包密码\sixPassdict.txt")
        startTime = datetime.datetime.now()

        for line in pwdLists.readlines():
            Pwd = line.strip('\n')
            t = MyThread(extractFile, (fileGet, Pwd, type))
            t.start()
            if (t.get_result() is Pwd):
                break
        endTime = datetime.datetime.now()
        timeSpan = endTime - startTime
        print("search time:%ss" % (timeSpan.total_seconds()))

    except:
        print("err:%s" % sys.exc_info()[0])


if __name__ == '__main__':
    mainStep()