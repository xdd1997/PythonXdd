#python123
#xdd1997
#绘制蟒蛇
#详解 https://blog.csdn.net/qq_40181592/article/details/86770960
#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)    #设置画布大小及画笔初始位置
turtle.penup()                      #抬起画笔
turtle.fd(-250)                     #前进-250
turtle.pendown()                    #落笔
turtle.pensize(25)                  #设置笔尖粗细
turtle.pencolor("purple")
turtle.seth(-40)                    #转向-40°（右转40°)

for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()