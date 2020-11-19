n = int(input())
h = 0
m = 0
for i in range(n):
    s = input().split()
    a,b = int(s[0]),int(s[1])
    if a >= 90 and a <= 140 and b >=60 and b <=90:
        h += 1
    else:
        if h > m:
            m = h
        h = 0
print(max(h,m))