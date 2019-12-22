#python123
#xdd1997
#2019-12-22

import turtle as t
import time
def drawGap(): #绘制数码管间隔
    t.penup()
    t.fd(5)#两条线的对角处距离
def drawLine(draw):   #绘制单段数码管
    drawGap()
    t.pendown() if draw else t.penup() #如果draw=ture就落笔，=false就提起笔
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False) #gg 中间横线
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False) #cc 右下竖线
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False) #c
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False) #aaa
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
    time.sleep(0.2)
def drawDate(date):
    t.pencolor("red")
    for i in date:
            drawDigit(eval(i))
def main():
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-300) #海龟初始在画布中心，后退300，笔尖朝向不变
    t.pensize(5)
    #drawDate(time.strftime('%Y%m%d',time.gmtime()))
    drawDate('3325655')
    t.done()
main()