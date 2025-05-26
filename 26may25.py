"""This file and its code blocks illustrate the core built in python dtypes, their internal representation
use cases, memory model, speed and performance factors"""

# block1
import sys
x = 12
print(sys.getsizeof(x))

y = 24.1988
print(sys.getsizeof(y))

z = 'stringdtype'
print(sys.getsizeof(z))

l = [2, 4, 9, 1, 5]
print(sys.getsizeof(l))
# end

# block2
import sys
a = 0
print(sys.getsizeof(a))

b = 10000
print(sys.getsizeof(b))

c = 11.53
print(sys.getsizeof(c))

valid_visa = False
print(sys.getsizeof(valid_visa))

str1 = ''
print(sys.getsizeof(str1))

string2 = 'filledstring'
print(sys.getsizeof(string2))

string3 = 'filledstrings'
print(sys.getsizeof(string3))

list1 = []
print(sys.getsizeof(list1))

list2 = [1, 3, 6]
print(sys.getsizeof(list2))

tuple1 = ()
print(sys.getsizeof(tuple1))

tuple2 = (1, 2, 7)
print(sys.getsizeof(tuple2))

dict1 = {}
print(sys.getsizeof(dict1))

dict2 = {'model' : 'distributed'}
print(sys.getsizeof(dict2))


# block 3
import numpy as np
array1 = np.array([2, 6, 9, 3])
print(array1.flags)

"""The following code blocks will illustrate the foundational operations, control flow, functions
logic used in python"""

# block 1
a = 10023
b = 73091
c = 12345
d = 10
e = 8
ops = a + b - c / d * e
print('The output of this operation is:-', ops)

c = 12
d = 8
e = c % d
print(e)

v1 = 12
v2 = 3
v3 = v1 ** v2
print('Hey user, the output of the operation is-', v3)

# block 4
salary = 10.3
us_visa = False
if salary > 10.0 or us_visa:
    print('selection successful')
else:
    print('selection unsuccessful')


product_pstatus = True
p_price = 103
if p_price < 100 and product_pstatus is False:
    print('pass')
else:
    print('drop')

age = 41
it_job = True
if age < 40 or it_job:
    print('eligible')
else:
    print('disqualified')

import sys
de_list = [1, 5, 7, 11, 19, 21, 23, 24, 28, 31, 33, 38, 39, 41, 44, 46, 49, 50, 51, 55, 61, 69, 71, 73, 75]
print(sys.getsizeof(de_list))
for element in de_list:
    if element < 38:
        print('to the left')
    elif element == 38:
        print('in the centre')
    else:
        print('to the right')
# end of code block


iot_readings = [18, 20, 22, 26, 23, 21, 19, 17]
for temperature in iot_readings:
    if temperature < 20:
        print('cold-c')
    elif temperature == 20:
        print('moderate-m')
    else:
        print('hot-h')
# end of code block 


x = 300000
while x < 10000000:
    print(x)
    x = x * 1.25


for i in range(1000):
    print(i)
    i = i * 1.75
# end

x = [2, 9, 12, 19, 21, 22, 24, 29, 31, 34, 36, 38]
for v in x:
    if v % 2 == 0:
        print('even-n')
    else:
        print('odd-n')
# end        

def latency(request, response):
    return response - request
# calling the function with arguments
delay = latency(26, 33)
print('The latency value for the app is-', delay)
# end


strinng = 'dokarmawithnoattachmenttooutcome'
print(strinng)
print(strinng[1:10])
