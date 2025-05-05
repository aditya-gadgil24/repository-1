# Working with lists

# Concatenation
list1 = [23, 29, 31, 33, 37, 39, 41]
list2 = [44, 47, 49, 55, 59, 61, 65]
comb_list = list1 + list2
print(comb_list)

# Repetition
my_list = ['a', 'g', 'x', 'f']
rep_list = my_list * 5
print(rep_list)

# Membership
list_a = [11, 43, 29, 31, 33, 37, 61]
print(61 in list_a)
print(11 not in list_a)

# Indexing [starts at 0]
list_q = [13, 7, 19, 24, 15, 1, 30, 8]
print(list_q[0])
print(list_q[-1])

# Slicing
our_list = [6, 9, 1, 3, 8, 0]
print(our_list[0:5])
print(our_list[:3])
print(our_list[1:6])


"""Built in functions"""
# len
my_list = [2, 9, 7, 4, 6]
print(len(my_list))

# max
my_list = [1, 3, 6, 7, 9, 11, 17, 8]
print(max(my_list))

# min
list_py = [4, 3, 8, 11, 14, 9, 10]
print(min(list_py))

# sum
list_sm = [10, 11, 20, 22, 31, 33, 32, 42]
addition = sum(list_sm)
print('The output of this function is', addition)


# sorted(iterable, key=None, reverse=False)

list_my = [2, 5, 1, 3, 9, 7, 10, 13, 11, 15, 12]
print(sorted(list_my, reverse=True))
print(sorted(list_my))
# end

# The list() function converts an iterable (e.g., tuple, set, or string) into a list.
tuple_ds = (10, 7, 3, 11, 15, 17)
# Converting a tuple to a list
list_from_tuple = list(tuple_ds)
print(list_from_tuple)

# string to list
string_1 = 'stevejobswaslegend'
list_from_string = list(string_1)
print(list_from_string)


# zip(*iterables)
brides = ['neha', 'vishakha', 'madhura', 'devika']
ages = [33, 34, 31, 36]
zipped = zip(brides, ages)
print(list(zipped))


# List Methods (Modifying the List In-Place)

# append(element)
list_p = [24, 5, 1988]
new_element = list_p.append(36)
print(list_p)

# extend(iterable)

list_d = [97, 88, 81, 77, 72]
list_ext = [10, 15, 11, 13, 19]
new_list = list_d.extend(list_ext)
print(new_list)

# insert(index, element): Inserts an element at a specific index

my_list = [2, 9]
my_list.insert(0, 3)
print(my_list)
# e

# b
other_list = ['aditya', 'gadgil', 'vishakha']
other_list.insert(3, 'kalkar')
print(other_list)

# remove(value): Removes the first occurrence of a specified value from the list. Raises a ValueError if the value is not found.
list_a = [7, 4, 6, 4, 9, 10, 4]
list_a.remove(7)
print(list_a)

# pop(index=-1):Removes and returns the element at the specified index. If no index is provided, it removes, returns the last element.
my_list = ['apple', 'iphone16', 'apple', 'iwatch', 'googlepixel']
purged_element = my_list.pop(4)
print(purged_element)

# clear(): Removes all elements from the list, making it an empty list
mah_list = [1, 10, 15, 45, 91, 181, 366, 412]
empty_list = mah_list.clear()
print(empty_list)

# index(value, start=0, end=sys.maxsize): Returns the index of the first occurrence of a specified value.
# Raises a ValueError if the value is not found.
list_my = ['banana', 'sapota', 'custard apple', 'mango']
print(list_my.index('banana'))

# count(value): Returns the number of times a specified value appears in the list

my_list = [1, 2, 2, 3, 2, 4, 5, 7, 5, 9, 11, 5, 13, 5, 4, 6, 4, 11, 4, 5, 11, 5]
print(my_list.count(5))
print(my_list.count(4))
# end


# sort(key=None, reverse=False): Sorts the elements of the list in-place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  
numbers.sort(reverse=True)
words = ["apple", "banana", "cherry"]
words.sort(key=len)
print(words)


# reverse(): Reverses the order of the elements in the list in-place.
my_list = [78500, 83000, 92000, 97575, 89525]
my_list.reverse()
print(my_list)

# TUPLES

"""This code block will work with different funtions and operations for Python Tuples"""
# Basic Operations (Similar to Lists, but Tuples are Immutable):

# Concatenation (+): Combines two tuples into a new tuple.
tuple1 = (41, 23, 31)
tuple2 = (54, 65, 76)
comb_tuple = tuple1 + tuple2
print(comb_tuple)

# Repetition (*): Repeats the elements of a tuple a specified number of times
my_tuple = ('simplify', 'focus')
cartesian_tuple = my_tuple * 3
print(cartesian_tuple)

# Membership (in, not in): Checks if an element exists in the tuple.
my_tuple = (11, 40, 53)
print(40 in my_tuple)
print(53 not in my_tuple)

# Indexing ([]): Accesses an element at a specific position (index)
my_tuple = ('microsoft', 'apple', 'adobe', 'meta')
print(my_tuple[3])
print(my_tuple[0])

# Slicing ([:]): Extracts a sub-tuple from a tuple
my_tuple = (11, 27, 17, 29, 31, 33)
print(my_tuple[0:4])   
print(my_tuple[:3])
print(my_tuple[5])

