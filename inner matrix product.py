import numpy as np

# Define a matrix X
X = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Compute the inner matrix product X^T X using np.dot
result = np.dot(X.T, X)

# Print the result
print("Inner matrix product X^T X:")
print(result)
