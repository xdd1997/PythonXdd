#python123
#xdd1997
#奇数星号

a =eval(input())
if a%2==1:
    for i in range(a):
        if i%2 == 0:
            print(('*'*(i+1)).center(a,' '))
else:
    print('请输入奇数')

