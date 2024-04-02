#create a random vector with shape(100,2) representing co-ordinates. find point-by-point distances

import numpy as np

coordinates = np.random.rand(100, 2)
distances = np.sqrt(((coordinates[:, np.newaxis] - coordinates) ** 2).sum(axis=2))
distances -= np.diag(np.diagonal(distances))

print("Distances: ", distances)
