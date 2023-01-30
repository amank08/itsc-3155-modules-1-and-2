import numpy as np

rand_list = np.random.rand(10)
mean = np.mean(rand_list)
median = np.median(rand_list)
std = np.std(rand_list)

print("List:", rand_list)
print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std)
