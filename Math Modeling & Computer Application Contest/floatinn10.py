import math
import solve_int
def floatinB10(flag,ii,tovPrice,er,Lastsize,Lastprice,Aprice,Asize,Bprice,Bsize):
    if flag==1:
        
        Lastsize[ii] = Lastsize[ii]- Asize[ii-1]#消去已经确定的
        if Lastsize[ii]==0:
            return [Lastprice[ii],[Asize[ii-1],0]]
        if  abs(er/Lastsize[ii])<10:
            newp=Lastprice[ii]-10*(er/abs(er)) 
            #print(Lastsize[ii],abs(er/10),Asize[ii-1])
            if newp==Aprice[ii-1]:
                return [[Lastprice[ii],[Lastsize[ii]-abs(er/10),0]],[newp,[abs(er/10)+Asize[ii-1],0]]]
            else:
                return [[Lastprice[ii],[Lastsize[ii]-abs(er/10),0]],[newp,[abs(er/10),0]],[Aprice[ii-1],[Asize[ii-1],0]]]
        elif  10<abs(er/Lastsize[ii])<20: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            #print(Lastsize[ii],abs(er/10),Asize[ii-1])
            
            if newp1==Aprice[ii-1]:
                return [[Lastprice[ii],[Lastsize[ii]-round(2*abs(er/30)),0]],[newp1,[round(abs(er/30))+Asize[ii-1],0]],[newp2,[Lastsize[ii]-3*round(abs(er/30)),0]]]
            elif newp2==Aprice[ii-1]: 
                return [[Lastprice[ii],[Lastsize[ii]-round(2*abs(er/30)),0]],[newp1,[round(abs(er/30)),0]],[newp2,[round(abs(er/30))+Asize[ii-1],0]]]
            else: 
                return [[Lastprice[ii],[Lastsize[ii]-round(2*abs(er/30)),0]],[newp1,[round(abs(er/30)),0]],[newp2,(abs(er/30),0)],[Aprice[ii-1],[Asize[ii-1],0]]]
        
        elif  20<abs(er/Lastsize[ii])<30: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            newp3=Lastprice[ii]-30*(er/abs(er))
            initsizegrid = [round(Lastsize[ii]/(4))]*(4)
            ans = solve_int.solveC(initsizegrid,[0,10,20,30],abs(er),Lastsize[ii])
            #print(Lastsize[ii],abs(er/10),Bsize[ii-1])
            if newp1==Aprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]+Asize[ii-1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]]]]
            elif newp2==Aprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]+Asize[ii-1]]],[newp3,[0,ans[3]]]]    
            elif newp3==Aprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]+Asize[ii-1]]]]
            else:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]]],[Aprice[ii-1],[0,Asize[ii-1]]]]   
        else:
            return [[]]   
            #print(Lastsize[ii],abs(er/60),er,Asize[ii-1])
    else:
        if   abs(er/Lastsize[ii])<10:#10 左右变动
            newp=Lastprice[ii]-10*(er/abs(er))
            return [[Lastprice[ii],[Lastsize[ii]-abs(er/10),0]],[newp,[abs(er/10),0]]]
        elif  10<abs(er/Lastsize[ii])<20: # 【已改】
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            return [[Lastprice[ii],[Lastsize[ii]-round(2*abs(er/30)),0]],[newp1,(abs(er/30),0)],[newp2,(abs(er/30),0)]]
        elif  20<abs(er/Lastsize[ii])<30: #【已改】
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            newp3=Lastprice[ii]-30*(er/abs(er))
            return [[Lastprice[ii],[Lastsize[ii]-round(3*abs(er/60)),0]],[newp1,[round(abs(er/60)),0]],[newp2,[round(abs(er/60)),0]],[newp3,[round(abs(er/60)),0]]]


def floatinA10(flag,ii,tovPrice,er,Lastsize,Lastprice,Aprice,Asize,Bprice,Bsize): #【已改】
    if flag==1:
        Lastsize[ii] = Lastsize[ii]- Bsize[ii-1]
        if Lastsize[ii]==0:
            return [Lastprice[ii],[Bsize[ii-1],0]]
        if  abs(er/Lastsize[ii])<10:
            newp=Lastprice[ii]-10*(er/abs(er))

            if newp==Bprice[ii-1]:
                return [[Lastprice[ii],[0,Lastsize[ii]-abs(er/10)]],[newp,[0,abs(er/10)+Bsize[ii-1]]]]
            else:
                return [[Lastprice[ii],[0,Lastsize[ii]-abs(er/10)]],[newp,[0,abs(er/10)]],[Bprice[ii-1],[0,Bsize[ii-1]]]]
            #print(approix)
        elif  10<abs(er/Lastsize[ii])<20: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            if newp1==Bprice[ii-1]: # here
                return [[Lastprice[ii],[0,Lastsize[ii]-round(2*abs(er/30))]],[newp1,[0,round(abs(er/30))+Bsize[ii-1]]],[newp2,[0,round(abs(er/30))]]]
            elif newp2==Bprice[ii-1]: 
                return [[Lastprice[ii],[0,Lastsize[ii]-round(2*abs(er/30))]],[newp1,[0,round(abs(er/30))]],[newp2,[0,round(abs(er/30))+Bsize[ii-1]]]]
            else: 
                return [[Lastprice[ii],[0,Lastsize[ii]-round(2*abs(er/30))]],[newp1,[0,round(abs(er/30))]],[newp2,[0,round(abs(er/30))]],[Bprice[ii-1],[0,Bsize[ii-1]]]]

        elif  20<abs(er/Lastsize[ii])<30: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            newp3=Lastprice[ii]-30*(er/abs(er))

            initsizegrid = [round(Lastsize[ii]/(4))]*(4)
            ans = solve_int.solveC(initsizegrid,[0,10,20,30],abs(er),Lastsize[ii])
            #print(Lastsize[ii],abs(er/10),Bsize[ii-1])
            if newp1==Bprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]+Bsize[ii-1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]]]]

            elif newp2==Bprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]+Bsize[ii-1]]],[newp3,[0,ans[3]]]]    
            elif newp3==Bprice[ii-1]:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]+Bsize[ii-1]]]]
            else:
                return [[Lastprice[ii],[0,ans[0]]],[newp1,[0,ans[1]]],[newp2,[0,ans[2]]],[newp3,[0,ans[3]]],[Bprice[ii-1],[0,Bsize[ii-1]]]]   
        else:
            return [[]]         
    else:
        if   abs(er/Lastsize[ii])<10:#10 左右变动
            newp=Lastprice[ii]-10*(er/abs(er))
            return [[Lastprice[ii],[0,Lastsize[ii]-abs(er/10)]],[newp,[0,abs(er/10)]]]
        elif  10<abs(er/Lastsize[ii])<20: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            return [[Lastprice[ii],[0,Lastsize[ii]-round(2*abs(er/30))]],[newp1,[0,round(abs(er/30))]],[newp2,[0,round(abs(er/30))]]]

        elif  20<abs(er/Lastsize[ii])<30: 
            newp1=Lastprice[ii]-10*(er/abs(er))
            newp2=Lastprice[ii]-20*(er/abs(er))
            newp3=Lastprice[ii]-30*(er/abs(er))
            return [[Lastprice[ii],[0,Lastsize[ii]-round(3*abs(er/60))]],[newp1,[0,round(abs(er/60))]],[newp2,[0,round(abs(er/60))]],[newp3,[0,round(abs(er/60))]]]

