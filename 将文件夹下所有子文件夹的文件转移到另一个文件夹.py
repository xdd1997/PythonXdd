# 将文件夹下所有子文件夹的文件转移到另一个文件夹
# https://blog.csdn.net/yangxinquan123/article/details/103326635

import os
import shutil
# ‪F:\desktop\123
#path = r"‪F:\desktop\123"
path = '‪F://desktop//123'
#path = 'D://BaiduNetdiskDownload//rock'
num = 0

for foot, dir, file in os.walk(path):
    if len(file) != 0:
        lujing = str(foot).split('\\')

        path = lujing[0] + '//' + lujing[1]
        for img_name in file:
            ori_pic_root = str(foot).replace('\\', '//')
            img = os.path.join(ori_pic_root, img_name)
            # 源图像地址
            img = str(img).replace('\\', '//')
            print(img)

            new_path = str(lujing[0]).replace('rock', 'new_rock').replace('//', '\\')
            new_path = os.path.join(new_path, lujing[1])

            ori_path = str(path).replace('//', '\\')
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            num += 1
            img_name = str(num) + '.JPG'
            new_img = os.path.join(new_path, img_name)
            # 新图像地址
            new_img = str(new_img).replace('\\', '//')
            print(new_img)
            print('-------------')
            shutil.move(img, new_img)
