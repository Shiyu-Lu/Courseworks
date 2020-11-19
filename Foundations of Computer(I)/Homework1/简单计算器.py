opt = input()
l = opt.split()
a = int(l[0])
b = int(l[1])
c = l[2]
if c == '+':
    y = a + b
    print ('%d' % y)
elif c == '-':
    y = a - b
    print ('%d' % y)
elif c == '*':
    y = a * b
    print ('%d' % y)
elif c == '/':
    if b == 0:
        print('Divided by zero!')
    else:
        y = a / b
        print ('%d' % y)
else:
    print('Invalid operator!')
