#encoding: utf-8
# 链接： https://blog.csdn.net/u010889616/article/details/78946568?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-7
import os


def writeResultAndPrint(fullPath):
    print (fullPath)
    file = open(resultFile,'a')
    file.write(fullPath)
    file.write("\n")
    file.close()


def findKey(fullPath):
    file = open(fullPath,'r')
    content = file.read()
    file.close()

    isExist = content.find(findId)
    if isExist > -1:
        global findCount
        findCount = findCount + 1
        writeResultAndPrint(fullPath)


def findFiles():
    for dirPath,dirNames,fileNames in os.walk(findDir):
        for file in fileNames:
            fullPath = os.path.join(dirPath,file)
            findKey(fullPath)
    print("找到了含字符串的文件个数 = " + str(findCount))


def clean():
    if os.path.exists(resultFile):
        os.remove(resultFile)


# ===================main============
findCount = 0
#   要查找的字符串，中文不行
findId = "clc"

# 要查找的文件夹
findDir = "D:\\test"

resultFile = os.path.join(findDir,"result.txt")
clean()
findFiles()
print('------------------------')

