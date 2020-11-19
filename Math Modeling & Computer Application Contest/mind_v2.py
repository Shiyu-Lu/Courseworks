#因为只知道买一卖一量，所以要根据我们单tick来模拟估计所有的买卖价格是怎么样的
#首先有以下假设，假设存在5个买卖价格，其中价格为整数
#如果有多种结果都可以，则趋向于较为中间的价格

import pandas
from scipy.optimize import minimize
import numpy as np
import math
import os

#自己写的
import floatinn10
import solve_int
import chooosegrid
import loaddata
import setratio
import outdata
import float10
path = os.path.dirname(__file__)


def searchprice(price,Bprice,Aprice,tovA,tovB,ii,Lastsize): # 返回一个列表，格式是[]
    #global tovA,tovB,ii,Lastsize
    if price==Bprice[ii]: # 和本期的买一价相等，说明是买方市场，主动卖出的数目就是期间成交量
        return [price,[Lastsize[ii],0]]
    elif price==Aprice[ii]: # 和卖一价相等，卖方市场，主动买入的数目是期间成交量
        return [price,[0,Lastsize[ii]]]
    else: # 介于二者之间，既有主动买入又有主动卖出
        if tovB[ii]*tovA[ii]>=0: # 卖一买一同向变动
            if tovA[ii]>0: # 双方都跌或持平 注意符号
                return [price,[Lastsize[ii],0]] # 供不应求，是买方市场
            else: # 双方都涨或持平
                return [price,[0,Lastsize[ii]]] # 是卖方市场
        else: # 买一卖一变化一正一负，分摊到两边，既有主卖又有主买
            return [price,[round(Lastsize[ii]*(abs(tovB[ii])/(abs(tovA[ii])+abs(tovB[ii])))),round(Lastsize[ii]*(abs(tovA[ii])/(abs(tovA[ii])+abs(tovB[ii]))))]]#按照比例区分

    