# Built-in Functions

# len(tuple): Returns the number of elements in the tuple.
my_tuple = (1, 3, 5, 45, 454, 6767, 232, 6768, 23, 6878, 898, 343, 123, 567, 6777878,2212, 455, 78344, 773, 5, 121, 45)
print(len(my_tuple))

# max(tuple): Returns the largest element in the tuple
numbers = (17, 5, 9, 11, 21, 27, 29, 33)
print(max(numbers))

# min
tuple_1 = (11, 1, 23, 8, 17, 24, 6)
print(min(tuple1))

# sum(tuple): Returns the sum of all elements in the tuple
tuple_ds = (99, 91, 87, 83, 79, 72, 68, 61)
print(sum(tuple_ds))

# sorted(iterable, key=None, reverse=False): Returns a new sorted list from the elements of an iterable

tuple_1 = (13, 11, 24, 31, 45, 19, 32, 46)
sorted_t = sorted(tuple_1)
print(sorted_t)

# tuple(iterable): Converts an iterable into a tuple
my_list = [1, 30, 15, 24]
t_from_l = tuple(my_list)  

my_string = "salesforcecloud"
t_from_s = tuple(my_string)
print(t_from_s)


# zip(*iterables): Returns an iterator of tuples
names = ("Steve", "Bill", "Jeff")
ages = (65, 50, 48)
zipped = zip(names, ages)
print(list(zipped))  
print(tuple(zipped))

# Tuple Methods (Limited due to Immutability):

# count(value): Returns the number of times a specified value appears in the tuple.
tuple_1 = (1, 6, 6, 2, 3, 1, 5, 6, 7, 1, 9, 1, 2, 2, 3, 4, 1, 6, 1, 6, 7, 9, 4, 5, 6, 4, 1, 5, 1, 6, 3, 6, 1, 2, 1, 6, 1, 5, 7, 1)
print(tuple_1.count(1))
print(tuple_1.count(6))

# index(value, start=0, end=sys.maxsize): Returns the index of the first occurrence of a specified value. 
# Raises a ValueError if the value is not found
my_tuple = ('apple', 'banana', 'cherry', 'banana')
print(my_tuple.index('apple'))     
print(my_tuple.index('banana', 2))


# Dictionary
# Accessing Values by Key ([]): Retrieves the value associated with a given key.
my_dict = {'name': 'iphone', 'age': 89999, 'brand' : 'samsung', 'model' : 'galaxy a25'}
print(my_dict['brand'])

# Adding or Modifying Key-Value Pairs ([] assignment):
my_dict = {'name': 'Bob', 'city': 'New York'}
my_dict['age'] = 36
my_dict['income'] = 455672
my_dict['name'] = 'aadoo'
print(my_dict)

# Membership (in, not in): Checks if a key exists in the dictionary (not the values).

my_dict = {'x': 1, 'c': 2, 'a' : 31, 'eligibility' : 'yes'}
print('a' in my_dict)     
print('x' not in my_dict)  

# len(dictionary): Returns the number of key-value pairs (items) in the dictionary.
dicto = {'category' : 'apparels', 'brand' : 'gucci', 'gender' : 'female', 'clothing' : 'pants'}
print(len(dicto))

# Dictionary Methods:
# get(key, default=None): Returns the value for the specified key. If the key is not found, it returns the default value

my_dict = {'name': 'Coldnvindictive', 'country': 'Australia'}
print(my_dict.get('name'))      
print(my_dict.get('city'))  

# keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {'x': 11, 'y': 42, 'r': 29}
print(my_dict.keys())
for keys in my_dict.keys():
    print(keys)



# values(): Returns a view object that displays a list of all the values in the dictionary
my_dict = {'metal' : 'gold', 'price' : 90570, 'location' : 'mumbai', 'country' : 'india'}
print(my_dict.values())
for values in my_dict.values():
    print(values)


# items(): Returns a view object that displays list of all key-value pairs (as tuples) in dictionary
oxford = {'product' : 'beer', 'cost' : 195, 'alcohol percentage' : '12', 'brand' : 'kingfisher'}
print(oxford.items())

# update([other]): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs
dict_a = {'a' : 11, 'b' : 17, 'c' : 23}
dict_b = {'p' : 21, 'q' : 32, 'r' : 18}
print(dict_a)

# pop(key, default=...): Removes the key and returns its corresponding value.
dairy_catalog = {
    "Amul Full Cream Milk 1L": 64.0,
    "Mother Dairy Toned Milk 500ml": 28.0,
    "Amul Paneer 200g": 85.0,
    "Gowardhan Ghee 1L": 550.0,
    "Nestle Flavored Milk 180ml": 30.0,
    "Amul Butter 100g": 52.0,
    "Mother Dairy Dahi 400g": 50.0,
    "Amul Cheese Slices 200g": 120.0,
    "Gowardhan Fresh Cream 200ml": 60.0,
    "Amul Kool Badam 200ml": 25.0
}

purg_key = dairy_catalog.pop('Amul Butter 100g')
print(purg_key)


# popitem(): Removes and returns the last inserted key-value pair as a tuple
my_dict = {'a': 11, 'b': 82, 'c': 73, 'f' : 51}
item = my_dict.popitem()
print(item)       
print(my_dict)    


























   

















