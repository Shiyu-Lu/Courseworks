lst = input().split()
l,M = int(lst[0])+1,int(lst[1])
L = [1]*l
count = 0
for i in range(M):
    lis = input().split()
    sta = int(lis[0])
    end = int(lis[1])
    for x in range(l):
        if x >= sta and x <= end:
            L[x] = 0
for i in L:
    if i is 1:
        count += 1
print(count)
