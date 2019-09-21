import numpy as np

# 3.1.
# Let V be a vector space with basis:
# {(1, 0, 0),(0,1,0),(0,0,1)}
# Give two different basis for V#V
b1 = np.array([1,0,0])
b2 = np.array([0,1,0])
b3 = np.array([0,0,1])
print(b1,b2,b3)
# combine vectors with stack
b4 = np.stack((b1,b2,b3))
print(b4)
b4.transpose()
# get product
print(np.multiply(b1,b1))
print(np.multiply(b1,b2))

# 3.11
# let psi be an n qubit state
# show that sum of distances between psi and basis vectors
# are bounded by a constant
