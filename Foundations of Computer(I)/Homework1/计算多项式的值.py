word = input()
l = word.split()
x = float(l[0])
a = float(l[1])
b = float(l[2])
c = float(l[3])
d = float(l[4])
fl = a*x**3 + b*x**2 + c*x + d
print('%.7f' % (fl))