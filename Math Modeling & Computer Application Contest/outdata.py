import pandas as pd
import os
def outdata(ans,lastprice,lastturn,lastsize,name):
    path = os.path.dirname(__file__)
    new_ans = []
    for i in range(len(ans)):
        data = ans[i]
        
        if data == None or data == []:
            ans[i] = []
            new_ans.append([])
        else:
            midlist = []
            for each_data in data:
                try:
                    if int(sum(each_data[1]))!=0:
                        midlist.append(each_data[0])
                        try:
                            midlist.append(each_data[1][0])
                            midlist.append(each_data[1][1])
                        except IndexError:
                            print(each_data[1])
                except TypeError:
                    print(each_data)
            new_ans.append(midlist)
    csv_list = pd.DataFrame(data=new_ans)
    csv_list.to_csv(path+'\\output\\'+name, encoding='gbk')
    return new_ans

def outdata_save_eff(ans,path,lastprice,lastturn,lastsize):
    new_ans = []
    for i in range(len(ans)):
        data = ans[i]
        
        if data == None or data == []:
            ans[i] = []
            new_ans.append([])
        else:
            midlist = []
            num = 0
            for each_data in data:
                
                if int(sum(each_data[1]))!=0:
                    midlist.append(each_data[0])
                    try:
                        midlist.append(each_data[1][0])
                        midlist.append(each_data[1][1])
                        num+=each_data[0]*sum(each_data[1])
                    except IndexError:
                        print(each_data[0])
            if 20>=abs((num-lastturn[i])):
                midlist.append(1)
            else:
                midlist.append(1)
            new_ans.append(midlist)
    csv_list = pd.DataFrame(data=new_ans)
    csv_list.to_csv(path+'\\outans.csv', encoding='gbk')

def outdata_check(ans,lastprice,lastturn,lastsize,name,helpprice):
    path = os.path.dirname(__file__)
    new_ans = []
    tol = 0
    act = 0
    count = 0
    tovct = [0]*4
    mean = []
    for i in range(len(ans)):
        data = ans[i]
        
        if data == None or data == []:
            ans[i] = []
            new_ans.append([])
        else:
            midlist = []
            num = 0
            ct = 0
            for each_data in data:
                
                try:
                    if int(sum(each_data[1]))!=0:
                        midlist.append(each_data[0])
                        try:
                            midlist.append(each_data[1][0])
                            midlist.append(each_data[1][1])
                            num+=each_data[0]*sum(each_data[1])
                            ct+=sum(each_data[1])
                        except IndexError:
                            print(each_data,each_data[1])
                except TypeError:
                    print(each_data)
            midlist.append(num-lastturn[i])
            midlist.append(ct-lastsize[i])
            if abs((num-lastturn[i]))==0:
                tovct[0]+=1
            elif 20>abs((num-lastturn[i]))>0:
                tovct[1]+=1
            elif 500>abs((num-lastturn[i]))>20:
                tovct[2]+=1
            elif abs((num-lastturn[i]))>500:
                tovct[3]+=1
            tol+=abs(num-lastturn[i])
            if ct==0:
                ct=1

            mean.append([num/ct,helpprice[i],num/ct-helpprice[i]])

            #print(tol,(num-lastturn[i]))
            act+=ct-lastsize[i]
            count+=1
            new_ans.append(midlist)
    print("完成了对：",name,"的检验，其中检验结果如下：")
    print("平均差与成交量总差异",tol/count,ct)
    print("差值在各范围内的计数",tovct)
    

        
            
    csv_list = pd.DataFrame(data=new_ans)
    csv_list.to_csv(path+'\\output\\'+name, encoding='gbk')
    #研究均值情况变化
    csv_list = pd.DataFrame(data=mean)
    csv_list.to_csv(path+'\\output\\mean.csv', encoding='gbk')

    return new_ans