#Consider a generator function that generates 10 integers and use it to build an array

import numpy as np

def generate_integers():
  for _ in range(10):
    yield np.random.randint(0, 100)  
array = np.fromiter(generate_integers(), dtype=int)
print("Generated array: ", array)
