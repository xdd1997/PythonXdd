#python123
#xdd1997
#文本进度条
import time
scale = 50
#center()方法，将减号字符填充在执行开始的两侧50//2=50/2取整
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()     #程序开始计时为0
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))