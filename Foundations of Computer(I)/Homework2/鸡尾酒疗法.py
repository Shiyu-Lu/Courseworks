n = int(input())
f = True
r = list(range(1,n))
for i in range(n):
    m = input().split()
    m1 = int(m[0])
    m2 = int(m[1])
    if f:
        s1,s2 = m1,m2
        l = s2/s1
        f = False
    else:
        if m2/m1 - l > 0.05:
            r[i-1]='better'
        elif l - m2/m1 > 0.05:
            r[i-1]='worse'
        else:
            r[i-1]='same'
for i in range(n-1):
    print(r[i]) #注意i与i-1

