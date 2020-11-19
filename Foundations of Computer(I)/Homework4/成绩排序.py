n =int(input())
lst = []
for i in range(n):
    o = [0,0]
    s = input().split()
    o[0] = s[0]
    o[1] = -int(s[1])
    lst.append(o)
lst.sort(key = lambda x:(x[1],x[0])) #先排成绩再排名字可以用多个lambda，不一定用itemgetter
for i in range(n):
    print (lst[i][0],-lst[i][1])