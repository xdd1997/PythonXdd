import tkinter as tk
from tkinter import filedialog
from PIL import Image

#打开选择文件夹对话框
root = tk.Tk()
root.withdraw()

#Folderpath = filedialog.askdirectory() #获得选择好的文件夹
Filepath = filedialog.askopenfilename() #获得选择好的文件

#print('Folderpath:',Folderpath)
print('Filepath:',Filepath)


img = Image.open(Filepath)
#img = Image.open('F:\desktop\爬取的图片\pic.jpg')
(picW,picH) = img.size
# 欲裁剪为4*3
bili = 16/9
if picW/picH>=bili:
    print('weight pic')
    picW2 = picH*bili
    left = (picW-picW2)/2
    right = left + picH*bili
    upper = 0
    lower = picH
    cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
    #print(left, upper, right, lower)
else:
    print('height pic')
    picH2 = picW /bili
    left = 0
    upper = (picH - picH2) / 2
    right = picW
    lower = upper + picW / bili
    cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
cropped.save(Filepath)
img.show()