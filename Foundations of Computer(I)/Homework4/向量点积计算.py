n = int(input())
lst1 = input().split()
lst2 = input().split()
a = 0
for i in range(n):
    a += int(lst1[i])*int(lst2[i])
print (a)
