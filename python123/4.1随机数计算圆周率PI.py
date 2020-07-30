#python123
#xdd1997
#随机数计算圆周率
from random import random, seed

DARTS = eval(input()) #进行的次数，撒点的次数
seed(123) #设种子，可复现；若不设，则默认以当前时间作为种子，则将不可复现
hits = 0.0
for i in range(DARTS):
    x, y = random(), random()#随机产生【0,1）小数
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("{:.9f}".format(pi))