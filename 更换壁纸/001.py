import ctypes
picture_path = 'C:/一行数据/更换壁纸/bing.jpg'



ctypes.windll.user32.SystemParametersInfoW(20, 0, picture_path, 3)