d = int(input())
g,s,b,su = 0,0,0,0
for i in range(d):
    m = input().split()
    g += int(m[0])
    s += int(m[1])
    b += int(m[2])
su = g+s+b+su
print('%d %d %d %d' % (g,s,b,su))
