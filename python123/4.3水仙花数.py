#python123
#xdd1997
import  time
x = 966
shui =''
for i in range(100,x+1):
    a = i // 100
    b = i // 10 -a*10
    c = i % 10
 #   time.sleep(0.5)
#    print(a,b,c)
    if pow(a,3)+pow(b,3)+pow(c,3)==i:
        shui =shui +str(i)+','
print(shui[:-1])

