#python123
#xdd1997
#print('输入待转换的温度，以C或F结尾（不区分大小写)')
wendu1 = str(input())

if wendu1[0:1] in ('f', 'F'): #确定是华氏度
    wenduF = eval(wendu1[1:])
    # C = ( F - 32 ) / 1.8
    wenduC = "%.2f" % ((wenduF - 32) / 1.8)
    print('C'+wenduC)
elif wendu1[0:1] in ('c', 'C'):  # 确定是华氏度
    wenduC = eval(wendu1[1:])
    # F = C * 1.8 + 32
    wenduF = "%.2f" % (wenduC * 1.8 + 32)
    print('F'+wenduF)
else:
    print('输入格式错误')

