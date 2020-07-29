# switch = {"valueA":functionA,"valueB":functionB,"valueC":functionC}
# try:
#　　switch["value"]() #执行相应的方法。
# except KeyError as e:
#       pass 或 functionX #执行default部分

switch = {
    "a":lambda x:x*2,
    "b":lambda x:x*3,
    "c":lambda x:x**x
}
try:
    swtich["c"](6)
except KeyError as e:
    pass