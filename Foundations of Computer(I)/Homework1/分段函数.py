N = input()
x = float(N)
if x >= 0 and x < 5:
    y = -x + 2.5
elif x >= 5 and x < 10:
    y = 2 - 1.5*(x-3)**2
else:
    y = x/2 - 1.5
print('%.3f' % (y))