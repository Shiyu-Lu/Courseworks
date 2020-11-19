while True:
    honey = int(input())
    if honey == -1:
        break
    trees = []
    cnt = 0
    while True:
        lst = input().split()
        a,b = int(lst[0]),int(lst[1])
        if a == -1 and b == -1:
            break
        cnt += 1
        trees.append([a,b])
    res = 0
    for i in range(cnt):
        n = honey
        peach = 0
        for j in range(i,cnt):
            if n >= trees[j][0]:
                peach += trees[j][0]
                n -= trees[j][1]
            else:
                break
        res = max(res,peach)
    print (res)
            