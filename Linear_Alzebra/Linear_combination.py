import numpy as np
# Linear Combination Practice
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Scalars (Weights)
a = 3
b = 5

# Creating a Linear Combination
w = (a * v1) + (b * v2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Linear Combination (3*v1 + 5*v2): {w}")


#Output:
#Vector 1: [1 0]
#Vector 2: [0 1]
#Linear Combination (3*v1 + 5*v2): [3 5]