'''
import math
xiazai = 1000
b = xiazai / (34 - math.log(xiazai + 1)/math.log(2))
print(b)
'''

#求exp(x) = 10^308
import math
x = 0
while(1):
    x +=1
    if pow(math.e,x)>pow(10,304):
        break
print('x=',x)
print(pow(math.e,x))
#x=700
#1.0142320547349667e+304
print(pow(math.e,709))
#8.218407461554662e+307





