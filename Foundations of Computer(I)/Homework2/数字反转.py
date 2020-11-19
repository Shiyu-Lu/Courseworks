N = input()
l = len(N)
first = True
if int(N) > 0:
    for i in range(l-1,-1,-1):
        if first:
            if int(N[i]) != 0:
                out = N[i]
                first = False
        else:
            out = out+N[i]
    print (out)
elif N == '0':
    print (N)
else:
    for i in range(l-1,0,-1):
        if first:
            if int(N[i]) != 0:
                out = N[i]
                first = False
        else:
            out = out+N[i]
    print ('-'+out)
