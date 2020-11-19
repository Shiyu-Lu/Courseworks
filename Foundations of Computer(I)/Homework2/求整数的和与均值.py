s = int(input())
l = 0
if s >= 1 and s <= 10000:
    for t in range(1,s+1):
        m = input()
        l += int(m)
ave = l/s
print (l,'%.5f'%ave)