ad = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #注意二维列表，不能用*，否则全部元素都跟着改变
line = []
for i in range(5):
    linei = input().split()
    if len(linei) > 5:
        for x in range(5):
            line.append(linei[x*5,(x+1)*5])
    else:
        line.append(linei)
    for j in range(5):
        if j == 0:
            maxl = int(linei[0]) 
            ad[i][0] = i 
            ad[i][2] = maxl  
        else:
            if int(linei[j]) > maxl:
                maxl = int(linei[j])
                ad[i][0] = i
                ad[i][2] = maxl
                ad[i][1] = j
for i in range(5):
    m = 0
    for j in range(5):
        if ad[i][2] <= int(line[j][ad[i][1]]):
            m += 1
        if m == 5:
            print (i+1," ",ad[i][1]+1," ",ad[i][2])
if m == 0:
    print('not found')
    

