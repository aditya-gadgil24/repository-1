# Working with core Python data types

# Float dtype object in python
# Float dtype in Numpy, float32 and float 64

"""The following code blocks illustrate the memory layout, use cases, performance, behavioural 
characteristics of float dtype in python, both object model and raw bytes type in Numpy"""

# begin
import sys
x = 12.56
y = 1.446745454566
size1 = sys.getsizeof(x)
size2 = sys.getsizeof(y)
print(size1)
print(size2)
# end


# begin
list = [9.24, 4.71, 8.18, 3.23]
lsize = sys.getsizeof(list)
print(lsize)
# end


# begin
import time
import numpy as np

# Pure Python
N = 1_000_000
a = [float(i) for i in range(N)]

start = time.time()
b = [x * 1.5 for x in a]
print("Python float time:", round(time.time() - start, 5), "seconds")
# end of logic


# begin
# NumPy float64
a_np = np.arange(N, dtype=np.float64)

start = time.time()
b_np = a_np * 1.5
print("NumPy float64 time:", round(time.time() - start, 5), "seconds")
# end of code

# begin
a_np32 = np.arange(N, dtype=np.float32)
start = time.time()
b_np32 = a_np32 * 1.5
print("NumPy float32 time:", round(time.time() - start, 5), "seconds")
# end of code block 



# COMPLEX NUMBERS

# begin
import cmath

z = 1 + 1j
print(cmath.sqrt(z))       # Square root
print(cmath.phase(z))      # Phase angle
print(cmath.polar(z))      # (r, theta)
print(cmath.exp(z))        # e^(a + bj)
# end


# begin
import time
import numpy as np

N = 1_000_000
py_complex = [complex(i, i + 1) for i in range(N)]

start = time.time()
result_py = [x * (2 + 3j) for x in py_complex]
print("Python complex time:", round(time.time() - start, 5), "seconds")
# end of code block 

# begin
np_complex128 = np.array([complex(i, i + 1) for i in range(N)], dtype=np.complex128)

start = time.time()
result_np128 = np_complex128 * (2 + 3j)
print("NumPy complex128 time:", round(time.time() - start, 5), "seconds")
# end of code block 

# begin
np_complex64 = np.array([complex(i, i + 1) for i in range(N)], dtype=np.complex64)

start = time.time()
result_np64 = np_complex64 * (2 + 3j)
print("NumPy complex64 time:", round(time.time() - start, 5), "seconds")
# end of code block 




# BOOLEAN DATA TYPE

# bool
# begin
import sys
is_american = True
boolsize = sys.getsizeof(is_american)
print(boolsize)
# end of code block

# begin
import time

N = 10_000_000
flags = [True if i % 2 == 0 else False for i in range(N)]

start = time.time()
out = [not f for f in flags]
print("Python bool operation time:", round(time.time() - start, 5), "seconds")
# end

# begin
import numpy as np

np_flags = np.array(flags, dtype=np.bool_)
start = time.time()
out_np = np.logical_not(np_flags)
print("NumPy bool_ operation time:", round(time.time() - start, 5), "seconds")
# end


# STRINGS
import sys
s = 'diamond'
ssize = sys.getsizeof(s)
print(ssize)

s1 = 'thorough123'
s1ze = sys.getsizeof(s1)
print(s1ze)
# end



# begin
import sys
s1 = 'A'
s2 = 'n'
s3 = 'A6n'
print(sys.getsizeof(s1))
print(sys.getsizeof(s2))
print(sys.getsizeof(s3))
# end


# begin
import numpy as np

a = np.array(["foo", "bar"], dtype="U10")  # Unicode (UTF-32)
b = np.array(["foo", "bar"], dtype="S10")  # Byte string (ASCII)

print(sys.getsizeof(a))
print(sys.getsizeof(b))
# end of code block 


# begin
a = "hello"
b = "hello"
a is b
# end

# begin
import sys
x = 'careerswithgoogle'
print(type(x))
print(sys.getsizeof(x))
# end


# begin
import sys
bstr = b"londonengland"
print(type(bstr))
print(sys.getsizeof(bstr))
print(bstr[0:6])
# end

# begin
b = b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87'
s = b.decode("utf-8")  # 'नमस्ते'
# end


# begin
import sys
ba = bytearray(b"bigdataengineering")
print(type(ba))
print(sys.getsizeof(ba))
ba[1] = 75
print(ba)
# end


# begin
s = "NAMASTE"
print(s)
b = s.encode("utf-8")
print(b)        
ba = bytearray(b)
print(ba)            

# Back to str
s2 = ba.decode("utf-8")
print(s2)     
# end 
