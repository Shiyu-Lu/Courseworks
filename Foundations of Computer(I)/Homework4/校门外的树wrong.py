lst = input().split()
L,M = list(range(int(lst[0])+1)),int(lst[1])
sub = []
for i in range(M):
    l = input().split()
    sta = int(l[0])
    end = int(l[1])
    for j in range(sta,end+1):  #同一个循环里不能用同一个循环变量
        if j in sub:
            pass
        else:
            sub.append(j)
for i in range(len(sub)):
    if sub[i] in L:
        L.remove(sub[i]) #直接进行remove操作，不用创建新list
print (len(L))

    

