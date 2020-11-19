import re
s = input()
d = {}
for x in s:
    if not x in d:
        d[x] = -1
    else:
        d[x] = 0
a = 0
for x in s:
    if d[x] == -1:
        print(x)
        a = 1
        break
if a == 0:
    print ('no')
else:
    pass
    

