import math
i = input().split()
a,b,c = float(i[0]),float(i[1]),float(i[2])
if a != 0:
    if b*b == 4*a*c:
        m = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        if abs(m) < 0.000001:
            m = 0
        print('x1=x2='+'%.5f'%m)
    elif b*b > 4*a*c:
        m = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        n = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        if abs(m) < 0.000001:
            m = 0
        if abs(n) < 0.000001:
            n = 0
        print('x1='+'%.5f'%m+';x2='+'%.5f'%n)
    elif b*b < 4*a*c:
        m = -b / (2*a)
        n = math.sqrt(4*a*c-b*b) / (2*a)
        if abs(m) < 0.000001:  #记住靠近0的直接用0
            m = 0
        print ('x1='+'%.5f'%m+'+'+'%.5f'%n+'i;x2='+'%.5f'%m+'-'+'%.5f'%n+'i')


