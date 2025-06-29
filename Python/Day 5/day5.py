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

fl= np.array([1.2,2.5,3.5])
print(fl.dtype)
it= np.array([1,2,3])
print(it.dtype)
st= np.array(["a","b","c"])
print(st.dtype)

arr= np.array([1.2,2.5,3.5,0,-1,-2])
newarr = arr.astype(int)
print(newarr)
newarr = arr.astype(bool)
print(newarr)

## common creaters in numpy


# to create matrix containing only zeros 
print(np.zeros((2,3)))  # multi dimentional
print(np.zeros(2))   # one dimentional

print(np.eye(3)) # to create identity matrix

print(np.linspace(2,10,num=5))  # will return 5 numbers from 2 to 10 with equal spacing between them

td_reshape = td.reshape(4,2) # to chage the shape of array...( will not change in original array)
print(td_reshape)

td_flat=td.flatten() # flatten the array to one-d
print(td_flat)

a = np.array([1,2,3])
b= np.array([1,2,3])

print(a+b)
print(a*2)# scaler multiply


## Broadcasting
'''
Broadcasting is a feature that allows you to perform operations between arrays of different shapes by automatically expanding them, when compatible. 
ex:  b matrix will look like :[[1 2 3],[1 2 3], [1 2 3]]

'''
c=np.array([[1],[2],[3]])

print(b+c)


## aggrigate functions

print(b.sum())
print(b.sum())
print(b.max())
print(np.median(b))
print(td.max(axis=0)) # 0 is for c

''' 
we can join arrays in numpy by the axis using the concatinate function 
Syntax:- np.concatenate((a,b),axis) (a,b are the arrays to be concatinated)
        np.concat(()) are the same
'''
a1=np.array([[1],[2],[3]])
a2=np.array([[4],[5],[6]])

print(np.concat((a1, a2),axis=1))
print(np.concat((a1, a2),axis=0))


'''
in numpy there are more type of functions to join arrays
1. Stack
'''

'''
Stack(): stacking is same as concatenation, only difference is that stacking is done along a new axis.
hstack(): Numpy provides a helper function:::: it stacks along rows
vstack(): to stack along columns
dstack(): to stack along height, which is the same as depth. 
'''


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]) 
# newarr1 = np.array_split(arr,3,axis=1)

# we also have the method split() available but it will not adjust the elements are less in source array for splitting, array_split() worked properly but split() would fail.

x=np.where(arr1==4) # used to search in numpy array (returns the index that get a match)
print(x)

# searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order
'''
the function np.searchsorted() is used to find the index where the value should be inserted so that the order of the array remains sorted
'''
arr = np.array([6,7,8,9])
y=np.searchsorted(arr,7,side='right')
print(y)


#### will sort the array in ascending order

abc = np.array([16,26,3,7,0,1])
print(np.sort(abc))

arr=["a","c","b","A","F","R","1","&"]
print(np.sort(arr))

#### bolean indexing

""" 
Bolean indexing means selecting elements from a array using boolean values.
It creates a mask based on a condition.
It filter elements where the condition is true.
"""

mask = arr1%5==0
print(mask)