pip install numpy
import numpy as np

arr = np.random.rand(10)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)