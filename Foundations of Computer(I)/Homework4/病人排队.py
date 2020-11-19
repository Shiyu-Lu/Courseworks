n = int(input())
old = []
noto = []
for i in range(n):
    l = input().strip().split()
    name,age = int(l[0]),int(l[1])
    l[1] = age
    if age >= 60:
        old.append(l)
    else:
        noto.append(l)
old.sort(key=lambda x:-x[1])
for i in range(len(old)):
    print (old[i][0])
for i in range(len(noto)):
    print (noto[i][0])
    