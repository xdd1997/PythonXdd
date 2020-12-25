
import urllib.request
import requests
import os.path
import ctypes

def get_img_url(raw_img_url="https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url  # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url

def save_img(img_url, dirname):
    # 保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print('文件夹', dirname, '不存在，重新建立')
            # os.mkdir(dirname)
            os.makedirs(dirname)
        # 获得图片文件名，包括后缀
        basename = "bing.jpg"
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
    print("Save", filepath, "successfully!")

    return filepath

def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)

def main():
    dirname = "C:/一行数据/更换壁纸/"  # 图片要被保存在的位置
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)  # 图片文件的的路径
    print(filepath)
    set_img_as_wallpaper(filepath)
main()