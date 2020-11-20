import timeit
import random
import matplotlib.pyplot as plt   # 引入绘图库

list_length = []
operation_time = []

for i in range(10000,1000001,20000):   # 逐渐增大list的长度，检测按索引取值的时间是否随list的长度变化而变化

    # 调用timeit对函数计时
    t = timeit.Timer('x[random.randrange(%d)]'%i,'from __main__ import random,x')  

    # 每次循环产生不同长度的列表x，并把列表的长度存进list_length中
    x = list(range(i))
    list_length.append(i)

    # 从列表中按索引任意取值，得到时间 lst_time，并把执行时间存进operation_time中
    lst_time = t.timeit(number=1000)
    operation_time.append(lst_time)

    # 在终端输出结果
    print('%d,%10.3f'%(i,lst_time))
    
plt.scatter(list_length,operation_time)   # 以列表长度为自变量，执行时间为因变量画散点图
plt.xlabel("Size of List")   # 设置自变量名称
plt.ylabel("Time to complete operation")   # 设置因变量名称
plt.show()

