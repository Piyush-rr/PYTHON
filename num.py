import numpy as np
#creating the one dimension array
# arr=np.array([1,2,3,4,5])
# print(arr)


# #creating 0 dimensional array

# arrzero=np.array(50)
# print(arrzero)

# #checking the dimension of the array
# print(arr.ndim)
# print(arrzero.ndim)

# #creating the two dimension array

# arr2=np.array([[12,3,4,6],[3,5,7,8]])
# print(arr2)

# # number of elements
# print(arr2.size)

# #total memory taken by an array

# print(arr2.nbytes)

# #single element size
# print(arr2.itemsize)

# #find the data type of the array
# print(arr2.dtype)

# # .......................................................................
# print(arr2)

# #for the specific element of the array
# print(arr2[0,2])

# #specific row of the array
# print(arr2[0,:])
# print(arr2[1,:])


# # .................................................

# arr3=np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr3)

# #print the bunch of the element
# #(start index: inclusive and last index exclusive)
# print(arr3[1:4])

# #copy the one to another array
# # print(arr3)

# arr4=arr3.copy()
# print(arr4)



# # ...................creating matrix.........................

# #zeroes matrix
# print(np.zeros((4,5)))

# #all 1 matrix

# print(np.ones((3,2,3)))


# # other matrix

# print(np.full((3,4),(33)))


# ...............importing the random number.....................

from numpy import random

# x=random.randint(10)
# print(x)

# #using the random in numpy

# s=np.random.rand(1,2)
# print(s)


##identity matrinx creating 

# p=np.identity(5)
# print(p)

##............Mathematical operation perform ..................

num4=np.array([1,2,3,4,5,6,7,8,9])
print(num4)

num5=num4+5
print(num5)