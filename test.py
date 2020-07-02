

import numpy as np

list1 = np.array([1,2,3,4])
list2 = np.array([1,2,3,4])
print(list1[:2])
print(type(list1))

list3 = list1.reshape([2,2])
print(list3)
print(type(list3))
print(np.dot(list3,list1[:2]))
