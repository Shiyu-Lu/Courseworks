lst = input().split()
n,m = int(lst[0]),int(lst[1])
line = []
linec = []
for i in range(n):
    l = input().split()
    line.append(l)
    linec.append(l.copy()) #浅copy，注意copy方式
for i in range(1,n-1):
    for j in range(1,m-1):
        ave = (int(line[i-1][j])+int(line[i][j-1])+int(line[i][j+1])+int(line[i+1][j])+int(line[i][j]))/5
        linec[i][j] = round(ave)
for i in range(n):
    for j in range(m):
        if j == m-1:
            print (linec[i][j])
        else:
            print (linec[i][j],end=" ")
    