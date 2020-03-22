#python123
#xdd1997
#2019-12-22

def cmul(a, *b):
    m = a
    for i in b:
        m *= i
    return m

#print(eval("cmul({})".format(input())))

def add (a,*b):
    sum = a
    for i in b:
        sum+=i
    return sum

str1 = input()
a = eval('cmul({})'.format(str1))
b = eval('add({})'.format(str1))
print(str(str1)+'这些数之和为'+str(b))
print(str(str1)+'这些数之积为'+str(a))