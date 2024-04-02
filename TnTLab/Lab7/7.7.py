#Generate a 2D Gaussian array
import numpy as np

mean = float(input("Enter the mean of the Gaussian distribution: "))
std_dev = float(input("Enter the standard deviation of the Gaussian distribution: "))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
size = (rows, cols)

gaussian_array = np.random.normal(mean, std_dev, size)

print(gaussian_array)
