#Multiply 5x3 by 3x2 matrix by numpy array
import numpy as np

matrix1 = np.empty((5, 3))
matrix2 = np.empty((3, 2))

print("Enter the first matrix: ")
for i in range(5):
    elements1 = np.array([float(x) for x in input().split()])
    if len(elements1) != 3:
        print("Error: Invalid number of elements entered. Please enter 3 values.")
        continue
    matrix1[i] = elements1

print("Enter the second matrix: ")
for i in range(3):
    elements2 = np.array([float(x) for x in input().split()])
    if len(elements2) != 2:
        print("Error: Invalid number of elements entered. Please enter 2 values.")
        continue
    matrix2[i] = elements2
    
# Print the user-created matrix
print("Matrix 1: \n", matrix1)
print("Matrix 2: \n", matrix2)
print("Product of the two matrices: \n", np.dot(matrix1, matrix2))
