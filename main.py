'''
There are 6 general mechanisms for creating arrays:

Conversion from other Python structures (i.e. lists and tuples)

Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)

Replicating, joining, or mutating existing arrays

Reading arrays from disk, either from standard or custom formats

Creating arrays from raw bytes through the use of strings or buffers

Use of special library functions (e.g., random)

'''
import numpy as np;

a = np.array([[1,2,3],[4,5,6]], np.int32)

print(a)

print(a[0,2])

a[1,2] = 7

b = a[1,2]

print(f"value of b {b}")

print(a.dtype)

print(a.shape)

print (a.size)

c = np.array({9,8,7})

print(c.dtype)
print(c)


zero = np.zeros((1,9))
print(zero)

num = np.arange(9)

print(num)

lspace = np.linspace(1,9,18)

print(f"linSpace: {lspace}")

emp = np.empty((4,4), np.int32)

print(emp.shape)

print(emp.size)

print(emp)

emp[3,3] = 9

print(emp)

emp_like = np.empty_like(lspace)

print(emp_like)


identity_matrix = np.identity(9)
print(identity_matrix)
# ----------------------------------------------

arr = np.arange(99)
print(arr.shape)

arr_reshape = arr.reshape(3,33)

print(arr_reshape)

print(arr_reshape.shape)


print(arr_reshape.ravel())

#  Multi Dimensional Array


arr = np.arange(60)

re_arr = arr.reshape(3, 20)

print(re_arr.shape)

print(re_arr.size)


axis0_sum = re_arr.sum(axis=0)

axis1_sum = re_arr.sum(axis=1)


print(axis0_sum)
print(axis1_sum)

# Attributes and Method in Numpy

#  Transport
print(re_arr.T)

for item in re_arr.flat:
    print(item)
    
print(re_arr.ndim)

print(re_arr.nbytes)

print(arr.argmax())
print(arr.argmin())

print(arr.argsort())


twoDi = np.array([[1,4,5],[3,2,5],[35,7,5]])

print(twoDi.argmin())

print(twoDi.argmax())

print(twoDi.argsort())

print(twoDi.argmax(axis=0))

print(twoDi.argmin(axis=1))

print(twoDi.argsort(axis=0))

oneDi = twoDi.ravel()

print(oneDi)

reshape = oneDi.reshape((9,1))

print(reshape)

arr1 = np.array([[32,42,53],[2,5,7]])

arr2 = np.array([[43,53,53],[34,35,64]])

print(arr1 + arr2) 

arr3 = arr1 * arr2
print(arr3.dtype)
print(arr3) 

print(np.sqrt(arr1))

print(arr1.sum())

print(np.where(arr1>30))

import sys

python_array = [2,35,5,3]

numpy_array = np.array(python_array)

print(f"python array size: {sys.getsizeof(1) * len(python_array)}")

print(f"Numpy array size: {numpy_array.itemsize * numpy_array.size}")