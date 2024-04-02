# Given a  1-D array, negate all the elements which are between 3 and 8
import numpy as np

def negate_between(arr):
  mask = (arr >= 3) & (arr <= 8)
  negated_arr = arr.copy() 
  negated_arr[mask] *= -1
  return negated_arr

array_str = input("Enter elements for the 1D array (separated by spaces): ")
array = np.array([float(x) for x in array_str.split()])

print("\nOriginal array:", array)
print("\nArray after negating elements between: \n", negate_between(array))
