import turtle
import time
def drawLine(draw): #绘制单段数码管
    turtle.pendown() if draw else  turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDight(digit):   #根据数字绘制晶体管
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)  #第一条线绘制情况
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
def drawDate(date): #解析获得时间中的数字
    for i in date:
        drawDight(eval(i))
def main ():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20191020')
    turtle.hideturtle()
    turtle.done() 
main()
