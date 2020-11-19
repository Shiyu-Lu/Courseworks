import re
m = '[0-9]+\.\d+|[0-9]\d*'
while True:
    try:
        s = input()
        lst = re.findall(m,s)
        for x in lst:
            print(x)
    except:
        break