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
#print(np.linspace(0,20,7))

#Randon 1D array between 0-1
print(np.random.rand(5))

#Randon 2D array between 0-1
#print(np.random.rand(5,8))

#Random integer array
amolsArr = np.random.randint(0,100,20)
print(amolsArr)
print(amolsArr.argmax())
#print(amolsArr.reshape(5,4))

#Indexing and slicing

arr = np.arange(0,21)
print(arr)
print(arr[16:])
slice = arr[:4]
print(slice)

#copy array
arr2 = arr.copy()


#Working with 2D arrays
d2arr = np.array([[1,2,3],[11,12,13],[21,22,23]])
print(d2arr[1,2])
print(d2arr[:1,1:])

#conditional selection
print(amolsArr[amolsArr >40])

# Array of same numbers
arr7 = np.full(7,7)
ar = np.ones((2,2)) * 3
print(ar)

evenArray = np.arange(10,51,2)
print(evenArray)


## aRRAY BY SHAPE
array2d = np.arange(12).reshape(4,3)
print(array2d)






