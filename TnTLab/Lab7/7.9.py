#Consider an array of dimension (5, 5, 3). Multiply it by an array of dimension (5, 5).

import numpy as np

array_3d = np.random.rand(5, 5, 3)
array_2d = np.random.rand(5, 5)

if array_2d.shape[-1] != array_3d.shape[-2]:
  print("Error: Inner dimensions of arrays are not compatible for multiplication.")
else:
  result = np.einsum('ijk,jl->ikl', array_3d, array_2d)
  print("Result of multiplication:")
  print(result)