'''
#数据模拟情况：
Lastprice=[111490,111270,111220,111220,111220,111250,111250,111270,111280,111380,111430]
Lastsize=[479,218,322,299,260,245,159,202,106,144,152]
Lastturn=[53403710,24262640,35816320,33254360,28915870,27254570,17690360,22490760,11798930,16031380,16934100]
Bprice=[111480,111250,111190,111210,111210,111250,111270,111270,111280,111380,111430]
Bsize=[22,21,4,3,7,12,1,68,83,4,43]
Aprice=[111490,111270,111230,111220,111250,111270,111280,111330,111300,111430,111440]
Asize=[2,95,1,6,39,40,22,1,9,4,10]
error = [0]*10
tovB=[0]*10
tovA=[0]*10
tovPrice=[0]*10
approix=[]
'''
def solve_and_output(path,name):
    
    df = loaddata.loaddata(path)

    Lastprice=list(df['LastPrice']) # 最后成交价
    Lastsize=list(df['LastSize']) # 期间成交量
    Lastturn=list(df['LastTurnover']) # 期间成交额
    Bprice=list(df['BidPrice']) # 买一价
    Bsize=list(df['BidSize']) # 买一价数量
    Aprice=list(df['AskPrice']) # 卖一价
    Asize=list(df['AskSize']) # 卖一价数量
    # 定义新变量
    error = [0]*len(Aprice)
    tovB=[0]*len(Aprice)
    tovA=[0]*len(Aprice)
    tovPrice=[0]*len(Aprice) #【变量名已改】
    approix=[]
    helpprice=[0]*len(Aprice)
    tovhprice=[0]*len(Aprice)

    for i in range(len(Aprice)): # 遍历每一个时刻
        error[i] = Lastsize[i]*Lastprice[i]-Lastturn[i] #error指的是：用最后成交价计算的成交额减去实际成交额，实际上error要分配到各笔交易里面去
        if Lastsize[i]==0:
            helpprice[i] = Lastprice[i]
        else:
            helpprice[i] = Lastprice[i]-error[i]/Lastsize[i]
        if i!=0:
            tovB[i]=-(Bprice[i-1]-Bprice[i]) # 买一变化值（前减后，下同）
            tovA[i]=-(Aprice[i-1]-Aprice[i]) # 卖一变化值
            tovPrice[i]=-(Lastprice[i-1]-Lastprice[i]) # 最后成交价变化
            tovhprice[i] = -(helpprice[i-1]-helpprice[i])
    ii=-1
    for er in error:

        ii+=1 
        if ii==0 or ii==len(Aprice)-1: # 在头尾两个时刻，跳过
            approix.append([])
            continue
        if Lastsize[ii]==0:
            approix.append([])
            continue

        
        if (tovhprice[ii]>= 10 and tovhprice[ii+1]>= 10): # 【已改】如果买一值连续两期增加，说明是卖方市场
            flag1=0
            confirm = 0
            confirmsize = 0
            if Lastsize[ii]>=Asize[ii-1] and Lastprice[ii]!=Aprice[ii-1]: # 如果期间成交量多于上一期卖一的数量，有一部分可以全部按照卖一的价格成交
                tov_er = Asize[ii-1]*Aprice[ii-1]+(Lastsize[ii]-Asize[ii-1])*Lastprice[ii] # 设置一个新的分配值，其等于（上期卖一的总额+剩余成交量按照最后一笔价格成交得到的总额）
                er = tov_er-Lastturn[ii] # 【已改】
                confirm = Lastturn[ii]-Asize[ii-1]*Aprice[ii-1]
                confirmsize = Asize[ii-1]
                flag1=1
            else:
                er = er # 如果期间成交量还不足完全购买上一期卖一的数量认为，
            if abs(tovhprice[ii])<=0:#改变
                if er==0: # 最后成交价计算的成交额=实际的成交额，说明都是按照最后成交额进行交易的
                    #print([searchprice(Lastprice[ii],Bprice,Aprice)])
                    approix.append([searchprice(Lastprice[ii],Bprice,Aprice,tovA,tovB,ii,Lastsize)]) # 【已改】添加结果
                #print(approix)

                else: # 最后成交价计算的总交易额不等于实际成交额
                    #print(floatinn10.floatinB10(flag1,ii,tovPrice,er,Lastsize,Lastprice,Aprice,Asize,Bprice,Bsize))
                    approix.append(float10.floatinB10(flag1,ii,tovPrice,er,Lastsize,Lastprice,Aprice,Asize,Bprice,Bsize))
            else:
                #设置格点数：
                
                grid,grid2 = chooosegrid.choosegrid_increasing(tovPrice[ii],Lastprice[ii])
                if grid==[]:
                    approix.append([])
                    continue
                
                #已经确定的格点，排除
                initsize = Lastsize[ii]-confirmsize
                initsizegrid = [round(initsize/(len(grid)))]*(len(grid))

                backans = solve_int.solveB(initsizegrid,grid,abs(er),initsize)
                new_ans = []
                for n in range(len(backans)):
                    new_ans.append([grid[n]+Lastprice[ii],[backans[n],0]])
                
                if flag1==1:
                    if Aprice[ii-1] in grid2:
                        new_ans[grid2.index(Aprice[ii-1])][1][0]+=Asize[ii-1]
                    else:
                        new_ans.append([Aprice[ii-1],[Asize[ii-1],0]])
                approix.append(new_ans)
                        


        elif (tovhprice[ii]<= -10 and tovhprice[ii+1]<= -10): # 【已改】如果买一值连续两期下降，说明是买方市场，同上
            flag1=0
            confirm = 0
            confirmsize = 0
            if Lastsize[ii]>=Bsize[ii-1] and Lastprice[ii]!=Bprice[ii-1]: # 如果期间成交量多于上一期卖一的数量，有一部分可以全部按照卖一的价格成交
                tov_er = Bsize[ii-1]*Bprice[ii-1]+(Lastsize[ii]-Bsize[ii-1])*Lastprice[ii] # 设置一个新的分配值，其等于（上期卖一的总额+剩余成交量按照最后一笔价格成交得到的总额）
                er = tov_er-Lastturn[ii] # 【已改】
                confirm = Lastturn[ii]-Bsize[ii-1]*Bprice[ii-1]
                confirmsize = Bsize[ii-1]
                flag1=1
            else:
                er = er # 如果期间成交量还不足完全购买上一期卖一的数量认为，
            if abs(tovhprice[ii])<=0:
                if er==0:
                    approix.append([searchprice(Lastprice[ii],Bprice,Aprice,tovA,tovB,ii,Lastsize)]) #【已改】
                #print(approix)

                else:
                    approix.append(float10.floatinA10(flag1,ii,tovPrice,er,Lastsize,Lastprice,Aprice,Asize,Bprice,Bsize))
            else:
                #设置格点数：
                grid,grid2 = chooosegrid.choosegrid_decreasing(tovPrice[ii],Lastprice[ii])
                if grid==[]:
                    approix.append([])
                    continue
                

                initsize = Lastsize[ii]-confirmsize
                
                initsizegrid = [round(initsize/(len(grid)))]*(len(grid))

                backans = solve_int.solveA(initsizegrid,grid,abs(er),initsize)
                new_ans = []
                for n in range(len(backans)):
                    
                    new_ans.append([grid[n]+Lastprice[ii],[0,backans[n]]])              
                if flag1==1:
                    if Bprice[ii-1] in grid2:
                        new_ans[grid2.index(Bprice[ii-1])][1][0]+=Bsize[ii-1]
                    else:
                        new_ans.append([Bprice[ii-1],[0,Bsize[ii-1]]])
                approix.append(new_ans)    

        
        else:

            grid = chooosegrid.choosegrid_stationary(er,Lastsize[ii])
            if grid == []:
                #print("too big")
                approix.append([])
                continue

            initsizegrid = [round(Lastsize[ii]/(len(grid)))]*(len(grid))

            backans = solve_int.solveC(initsizegrid,grid,-er,Lastsize[ii])
            #print(backans)
            ##不同比率判断买卖比例
            #reback = setratio.noratio(grid,backans,tovA[ii],tovB[ii],Lastprice[ii])
            reback = setratio.distanceratio(grid,backans,Aprice,Bprice,Lastprice,ii)
            #print (reback)
            approix.append(reback)
    
    #输出+检验
    ans = outdata.outdata_check(approix,Lastprice,Lastturn,Lastsize,name,helpprice)

    ##单纯输出
    #ans =  outdata(ans,Lastprice,Lastturn,Lastsize,name)
    return ans
