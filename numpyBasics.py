import numpy as np

amols_list = [1,4,6,7]
arr = np.array(amols_list)
print(arr)

# Create a range array
print(np.arange(1,31))
# Create range array with step
print(np.arange(1,31,5))

#Array of zeros
print(np.zeros(5))
#Array of ones
print(np.ones(6))
#Properly spaced array
print(np.linspace(0,20,3))
print(np.linspace(0,20,5))
print(np.linspace(0,20,7))

#Randon 1D array between 0-1
print(np.random.rand(5))

#Randon 2D array between 0-1
print(np.random.rand(5,8))