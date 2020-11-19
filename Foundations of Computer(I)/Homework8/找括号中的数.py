# import re
# n = int(input())
# m = '(<)(\d*?)(>)'
# l =[]

# for i in range(n):
#     s = input()
#     line = ''
#     for x in re.finditer(m,s):
#         num = str(x[2])
#         if num == '0':
#             line += num+' '
#         elif num == '':
#             line += 'NONE'+' '
#         elif len(num)<4 and num[0] != '0':
#             line += num+' '
#     l.append(line)

# for i in range(n):
#     print(l[i])

import re

m = r'<(0|[1-9]\d{0,2})>'
n = int(input())

for i in range(n):
    s = input()
    result = re.findall(m, s)
    for item in result:
        print(item, end=' ')
    if len(result) == 0:
        print("NONE", end=' ')
    print('')

    
