#swap 2 rows of an array

import numpy as np

def swap_rows(array, row1, row2):
    array[[row1, row2]] = array[[row2, row1]]
    return array

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

array = np.random.randint(1, 100, size=(rows, cols))
print("Original Array:")
print(array)

row1 = int(input("Enter the first row index to swap: "))
row2 = int(input("Enter the second row index to swap: "))

if row1 >= rows or row2 >= rows or row1 < 0 or row2 < 0:
    print("Invalid row indices!")
else:
    array = swap_rows(array, row1, row2)
    print("\nArray after swapping rows:")
    print(array)
