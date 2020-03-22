#python123
#xdd1997
#绘制正方形
#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)    #设置画布大小及画笔初始位置
turtle.penup()                      #抬起画笔
#turtle.fd(-250)                     #前进-250
turtle.pendown()                    #落笔
turtle.pensize(5)                  #设置笔尖粗细
turtle.pencolor("purple")
long = 40
angle = 90
for i in range(4):
    turtle.fd(long)
    turtle.seth(angle*(i+1))
turtle.done()
