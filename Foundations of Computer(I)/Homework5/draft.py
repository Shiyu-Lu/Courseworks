# d = {}
# l = ['apple','b','c']
# d['b'] = 1
# print (d)

# a = '123'
# print ('123'.isdigit())

l = []
honey = -1
maxnum = 0
def mpeach(honey,l,maxnum):
    for i in range(len(l)):
        peach,rest = 0,honey
        rest -= int(l[i][1])
        peach += int(l[i][0])
        if rest < 0:
            if peach > maxnum:
                maxnum = peach
        if len(l) > 1:
            for m in range(i+1,len(l)):
                rest -= int(l[m][1])
                if rest < 0:
                    break
                peach += int(l[m][0])
                if peach > maxnum: #可以写成maxnum=max(maxnum,peach)
                    maxnum = peach
        else:
            if rest < 0:
                maxnum = 0
            else:
                maxnum = peach
    print (maxnum)

while True:
    lst = input().strip().split()
    if lst == ['-1']:
        break
    elif lst == ['-1','-1']:
        mpeach(honey,l,maxnum)
        honey = -1
        l = []
        maxnum = 0 #恢复默认数据，重新开始下一个案例
    else: #输入第一个案例
        if honey == -1:
            honey = int(lst[0])
        else:
            l.append(lst) 