#subtract the mean of each row of a matrix and display it in an array
import numpy as np

rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of columns: "))

matrix=np.empty((rows, cols))

print("Enter the matrix: ")
for i in range(rows):
    elements1 = np.array([float(x) for x in input().split()])
    if len(elements1) != cols:
        print("Error: Invalid number of elements entered. Please enter ", cols, " values.")
        continue
    matrix[i] = elements1

row_means = np.mean(matrix, axis=1)
centered_matrix = matrix - row_means[:, np.newaxis]

print(centered_matrix)
