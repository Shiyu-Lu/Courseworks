import timeit
import matplotlib.pyplot as plt   # 引入绘图库

size = []
lst_time = []
dict_time = []

for i in range(10000,1000001,20000):   # 逐渐增大size，检测执行时间是否随size变化而变化

    # 调用timeit对函数计时
    t1 = timeit.Timer('del(x[len(x)//2])','from __main__ import x')
    t2 = timeit.Timer('del x[len(x)-1]','from __main__ import x')   # 注意：不能设置与i有关的key
    size.append(i)

    # 先获得list的del执行时间，并存进lst_time中
    x = list(range(i))
    t_lst = t1.timeit(number=3000)
    lst_time.append(t_lst)

    # 获得dict的del执行时间，并存进dict_time中
    x = {j:None for j in range(i)}
    t_dict = t2.timeit(number=3000)
    dict_time.append(t_dict)

    # 在终端输出结果
    print('%d,%10.3f,%10.3f'%(i,t_lst,t_dict))

plt.scatter(size,lst_time,c='red')
plt.scatter(size,dict_time,c='green')
plt.legend(['List','Dictionary'])
plt.xlabel("Size of List or Dictionary")   # 设置自变量名称
plt.ylabel("Time to complete operation")   # 设置因变量名称
plt.show()
