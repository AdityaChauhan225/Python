
# Numpy

'''
numpy stands for Numeric python
it is mainly used for handeling arrays

It is a powerfull python libaray for numerical computing 
It supports multidimentional arrays (ndarray)
It is used for working with arrays and it also have functions for working in domain of linear algebra, fourier transform and matrices
arrays are frequently used in data science where speed and resourses are important 
numpy arrays store at one continous place in memory unlike list, so the process of accessing and manupulating is very low 
''' 

import numpy as np 
zd=np.array(34)
od = np.array([1,2,3,4,6,4,3,35,67,88])
td  = np.array([[1,2,3,4],[5,6,7,8]])
threed = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])


fivd = np.array([1,2,3,4],ndmin=5)

print(od[1])
print(td[1,1])

##### Day 5 

print(threed[-1,-2,-1])
print(td[-1,-1])

# slicing

print(od[2:5:3])
print(od[2:])
print(od[:4])
print(od[:])
print(od[-1:1:-1])


# 2-d array:
print(td[:,1])

# print(f"{zd}\n{od}\n{td}\n{threed}\n{fivd}")

# for i in range(1,6):
#     print("*"*i)

# for i in range(6,1,-1):
#     print("*"*i)

