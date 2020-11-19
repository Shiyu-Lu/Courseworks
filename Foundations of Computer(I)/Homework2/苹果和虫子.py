i = input().split()
n = int(i[0])
x = int(i[1])
y = int(i[2])
if x != 0: #注意x不能为0
    if (y/x) % 1 == 0: #注意是判断y/x能不能被整除
        a = n - y//x
    else:
        a = n - y//x - 1
if a >=0:
    print ('%d' % a)
else:
    print('0') #注意输出结果不能为负数

#lst = input().split()
#n,x,y = int(lst[0]),int(lst[1]),int(lst[2])
#print(max(n-(y+x-1)//?,0))