import mind_v2
import loaddata
import os

path = os.path.dirname(__file__)
#####根据一个样本模拟估计：
inpath = path+"\\data"
back= loaddata.walk(inpath)
if back ==-1:
    print("Wrong path")
else:
    paths,name = back[0],back[1]
i = 0
for pa in paths:
    print("开始求解")
    mind_v2.solve_and_output(pa,name[i])
    
    print("ok anaylze",name[i])
    print()
    i+=1