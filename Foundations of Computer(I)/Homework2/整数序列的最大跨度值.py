n = int(input())
lst = input().split()
first = True
f = True
for x in lst:
    if first:
        maxV = int(x)
        first = False
    else:
        if maxV < int(x):
            maxV = int(x)
for x in lst:
    if f:
        minV = int(x)
        f = False
    else:
        if minV > int(x):
            minV = int(x)
print(maxV-minV)