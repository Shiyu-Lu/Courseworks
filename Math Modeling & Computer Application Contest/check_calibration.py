import pandas as pd
def check(ans,path,lastprice,lastturn,lastsize):
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