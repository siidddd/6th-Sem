#Generate 2 random arrays and check whether they are equal or not in numpy array
import numpy as np

rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of columns: "))

array1 = np.random.rand(rows, cols)  
array2 = np.random.rand(rows, cols)  

print("The first generated array: \n", array1)
print("The second generated array: \n", array2)

if np.array_equal(array1, array2):
  print("The two arrays are equal.")
else:
  print("The two arrays are not equal.")