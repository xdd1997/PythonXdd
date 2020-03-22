"""
可以遍历输入的路径的指定后缀的文件,主要是用来筛选图片,将图片分成
横屏,竖屏分别存放在两个文件夹中
"""
#安装模块
'''
pip install image
pip install tqdm
pip install shutil
'''

from PIL import Image
import os
import os.path
from tqdm import tqdm
import shutil
#函数查找指定路径中所有文件的路径
#函数查找指定路径中所有文件的路径
def get_file(path):
    list1=[]#用于存储递归查找到的所有文件,传递给函数
    fileList = os.listdir(path)  # 获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename) # 获取path与filename组合后的路径
        if os.path.isdir(pathTmp):  # 如果是目录
            a=get_file(pathTmp) # 则递归查找(注意一定要有接受变量,不然就出错了)
            for i in a:
                list1.append(i)
        else: 
            list1.append(pathTmp)
    return list1
#---------------------修改处1,修改原始文件位置------------------------------------
#path = input('请输入路径：').strip()  #.strip()去除首尾的空格
path = r'F:\桌面\一见倾心系列'  #待分开文件的位置

file_path_list=get_file(path)

#筛选后缀函数,传入包含所有后缀名的列表,以及需要筛选的后缀(默认筛选txt文件)
def shai_xuan_hou_zhui(file_path_list,hou_zhui='.txt'):
    
    list2=[]  #用于储存筛选好的文件的路径
    for filepath in file_path_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(filepath)[1] == hou_zhui:
            list2.append(filepath)
    #        print(filepath +'\n')
    
    return list2
#----------------------修改2，修改文件后缀，(可完善）------------------------------------
# hou_zhui='.jpg'
# py_list=shai_xuan_hou_zhui(file_path_list,'.py')  #筛选py文件
pig_list=shai_xuan_hou_zhui(file_path_list,'.jpg')   #筛选jpg格式文件
# print(txt_list)
#-----------------------修改处3，修改图片存储路径-------------------------------
folder1=r'F:\桌面\一见倾心系列\heng'  #存放横屏图片的地址
folder2=r'F:\桌面\一见倾心系列\shu'   #存放竖屏图片的地址

for i in tqdm(range(len(pig_list))):
    lujing=pig_list[i]
    picture=Image.open(lujing)
    width=picture.width
    height=picture.height
    picture.close()
    if width > height:
        shutil.move(lujing,folder1)
        print('正在处理横屏')
    else:
        shutil.move(lujing,folder2)
        print('正在处理竖屏')

print('over,over,over!')
