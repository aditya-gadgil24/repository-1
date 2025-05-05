""" This python file and its code blocks will illustrate the low level technical representation of
Numpy and Pandas data structures and the performance/efficiency trade off for several operations applied"""


"""The first part of the file will deal with Numpy core data structure, nd-arrays, their storage layout, 
memory model, use cases and performance,speed considerations"""


# NUMPY LIB
# nd-Arrays
import numpy as np
import sys
array1 = np.array([4, 1], dtype=np.int32)
print(array1)
print(sys.getsizeof(array1))
# end


# PERFORMANCE COMPARISON OF NUMPY ARRAYS AND PYTHON LISTS
# begin
import time
py_list = list(range(10_000_000))
start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()

print("Python list time:", end - start)
# end

# begin
import numpy as np

np_array = np.arange(10_000_000)
start = time.time()
np_result = np_array * 2
end = time.time()

print("NumPy array time:", end - start)
# end

"""Numpy operatins are 1X times faster than Lists"""



# CREATING NUMPY ndarrays

# Using lists
import numpy as np
array01 = np.array([2, 4], [3, 7], dtype=np.int32)
print(array01)

arr = np.arange(12).reshape(6,2)
print(arr)

"""using constructor methods"""
# begin
zarray = np.zeros((2, 3))
print(zarray)          
onearray = np.ones((2, 3))
print(onearray)           
afull = np.full((2, 3), 24)
print(afull)        
eyea = np.eye(3)
print(eyea)
# end                 

# begin
arr = np.arange(42).reshape(7, 6).astype(np.int8)
print(arr)
print(arr.nbytes)
print(arr.flags)
# end

# CONTIGUOUS MEMORY ILLUSTRATION
import numpy as np
array = np.array([[1, 2, 4], [11, 19, 14]], dtype=np.int32)
print(array)
# end 

""" View and Copy concepts"""

# View shares memory with original memory, copy allocates new memory
# begin
import numpy as np
a = np.array([2, 4, 6, 8, 1, 3])
b = a[1:4]
print(a)
print(b)
# end
b[0] = 24
print(a)
# end of code block 

# copy operation illustration
# begin
b = np.array([16, 47, 83, 88])
print(b)
c = b[0:4].copy()
print(c)
# end

# begin
a = np.arange(6).reshape(2, 3)
print(a)
b = a[:, :2]
print(b)
b[:] = 0
print(a)
# end


# broadcasting in numpy
a = np.ones((1, 1000000))
b = np.ones((1000000, 1))

result = a + b
# end


# begin
import numpy as np

person_dtype = np.dtype([
    ('name', 'S10'),        
    ('age', 'i4'),          
    ('height', 'f4')        
])

data = np.array([
    (b'Alice', 25, 5.5),
    (b'Bob',   30, 6.0)
], dtype=person_dtype)
print(data)
# end

# Working with text.string data type in numpy arrays
# begin
import numpy as np
import sys
txtarray = np.array(['text', 'string'], dtype='U10')
print(txtarray)
print(sys.getsizeof(txtarray))
# end of code block 


# Realistic Use Case (Fixed-length strings)
dt = np.dtype([('name', 'S10'), ('age', 'i4')])
arr = np.array([(b'Alice', 30), (b'Bob', 25)], dtype=dt)
print(arr)
print(sys.getsizeof(arr))
# end 



"""PANDAS SERIES, DATAFRAME, THEIR STRUCTURE, MEMORY MAP, STORAGE LAYOUT, EFFICIENCY AND PERFORMANCE
CHARACTERISTICS, USE CASES"""

# begin
import pandas as pd
import sys
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
print(sys.getsizeof(s))
# end


# Memory Usage in Series

# begin
import pandas as pd
s = pd.Series(range(10**6))
s.memory_usage()
# end 

# Memory Usage in DataFrame
import pandas as pd
df = pd.DataFrame({
"id": range(10**6),
"name": ["user"] * 10**6,
"score": np.random.rand(10**6)
})
print(df)
memdf = df.memory_usage(deep=True)
print(memdf)
# end


"""Comparing Raw NumPy vs Pandas Overhead"""
import numpy as np
np_arr = np.arange(10**6)
pd_series = pd.Series(np_arr)
print(np_arr)
print(pd_series)

np_arr.nbytes           # ~8 MB
pd_series.memory_usage()  # ~8 MB + index overhead
# end

# tools for memory profiling
import numpy as np
import pandas as pd
import sys
print(sys.getsizeof(df))
print(df.memory_usage(deep=True))
# end of code block 



"""This is the end of this python file and its sample code blocks"""





















