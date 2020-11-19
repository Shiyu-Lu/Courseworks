n = int(input())
if n == 1:
    print('End')
else:
    while n != 1:
        m = n
        if n % 2 != 0:
            n = n*3 + 1
            print('%d'%m+'*3+1='+'%d'%n)
        else:
            n = n/2
            print('%d'%m+'/2='+'%d'%n)
    else:
        print('End')
