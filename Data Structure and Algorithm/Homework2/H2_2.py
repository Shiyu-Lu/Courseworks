import timeit
import random
import matplotlib.pyplot as plt   # 引入绘图库

dict_size = []
get_time = []
set_time = []

for i in range(10000,1000001,20000):   # 逐渐增大字典的长度，检测执行时间是否随字典的长度变化而变化

    # 调用timeit对函数计时
    t_getitem = timeit.Timer('x.get(random.randrange(%d))'%i,'from __main__ import random,x')   # get time的执行时间
    t_setitem = timeit.Timer('x.setdefault(random.randrange(%d))'%i,'from __main__ import random,x')   # set time的执行时间

    # 每次循环产生不同大小的字典（value为none），并把字典的长度存进dict_size中
    x = {j:None for j in range(i)}
    dict_size.append(i)

    # 分别获得执行时间，并存进get_time和set_time中
    getitem_time = t_getitem.timeit(number=1000)
    setitem_time = t_setitem.timeit(number=1000)
    get_time.append(getitem_time)
    set_time.append(setitem_time)

    # 在终端输出结果
    print('%d,%10.3f,%10.3f'%(i,getitem_time,setitem_time))

plt.scatter(dict_size,get_time,c='red')
plt.scatter(dict_size,set_time,c='green')
plt.legend(['get item','set item'])
plt.xlabel("Size of Dictionary")   # 设置自变量名称
plt.ylabel("Time to complete operation")   # 设置因变量名称
plt.show()

