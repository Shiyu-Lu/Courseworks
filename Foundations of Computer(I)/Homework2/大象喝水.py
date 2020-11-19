i = input().split()
h = int(i[0])
r = int(i[1])
water = 3.14159*r*r*h/1000
if 20 % water == 0:
    print('%d' % (20/water))
else:
    print('%d'%(20//water+1))

