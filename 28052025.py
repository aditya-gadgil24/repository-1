"""This script file illustrates the core built in data structures in Python, their internal representation
memory/storage model, footprint, use cases, speed and performance trade offs and properties"""


"""We will start with List"""


"""We will illustrate the internal memory layout or map of the list data structure
using sys library functions"""

# code block

import sys

list1 = []
print(sys.getsizeof(list1))

lsize = sys.getsizeof(list1)
print(lsize)

nv = list1.append(1000)
print(sys.getsizeof(list1))

import sys
tasks = ['wake up', 'exercise', 'breakfast', 'lunch']
tasks.append('dinner')
tasks.append('sleep')
print(tasks)

tasks.remove('exercise')
print(tasks)
print(sys.getsizeof(tasks))


import sys

# Create a list of 10 million integers
data = list(range(10_000_000))

# Check memory usage
print(sys.getsizeof(data))

import sys
list1 = [2553534, 5645332243, 4457424234, 4582312312321432, 532, 49645, 9654, 7344, 923545, 1424343, 911423]
list2 = [13454, 4552323, 343422, 844333, 2323235522323232, 7723232, 656568543, 93434, 123243, 4534, 95342]
list3 = list1 + list2
print(list3)
print(sys.getsizeof(list3))


"""Next lets get to Tuples"""

"""We will illustrate the internal memory layout or map of the tuple data structure
using sys library functions"""

import sys
list1 = []
tuple1 = ()
print(sys.getsizeof(list1))
print(sys.getsizeof(tuple1))

l = [2, 100, 5000]
t = (2, 100, 5000)
print(sys.getsizeof(l))
print(sys.getsizeof(t))


coordinates = (155, 12, 6)
rbgvalue = (246, 5, 9)

print(coordinates)

"""Lets move on to Sets"""

import sys

emp_list = []
emp_set = set()

print(sys.getsizeof(emp_list))
print(sys.getsizeof(emp_set))


import sys
uni_ints = set([1, 3, 1, 4, 5, 2, 1, 3, 6, 1, 3, 3, 6, 1, 4, 6, 1, 6, 2, 3, 1, 3, 1])
print(uni_ints)
print(sys.getsizeof(uni_ints))


name_set = set(['Johnathan', 'Vikings', 'Edwards', 'James'])
if 'Vikings' in name_set:
    print('positive -member')
else:
    print('negative-member')



"""Set operations"""

set1 = {2, 4, 6, 9}
set2 = {9, 2, 5, 1}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)


players = set(['rishabh', 'sai sudharshan', 'shubhman', 'avesh'])
if 'sai sudharshan' in players:
    print('selected')
else:
    print('ousted')


# creating set from list for unique elements

l = [2, 6, 1, 9, 3, 6, 9, 3, 9, 5, 9, 3, 5, 1, 2, 3, 4, 1, 8, 3, 9, 6, 3]
s = set(l)
print(s)


# illus 2

list_emails = ['foo@gmail.com', 'aoo@gmail.com', 'boo@gmail.com', 'aoo@gmail.com', 'hoo@gmail.com']
set_from_list = set(list_emails)
print(set_from_list)

# illus 3

user_ip = '129.234.3.4'
blocked_ip = {'129.234.3.8', '129.233.3.8', '125.345.6.1', '123.210.9.2'}
if user_ip in blocked_ip:
    print('user blocked')
else:
    print('access granted')


"""Lets move on to Dictionary data structure"""

# code 01

import sys
ew = {'mercury' : 123.34, 'uranium' : 245.15, 'titanium' : 198.02, 'sodium' : 141.36}
print(sys.getsizeof(ew))

css = {'font' : 'helvetica', 'color' : 'yellow', 'fontsize' : 12}
print(css)


"""End of file"""