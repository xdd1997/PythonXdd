from PIL import Image
img = Image.open('F:\desktop\爬取的图片\pic.jpg')
(picW,picH) = img.size
# 欲裁剪为4*3
bili = 4/3
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
cropped.save("F:\desktop\爬取的图片\pic.jpg")