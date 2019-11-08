import numpy as np

m = np.array([[1, 9], [5, 5]], np.int32)
print(m)

n = np.array([[2, 3], [5, 1]], np.int32)
print(n)

mn = m + n
print(mn)

mn = m * n
print(mn)
# 2, 27, 25, 5

d = np.dot(m, n)
print(d)
# 1x2 + 9x5, 1x3 + 9x1; 5x2 + 5x5, 5x3 + 5x1
# 3+45, 3+9, 10+25, 15+5
# 48, 12, 35, 20

k = np.kron(m,n)
print(k)
