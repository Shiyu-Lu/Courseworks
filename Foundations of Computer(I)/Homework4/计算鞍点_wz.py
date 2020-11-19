ad = [[0,0] for i in range(5)] #注意二维列表，不能用*，否则全部元素都跟着改变
line = []
for i in range(5):
    linei = input().strip().split()
    if len(linei) > 5:
        for x in range(5):
            line.append(linei[x*5:(x+1)*5])
        break
    else:
        line.append(linei)
for i in range(5):
    for j in range(5):
        if j == 0:
            maxl = int(line[i][0]) 
            ad[i][0] = 0
            ad[i][1] = maxl  
        else:
            if int(line[i][j]) > maxl:
                maxl = int(line[i][j])
                ad[i][0] = j
                ad[i][1] = maxl
flag = False
for i in range(5):
    m = 0
    for j in range(5):
        if ad[i][1] < int(line[j][ad[i][0]]):
            m += 1
        if m == 4:
            print (str(i+1) + " " + str(ad[i][0]+1) + " " + str(ad[i][1]))
            flag = True
            break
if flag == False:
    print('not found')