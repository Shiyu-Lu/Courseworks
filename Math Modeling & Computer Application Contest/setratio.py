def noratio(grid,ans,tovA_ii,tovB_ii,lastprice_ii):
    #no比例
    reback=[]
    for each in range(len(grid)):
        if int(abs(ans[each]))==0:
            continue
        if grid[each]>0:#want to buy
            reback.append([lastprice_ii+grid[each],[ans[each],0]])
        elif grid[each]<0:#want to sell
            reback.append([lastprice_ii+grid[each],[0,ans[each]]])
        else:
            if tovA_ii<0 and tovB_ii<0:#降价促销
                reback.append([lastprice_ii,[0,ans[each]]])
            
            elif tovA_ii>0 and tovB_ii>0:#快来买啊要涨
                reback.append([lastprice_ii,[ans[each],0]])
            
            elif (tovA_ii<=0 and tovB_ii>0):
                reback.append([lastprice_ii,[round(ans[each]*(abs(tovB_ii))/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*abs(tovB_ii)/(abs(tovA_ii)+abs(tovB_ii)))]])
                
            elif (tovA_ii<0 and tovB_ii>=0):
                reback.append([lastprice_ii,[round(ans[each]*(abs(tovB_ii))/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*abs(tovB_ii)/(abs(tovA_ii)+abs(tovB_ii)))]])
                
            elif (tovA_ii>=0 and tovB_ii<0):#理解为往两边跑，为什么呢，因为中间的买完了呗，这个时候我想想啊，反过来涨的高，买的多，降的多，卖的多
                reback.append([lastprice_ii,[round(ans[each]*abs(tovA_ii)/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*(abs(tovA_ii))/(abs(tovA_ii)+abs(tovB_ii)))]])
            
            elif (tovA_ii>0 and tovB_ii<=0):#理解为往两边跑，为什么呢，因为中间的买完了呗，这个时候我想想啊，反过来涨的高，买的多，降的多，卖的多
                reback.append([lastprice_ii,[round(ans[each]*abs(tovA_ii)/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*(abs(tovA_ii))/(abs(tovA_ii)+abs(tovB_ii)))]])
                
            else:
                reback.append([lastprice_ii,[round(ans[each]/2),ans[each]-round(ans[each]/2)]])#一半一半
        

    return reback
    #对于有一定分布程度的其实差不多，在非零的时候要修改
    #计算幅度：

def fixcratio(grid,ans,tovA_ii,tovB_ii,lastprice_ii):
    ratio = [0.8,0.2]#增加的时候0.8主动买，0.2主动卖，反之亦然
    reback=[]
    for each in range(len(grid)):
        if int(abs(ans[each]))==0:
            continue
        if grid[each]>0:#want to buy
            reback.append([lastprice_ii+grid[each],[round(ratio[0]*ans[each]),ans[each]-round(ratio[0]*ans[each])]])
        elif grid[each]<0:#want to sell
            reback.append([lastprice_ii+grid[each],[round(ratio[1]*ans[each]),ans[each]-round(ratio[1]*ans[each])]])

        else:
            if tovA_ii<0 and tovB_ii<0:#降价促销
                reback.append([lastprice_ii,[0,ans[each]]])
            elif tovA_ii>0 and tovB_ii>0:#快来买啊要涨
                reback.append([lastprice_ii,[ans[each],0]])
            elif (tovA_ii<=0 and tovB_ii>0):
                reback.append([lastprice_ii,[round(ans[each]*(abs(tovB_ii))/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*abs(tovB_ii)/(abs(tovA_ii)+abs(tovB_ii)))]])
            elif (tovA_ii<0 and tovB_ii>=0):
                reback.append([lastprice_ii,[round(ans[each]*(abs(tovB_ii))/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*abs(tovB_ii)/(abs(tovA_ii)+abs(tovB_ii)))]])
            elif (tovA_ii>=0 and tovB_ii<0):#理解为往两边跑，为什么呢，因为中间的买完了呗，这个时候我想想啊，反过来涨的高，买的多，降的多，卖的多
                reback.append([lastprice_ii,[round(ans[each]*abs(tovA_ii)/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*(abs(tovA_ii))/(abs(tovA_ii)+abs(tovB_ii)))]])
            elif (tovA_ii>0 and tovB_ii<=0):#理解为往两边跑，为什么呢，因为中间的买完了呗，这个时候我想想啊，反过来涨的高，买的多，降的多，卖的多
                reback.append([lastprice_ii,[round(ans[each]*abs(tovA_ii)/(abs(tovA_ii)+abs(tovB_ii))),ans[each]-round(ans[each]*(abs(tovA_ii))/(abs(tovA_ii)+abs(tovB_ii)))]])
            else:
                reback.append([lastprice_ii,[round(ans[each]/2),ans[each]-round(ans[each]/2)]])#一半一半
    return reback

#距离近似模拟
def distanceratio(grid,ans,Aprice,Bprice,lastprice,ii):
    
    reback=[]
    for num in range(len(grid)):
        if int(abs(ans[num]))==0:
            continue
        distanceB = Bprice[ii-1]-(lastprice[ii]+grid[num])
        distanceA = Aprice[ii-1]-(lastprice[ii]+grid[num])
        if distanceA >=0 and distanceB <0:
            #print("1",distanceA,distanceB)
            ratio = [abs(distanceB)/(abs(distanceA)+abs(distanceB)),abs(distanceA)/(abs(distanceA)+abs(distanceB))]
            reback.append([lastprice[ii]+grid[num],[round(ratio[0]*ans[num]),ans[num]-round(ratio[0]*ans[num])]])
        elif distanceA >0 and distanceB <=0:    
            #print("2",distanceA,distanceB)  
            ratio = [abs(distanceB)/(abs(distanceA)+abs(distanceB)),abs(distanceA)/(abs(distanceA)+abs(distanceB))]
            reback.append([lastprice[ii]+grid[num],[round(ratio[0]*ans[num]),ans[num]-round(ratio[0]*ans[num])]])
        elif distanceA <0 and distanceB <0:#都涨价，买方主动性全部
            #print("3",distanceA,distanceB)
            ratio = [1,0]
            reback.append([lastprice[ii]+grid[num],[round(ratio[0]*ans[num]),round(ratio[1]*ans[num])]])
        elif distanceA >0 and distanceB >0:#反之成立
            #print("4",distanceA,distanceB)
            ratio = [0,1]
            reback.append([lastprice[ii]+grid[num],[round(ratio[0]*ans[num]),round(ratio[1]*ans[num])]])
        else:
            print("have no consider it")

    return reback
