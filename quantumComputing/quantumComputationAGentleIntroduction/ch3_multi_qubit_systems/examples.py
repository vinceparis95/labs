import numpy as np
import tensorflow as tf

# # build two little vectors
# a = np.ones(3)
# b = np.ones(3)
# c = a + b
# print(c)
#
# # give their tensor product
# d = a.dot(b)
# print(d)
#
# # and their kronecker product
# e = np.kron(a, b)
# print(e)

# example 3.1.1
# create 2 little matrices
a = np.ones((3, 3))
b = np.ones((3, 3))
print(a)
print(b)
c = a.dot(b)
print(c)
l = np.ones(3)
m = np.ones(3)
n = np.dot(l,m)
o = np.kron(l, m)
print(l*m)
print(n, o)

