# import re
# n = int(input())
# tag = r'(<([a-z]+>).*?</)\2'
# ntag = r'(\(\d{1,2}\)-\d{3})+\D'

# for i in range(n):
#     s = input()
#     r = re.findall(tag,s)
#     if len(r)>0:
#         for m in range(len(r)): # 把符合tag条件的r里面的每个子串单拎出来分析
#             num = []
#             rig = 0
#             string = ''
#             for item in re.finditer(ntag,r[m][0]): # 在符合ntag条件的子串中寻找贪婪模式下符合ntag模式的电话号码
#                 a = item.group()
#                 b = re.split('\(|\)',a) # 把区号左右两边的括号split出来
#                 for n in range(len(b)):
#                     if len(b[n]) == 1 or len(b[n]) == 2: #因为只有区号是1-2位所以可以用长度判断
#                         num.append(b[n]) # 将区号加入num的list中
#             if len(num) != 0: #若有符合条件的区号，进行string连接，并打印
#                 for n in range(len(num)): 
#                     if n < len(num)-1:
#                         string += str(num[n])+','
#                     else:
#                         string += str(num[n])
#                 print ('<'+r[m][1]+string+'</'+r[m][1])
#                 rig = 1
#         if rig == 0: # 一个tag中没有一个符合条件的电话号码
#             print ('NONE')
#     else:
#         print('NONE')

#测试数据
# 2
# <bb>(01)-123<a>bbb(02)-2784KK</a><xy>stk(1)-123(03)-345b</xy>(04)-123</xy><z>(05)-123</zz>zz<yy>(06)-123</yy>
# <bb>(01)-123<a><k>1223</k><a>(01)-12</a>

import re

n = int(input())
tag = r'<([a-z]+?>).+?</\1'
ntag = r'\((\d{1,2})\)-(\d{3,})'

for i in range(n):
    s = input()
    printed = False
    for r in re.finditer(tag, s):
        num = []
        string = ''
        for item in re.finditer(ntag,r.group(0)): 
            if len(item.group(2)) != 3:
                continue
            num.append(item.group(1))
        if len(num) != 0: 
            for n in range(len(num)):
                if n < len(num)-1:
                    string += str(num[n])+','
                else:
                    string += str(num[n])
            head = '<' + r.group(1)
            tail = '</' + r.group(1)
            print (head+string+tail)
            printed = True
    if not printed:
        print("NONE")
