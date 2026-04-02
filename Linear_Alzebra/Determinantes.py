import numpy as np
A = np.array([[1, 2], [3, 4]])

# Determinant
det = np.linalg.det(A)
print(f"Determinant: {det}")

# Inverse
if det != 0:
    inv_A = np.linalg.inv(A)
    print(f"Inverse of A:\n{inv_A}")