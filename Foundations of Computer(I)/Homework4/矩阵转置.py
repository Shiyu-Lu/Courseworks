lst = input().split()
n,m = int(lst[0]),int(lst[1])
matrix = []
for i in range(n):
    linei = input().split()
    matrix.append(linei)
for i in range(m):
    for s in range(n):
        if s == n-1:
            print(matrix[s][i])
        else:
            print (matrix[s][i],end = ' ')



     
        
