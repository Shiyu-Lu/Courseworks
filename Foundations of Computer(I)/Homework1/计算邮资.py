inf = input()
b = inf.split()
c = int(b[0])
x = 8
if c > 1000:
    if c % 500 == 0:
        x += 4 * ((c - 1000) / 500)
    else:
        x += 4 * ((c - 1000) // 500 + 1)
if b[1] == 'y':
    x += 5

print('%d' % (x)) #题目要求要输出整数