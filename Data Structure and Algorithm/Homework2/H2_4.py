import matplotlib.pyplot as plt
from random import random
import timeit
import numpy as np

sort_time=[]
t=timeit.Timer('lst.sort()','from __main__ import lst')
r=range(10**4,10**10,20**4)
for size in r:
    lst = np.random.randint(10**6,size=size)
    lst = lst.tolist()
    sort_time.append(t.timeit(1))

ideal_time = [i * np.log(i) * 2.5 / (10**8) for i in list(r)]
# print(sort_time,ideal_time)
plt.scatter(list(r), sort_time, c='red')
plt.scatter(list(r), ideal_time, c='green')
#plt.legend(['List', 'Dictionary'])
plt.xlabel("Size of List")
plt.ylabel("Time to Sort")
plt.show()

