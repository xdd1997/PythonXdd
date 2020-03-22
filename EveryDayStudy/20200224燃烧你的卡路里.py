#编写一个程序，输入体重（KG）、跑步时间（分钟）、跑步速度（公里/小时），可以计算跑步距离和消耗的卡路里
# 。消耗卡路里＝体重（kg）×运动时间（小时）×指数K。指数K＝30÷速度（分钟/400米），输出效果如图所示。
#2020-02-29
#edit by xdd

print ("========燃烧你的卡路里========")
print (30 *"#")
weight=eval(input("输入您的体重（KG）："))
speed=eval(input("速度（公里/小时）："))
times=eval(input("跑步时间（分钟）："))
CanShu1 = times/60 * speed
print("跑步距离（公里）:",format(CanShu1,'.2f' ))
#计算卡路里
K = 30 /(60/ (speed *1000/400))
KaLuLi = weight * (times/60) * K
print("燃烧卡路里:", format(KaLuLi,'.2f'  ))

'''
print ("========燃烧你的卡路里========")
print (30 *"#")
weight=float(input("输入您的体重（KG）：") )
speed=float(input("速度（公里/小时）："))
times=int(input("跑步时间（分钟）："))
dista=speed * times/60
calor =weight * 30/(400/(speed*1000/60)) * times/60
print("跑步距离（公里）:",format(dista,'.2f'))
print("燃烧卡路里:",format(calor,'.2f'))
'''