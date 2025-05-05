# Core data types in Python

"""Basic scalar types"""

x = 10
print(type(x))

y = 83.75
print(type(y))

z = 4 + 2j
print(type(z))

e = False
print(type(e))

"""String type/character/text"""
f = 'success'
print(f)
print(type(f))

"""Sequence type"""
list1 = [2, 5, 7, 11, 6]
print(list1)
print(type(list1))

tuple1 = (1, 4, 7, 3)
print(tuple1)
print(type(tuple1))

range = range(10)
print(range)
print(type(range))

"""Set types"""
set1 = {2, 1, 6, 7, 8}
print(set1)
print(type(set1))

frozenset = frozenset([2, 1, 4, 11, 6])
print(type(frozenset))

"""Mapping type"""
oxford = {'name' : 'aditya', 'role' : 'data engineer', 'salary' : 1123462}
print(oxford)
print(type(oxford))


# checking type
print(type(5))             
print(type(10.3))

# getting size of python objects
import sys
size1 = sys.getsizeof(10223)
size2 = sys.getsizeof('volkswagen tiguan')
print(size1)
print(size2)

size3 = sys.getsizeof(True)
print(size3)

size4 = sys.getsizeof('googlemetamicrosoftamazonetflix')
print(size4)

size5 = sys.getsizeof([])
print(size5)

size6 = sys.getsizeof([1001, 1003, 1934, 1934, 2657, 2287, 2812, 2888])
print(size6)

size7 = sys.getsizeof(())
size8 = sys.getsizeof((1, 6, 7))
print(size7)
print(size8)

empdsize = sys.getsizeof({})
dsize = sys.getsizeof({'name' : 'aditya', 'age' : '33', 'domain' : 'big data', 'language' : 'python'})
print(dsize)

setsize = sys.getsizeof({1, 9, 7, 10})
print(setsize)

str_size = sys.getsizeof('ag')
print(str_size)
# This was hands on with the core dtypes and data structures in Python, their memory representation


"""Data structures, dtypes their memory representation, overhead and memory/performance tradeoff is very
important to understand to help select the most efficient dtypes for optimum memory usage and high
performance"""

# working with pandas and numpy libraries and their functions

import pandas as pd
import numpy as np

array = np.array(['a', 2, 'c', 6])
print(array)


