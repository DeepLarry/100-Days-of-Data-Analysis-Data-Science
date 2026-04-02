import numpy as np

# 1. Creating Matrices
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

print("Matrix A:\n", A)

# 2. Matrix Addition (Element to element)
print("\nAddition (A + B):\n", A + B)

# 3. Transpose (Flip Rows and Columns)
print("\nTranspose of A:\n", A.T)

# 4. Matrix Multiplication (The real deal)
# Iske liye '*' use nahi karte, 'np.dot' ya '@' use karte hain
C = np.dot(A, B) 
print("\nMatrix Multiplication (A . B):\n", C)