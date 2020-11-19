a = input()
b = a.split()
x = int(b[0])
y = int(b[1])
if x <= 1 and x >= -1:
    if y <=1 and y>=-1:
        print('yes')
    else:
        print('no')
else:
    print('no')