import numpy as np

# Creating a 3x3 Matrix
A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# 1. Transpose
print(f"Transpose:\n{A.T}")

# 2. Rank of Matrix
rank = np.linalg.matrix_rank(A)
print(f"Rank of A: {rank}") 
# Note: If rank < 3, it means some rows are dependent!

# 3. Identity Matrix
I = np.eye(3) # Creates a 3x3 Identity matrix
print(f"Identity Matrix:\n{I}")

# 4. Determinant
det = np.linalg.det(A)
print(f"Determinant: {det:.2f}")

# 5. Inverse (Only if det != 0)
# A above has det=0 (rank 2), so let's use a different one
B = np.array([[1, 2], [3, 4]])
inv_B = np.linalg.inv(B)
print(f"Inverse of B:\n{inv_B}")