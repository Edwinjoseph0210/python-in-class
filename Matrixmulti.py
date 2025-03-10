import numpy as np

# Define two matrices A and B
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

# Perform matrix multiplication
result = np.dot(A, B)

# Print the result
print("Matrix Multiplication using np.dot():")
print(result)
