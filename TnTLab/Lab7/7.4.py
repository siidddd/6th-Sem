#Create a vector of size 10, value ranges from 0 to 1. Sort it in ascending order

import numpy as np

vector = np.random.rand(10)
print("The generated vector: ", vector)
sorted_vector = np.sort(vector)
print("The sorted vector: ", sorted_vector)
