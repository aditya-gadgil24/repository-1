"""Working with numpy n-dimensional arrays, their properties, performance, behaviour and use cases"""

# importing the library
import sys
import numpy as np

a = [1] * 1000000
b = np.ones(1000000, dtype=np.int32)

print("list size:", sys.getsizeof(a))      # ~8MB
print("numpy size:", b.nbytes)            # ~4MB

# array array
import array
a = array.array('i', [1, 1, 2, 4])
print(a)

# contiguous/non contiguous memory. 
# python objects, arrays, dataframes, series
arr = np.array([1, 9, 11, 76])
print(arr.flags)

"""Contiguous memory means data is laid out back to back 
in a single block of RAM with no gaps between elements"""

x = 1
y = 6
z = x + y
print('The output of the operation is:-', z)

# block 2
a = 'fc'
b = 'kj'
c = a + b
print(c)

# block 3
import sys
x = [1, 4, 7]
xsize = sys.getsizeof(x)
print(xsize)

# block 4
a = 13.47
asize = sys.getsizeof(a)
print('The size of this object is:', asize)

# block 5
b = 'string'
strsize = sys.getsizeof(b)
print('The size of the python object is', strsize)

# block 6
tuple_1 = (203, 454)
tuple_size = sys.getsizeof(tuple_1)
print('The size of python data structure is:', tuple_size)

# block 7
import numpy as np
import pandas as pd
array1 = np.array([1, 3])
print(array1)
arraysize = sys.getsizeof(array1)
print(arraysize)

# block 8
arr1 = np.array([2, 5, 7, 9])
arr2 = np.array([3, 1, 8, 6])
array_add = np.add(arr1, arr2)
print(array_add)
array_sub = np.subtract(arr1, arr2)
print(array_sub)
product = np.multiply(arr1, arr2)
print(product)
remainder = np.divide(arr1, arr2)
print(remainder)
# end of code block


# block 9
"""Creating arrays with ones and zeros for initialization and sample data"""

# creating arrays with ones, 1d and 2d
import numpy as np
numpy_1d = np.zeros(10)
print(numpy_1d)
numpy_2d = np.zeros((7, 3))
print(numpy_2d)

# creating 1d and 2d arrays with ones

array_1d = np.ones(5)
print(array_1d)
array_2d = np.ones((10, 3))
print(array_2d)
# end of code block

