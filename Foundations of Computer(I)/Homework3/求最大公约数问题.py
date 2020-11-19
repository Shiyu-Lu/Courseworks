lst = input().split()
a,b = int(lst[0]),int(lst[1])
def irt(x,y):
    m,n = max(x,y),min(x,y)
    if (m % n) != 0:
        m = m % n
        irt(m,n)
    else:
        print (n)
irt(a,b)