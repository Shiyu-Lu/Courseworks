n = int(input())
monthday = [0,31,28,31,30,31,30,31,31,30,31,30,31]
dayy = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
dayylist = list(range(n))
def yearscount(a,b,c):
    global days
    if a != 2019:
        for a1 in range(min(a,2019),max(a,2019)):
            if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0:
                days += 366
            else:
                days += 365
    return days
def mdcount(a,b,c):  
    global days      
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        monthday[2]=29
    if (a > 2019) or (a == 2019 and b > 1):
        for month in range(1,b):
            days += monthday[month]
        days -= 6
        days += c
    elif a < 2019:
        for month in range(1,b):
            days -= monthday[month]
        days += 6
        days = days - c
        days = 7 - days%7
    else:
        days += c
        days -= 6
    return days
for i in range(n):
    days = 0
    monthday[2] = 28
    lst = input().split()
    y,m,d = int(lst[0]),int(lst[1]),int(lst[2])
    if (m<1 or m>12) or (d<1 or d >monthday[m]):
        dayylist[i] = "Illegal"
    else:
        yearscount(y,m,d)
        mdcount(y,m,d)
        t = days % 7
        dayylist[i] = dayy[t]
for i in range(n):
    print(dayylist[i])



