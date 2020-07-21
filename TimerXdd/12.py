
def num2hms(sec):
    hour = int(sec / 3600)
    min = int(sec % 3600 / 60)
    s = sec % 60
    if hour<10:
        hour= '0'+str(hour)
    if min<10:
        min = '0'+str(min)
    if s<10:
        s = '0'+str(s)
    print(s)
    stringTime = str(hour) +':' +str(min) +':'+str(s)
    return  stringTime

a = num2hms(72)
print(a)


pyinstaller -F -w "TimerMain.py"