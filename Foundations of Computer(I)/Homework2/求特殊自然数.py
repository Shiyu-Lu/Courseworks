a = 7*7
b = 9*9**0 + 9*9**1 +9*9**2
for i in range(a,b+1):
    n7 = str(i//49) + str((i%49)//7) + str((i%49)%7)
    n9 = str(i//81) + str((i%81)//9) + str((i%81)%9)
    if n7[0] == n9[2] and n7[1] == n9[1] and n7[2] == n9[0]:
        print(i)
        print(n7)
        print(n9)