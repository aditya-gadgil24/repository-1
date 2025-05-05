# WORKING WITH CORE BUILT IN DATA STRUCTURES IN PYTHON


# LISTS 
# memory model and storage layout of List
# begin
import sys
list1 = [2, 7, 3, 9]
list1.append(10)
print(list1)
list1.remove(2)
print(list1)
print(sys.getsizeof(list1))
nlist = []
print(sys.getsizeof(nlist))
add1 = nlist.append(1)
print(sys.getsizeof(nlist))


# list comprehension and generator expression
# begin
import sys
list2 = [x * 3 for x in range(100)]
print(list2)
print(sys.getsizeof(list2))  # prints the memory model of the list

list3 = (x * 2 for x in range(50))
print(list3)
print(sys.getsizeof(list3))
# end of code block 

# begin
import sys

N = 10**6

list_comp = [x * 2 for x in range(N)]
gen_expr = (x * 2 for x in range(N))

print("List comprehension size:", sys.getsizeof(list_comp))
print("Generator expression size:", sys.getsizeof(gen_expr))
# end of code block 

# begin
import sys
frst = [21, 30, 51]
print('The size of this list type data structure is:', sys.getsizeof(frst))
# end


# begin
import sys

empty = []
print(sys.getsizeof(empty))  

one = [1]
print(sys.getsizeof(one))    

four = [1, 2, 3, 4]
print(sys.getsizeof(four))   

ten = list(range(10))
print(sys.getsizeof(ten))


# begin
lst = [10, 20, 30, 40]

for idx, item in enumerate(lst):
    print(f"Index {idx}: Value = {item}, id = {id(item)}")

# end

# begin
import gc
lst = [10, 20, 30, 40]
print(gc.get_referents(lst))
# end

"""This ends the analysis of Lists type built in data structure in Python"""



# TUPLES
# USE CASES, PERFORMANCE/SPEED, MEMORY MODEL, STORAGE LAYOUT

# begin
import  sys
t1 = (1, 2, 7)
t2 = 2, 6, 9
t3 = (4, )
t4 = tuple([2, 4, 8])
print(sys.getsizeof(t1))
print(sys.getsizeof(t2))
print(sys.getsizeof(t3))
print(sys.getsizeof(t4))
# end

# begin
# memory model comparison of lists and tuples
import sys
lst = [2, 4, 88]
tpl = (2, 4, 88)
print(sys.getsizeof(lst))
print(sys.getsizeof(tpl))
# end 


"""Program to illustrate the mutability of elements inside a tuple"""

# begin
lst = [1, 2, 3]
tple = (lst, "hello", 62)

print(tple)

# Now mutate the list inside the tuple
lst.append(9)

print(tple)
# end

# tuple packing illustration
tupal = 2, 30, 1, 15
print(tupal)
# end



# DICTIONARY

# MEMORY MODEL, USE CASES, PERFORMANCE, SPEED OF OPERATIONS 

# begin
import sys
dct = {'a' : 7, 'b' : 5}
print(sys.getsizeof(dct))
# end 

# begin
import sys
ed = {}
print(ed)
print(sys.getsizeof(ed))


ed['best'] = 1
print(ed)

ed['better'] = 2
ed['poor'] = 1
ed['worst'] = 0
print(ed)
# end



# SETS

# USE CASES, PERFORMANCE/SPEED, MEMORY MODEL, STORAGE LAYOUT
# begin
import sys
s = {'x', 'v', 'b', 'g'}
print(s)
print(sys.getsizeof(s))

s.add('p')
s.add('u')
print(s)
print(sys.getsizeof(s))
# end

# begin
import sys
zs = {}
print(sys.getsizeof(zs))
# end


# begin
import sys
# Step-by-step memory usage of set during insertions (using literal syntax)
s_literal_step_by_step = {1, 2}  # Starting with two elements
initial_memory_literal = sys.getsizeof(s_literal_step_by_step)

# Insert additional elements one by one
elements = [3, 4, 5, 6, 7]
memory_usage_literal_step_by_step = [initial_memory_literal]

for element in elements:
    s_literal_step_by_step.add(element)
    memory_usage_literal_step_by_step.append(sys.getsizeof(s_literal_step_by_step))

memory_usage_literal_step_by_step
# end of code block 


# FROZEN SETS
# USE CASES, MEMORY MODEL, SPACE LAYOUT, PERFORMANCE/SPEED FACTORS
import sys
f = frozenset({1, 5, 9})
print(type(f))
print(sys.getsizeof(f))
# end 

"""The script demonstrates the use cases, performance, speed of operations, memory map, overhead and storage
considerations and implications for all core built in data structures in Python"""


"""The sample code blocks used in the tech documentation are strictly illustrative and should only be used 
for learning"""






