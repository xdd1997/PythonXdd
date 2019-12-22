#python123
#xdd1997
#天天向上
base = 1.0
A = (base + 0.01)**365
def Bup(rate):
    base = 1.0
    for i in range(365):
        if i % 7 in(6,0):
            base = base*(1-0.01)
        else:
            base = base*(1+rate)
    return base
i = 0
B = 0
while(1):
    print(A,'   ',B)
    if B>A:

        print('I= ',"%.3f" % i)
        break
    else:
        B = Bup(i)
        i+=0.000001
        #

