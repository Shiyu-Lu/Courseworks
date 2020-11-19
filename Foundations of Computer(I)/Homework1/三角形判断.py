a = input()
b = a.split()
x = int(b[0])
y = int(b[1])
z = int(b[2])
if x + y > z and x + z > y and y+z>x:
    print('yes')
else:
    print('no')