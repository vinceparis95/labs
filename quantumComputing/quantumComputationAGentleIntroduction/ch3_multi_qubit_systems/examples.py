import numpy as np
import tensorflow as tf

# build two little vectors
a = np.ones(3)
b = np.ones(3)
c = a + b
print(c)

# give their tensor product
d = a.dot(b)
print(d)

# and their kronecker product
e = np.kron(a,b)
print(e)