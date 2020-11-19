lst = input().split()
N,NA,NB = int(lst[0]),int(lst[1]),int(lst[2])
a = input().split()
b = input().split()
w,l = 0,0
a,b = a * (N//NA),b * (N//NB)
def com(x,m):
    for i in range(m):
        x.extend(x[i]) 
com(a,N%NA)
com(b,N%NB)
for i in range(N):
    if int(a[i])-int(b[i]) == -2 or int(a[i])-int(b[i]) == -3 or int(a[i])-int(b[i]) == 5:
        w +=1
    elif int(a[i])-int(b[i]) == 0:
        pass
    else:
        l += 1
if w > l:
    print ('A')
elif w < l:
    print('B')
else:
    print('draw')