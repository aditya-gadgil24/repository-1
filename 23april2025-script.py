"""Data engineering- data processing concepts"""

# SIMD instructions for parallel processing of data
import numpy as np
a = np.random.rand(1000000).astype(np.float32)
b = np.random.rand(1000000).astype(np.float32)
c = a + b
print(c)
# end of logic

# begin
import numpy as np
a = np.random.rand(1_000_000)
b = np.random.rand(1_000_000)
c = a + b  # SIMD-accelerated behind the scenes
print(c)
# end

# working with apache arrow data format using pyarrow lib
import pyarrow.compute as pc
import pyarrow as pa

arr = pa.array([1, 2, 3, 4, 5, 6])
result = pc.add(arr, 10)
print(result)
# end

# begin
import polars as pl
df = pl.DataFrame({"a": [1, 2, 3, 4], "b": [10, 20, 30, 40]})
newdf = df.with_columns((pl.col("a") * pl.col("b")).alias("product"))
print(newdf)
# end
