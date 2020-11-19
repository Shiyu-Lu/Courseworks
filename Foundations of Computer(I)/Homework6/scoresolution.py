'''

1) id.txt 里面放着学号和姓名，没有排序
2) finalscore里面放着学生的做题信息。其中第三栏或第四栏是做题数量
3) 分数计算办法: 1题50,2题60,此后每做一题加4分
4) 生成id.txt里面有的所有学生的成绩，按学号排序输出到结果文件result.txt。

如果在 finalscore里面找不到学生的做题记录，该生题数和成绩都记0

'''
# coding=utf-8

# 引入库
import sys
import re
import jieba
import pdb

def score(filename,name,ids,corr,sco): 
    try:
        f = open(filename,"r",encoding='utf-8') 
    except Exception as e:
        print("file not exists")
        return 0

    lines = f.readlines() #将每一行加进lines里
    f.close()

    for line in lines:
        lst = line.strip().split('\t')
        nic = jieba.lcut(lst[1]) #昵称一栏的切分
        for i in nic: #找出昵称中的学号或者名字
            if i in name.keys(): #若i是学号
                if lst[2].isdigit(): #将学号作为key，题数作为value存入corr的字典
                    corr[i] = int(lst[2])
                else:
                    corr[i] = int(lst[3])
            elif i in ids:
                if lst[2].isdigit(): 
                    corr[ids[i]] = int(lst[2])
                else:
                    corr[ids[i]] = int(lst[3])

    for i in corr: #计算得分，存入s的字典；不能用i in range因为字典里没有corr[i]
        if corr[i] == 0:
            sco[i] = 0
        elif corr[i] == 1:
            sco[i] = 50
        elif corr[i] == 2:
            sco[i] = 60
        elif corr[i] > 2:
            sco[i] = 60+(corr[i]-2)*4

    return corr,sco

info = []
name = {}
ids = {}
f = open("id.txt","r",encoding='utf-8')
lines = f.readlines()
f.close()

# 用set把学号和名字存起来
for line in lines:
    line = line.strip().split('\t')
    if line == "":
        continue
    else:
        info.append(line[0])  #将学号加入info集合
        name[line[0]] = line[1] #将名字作为value，学号作为key存入name这个字典中
        ids[line[1]] = line[0] #将学号作为value，名字作为key存入name这个字典中

corr = {}
sco = {}
corr,sco = score(sys.argv[1],name,ids,corr,sco)
if corr != 0 and sco != 0:
    info.sort()
    f = open(sys.argv[2],"w",encoding='utf-8')
    f.write('学号\t姓名\t题数\t分数\n') #注意制表符的用法
    for x in range(len(info)):
        if info[x] in corr:
            f.write('%s\t%s\t%s\t%d\n' % (info[x],name[info[x]],corr[info[x]],sco[info[x]]))
        else:
            f.write('%s\t%s\t%s\t%d\n' % (info[x],name[info[x]],'0',0))
    f.close()