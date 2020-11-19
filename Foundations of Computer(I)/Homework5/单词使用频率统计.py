import re
l = {}
la = []
lb = []
try:
    while True:
        s = input()
        lst = re.split(":|,|\.|\?|\!|;|\"|\'| |\r|\t|\n|\(|\)",s)
        for i in range(len(lst)):
            word = lst[i].lower()
            if word.isdigit():
                pass
            elif word == '':
                pass
            else:
                if not word in l:
                    l[word] = 1
                else:
                    l[word] += 1
except Exception as e:
    pass

for i in l.keys():
    if not i in la:
        la.append(i)

la.sort()
for i in range(len(la)):
    print (la[i]+'\t'+str(l[la[i]]))

print ('----')

for i in l.items():
    lb.append(i)

lb.sort(key = lambda x:(-x[1],x[0]))
for i in range(len(la)):
    print (lb[i][0]+'\t'+str(lb[i][1]))

