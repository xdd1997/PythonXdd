f = open('sixPassdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()