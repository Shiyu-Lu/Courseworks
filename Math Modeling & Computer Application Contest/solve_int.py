from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
import consnum
import math
#import pandas as pd
def fun(p):
    
    v =lambda x: np.dot(x,p)
    return v

def con(quant,confirm,p):

    num = len(p)
    cons =consnum.consnum(num,confirm,quant,p)

    return cons


def solveA(x,p,confirm,quant):
    max_count = 10
    count = 0
    torv = 1000
    xn = []
    for n in p:
        xn.append(abs(n)) 
    p = xn
    
    while count<max_count and torv>100:
        #x = np.array(x)
        #p = np.array(p)
        cons = con(quant,confirm,p)

        res = minimize(fun(p),x,method="SLSQP",constraints=cons)
        
        ans = list(res.x)
        

        nans = []
        ns = 0
        i=0
        for num in ans:
            nans.append(round(num))
            ns+= num*p[i]
            #print(num*p[i],num,p[i])
            i+=1
            
        #print(ans,np.dot(ans,p))
        try:
            tov = int(sum(nans)-quant)
        except ValueError:
            print(nans,quant,p,confirm)

            return [0,0,0,0,0]
        if tov==0:
            pass
        elif tov>0:
            for i in nans:
                if i >tov:
                    nans[nans.index(i)] -= tov
                    break
        else:
            nans[0]-=tov
        
        torv = abs(np.dot(nans,p)-confirm)
        

        #更新值
        x = nans
        #print("error",torv)
        count+=1
    #print(nans,"\n")
    return nans

def solveB(x,p,confirm,quant):
    max_count = 10
    count = 0
    torv = 1000
    xn = []
    for n in p:
        xn.append(-n)
    p = xn
    #print(p)
    while count<max_count and torv>100:
        #x = np.array(x)
        #p = np.array(p)
        cons = con(quant,confirm,p)

        res = minimize(fun(p),x,method="SLSQP",constraints=cons)
        
        ans = list(res.x)
        

        nans = []
        ns = 0
        i=0
        for num in ans:
            nans.append(round(num))
            ns+= num*p[i]
            #print(num*p[i],num,p[i])
            i+=1
            
        #print(ans,np.dot(ans,p))

        tov = int(sum(nans)-quant)
        if tov==0:
            pass
        elif tov>0:
            for i in nans:
                if i >tov:
                    nans[nans.index(i)] -= tov
                    break
        else:
            nans[0]-=tov
        
        torv = abs(np.dot(nans,p)-confirm)
        

        #更新值
        x = nans
        #print("error",torv)
        count+=1
    #print(nans,"\n")
    return nans

def solveC(x,p,confirm,quant):
    max_count = 10
    count = 0
    torv = 1000
    xn = []

    #print(p)
    while count<max_count and torv>100:
        #x = np.array(x)
        #p = np.array(p)
        cons = con(quant,confirm,p)

        res = minimize(fun(p),x,method="SLSQP",constraints=cons)
        
        ans = list(res.x)
        

        nans = []
        ns = 0
        i=0
        for num in ans:
            nans.append(round(num))
            ns+= num*p[i]
            #print(num*p[i],num,p[i])
            i+=1
            
        #print(ans,np.dot(ans,p))

        tov = int(sum(nans)-quant)
        if tov==0:
            pass
        elif tov>0:
            for i in nans:
                if i >tov:
                    nans[nans.index(i)] -= tov
                    break
        else:
            nans[0]-=tov
        
        torv = abs(np.dot(nans,p)-confirm)
        

        #更新值
        x = nans
        #print("error",torv)
        count+=1
    #print(nans,"\n")
    return nans







'''
if __name__ == "__main__":
    solve([36,36,36,36,36,36],[111490,111450,111400,111350,111300,111270],24262640,218)

'''
