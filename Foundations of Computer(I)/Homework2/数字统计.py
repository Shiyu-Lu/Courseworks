s = input().split()
L,R = int(s[0]),int(s[1])
count = 0
for i in range(L,R+1):
    for m in str(i):
        if m == '2': #记住是string
            count += 1
print (count)
