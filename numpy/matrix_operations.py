import numpy as np

# [[0]	                0 0 0 
#  [1]  x  [0,1,0]   =  0 1 0
#  [0]]                 0 0 0

a = np.array([[0], [1], [0]])
b = np.array( [0,   1,   0 ])

print(a*b)


### create 
img = np.zeros((100,100,3))
print(img.shape)

### add new dimension
img = img[..., np.newaxis]
print(img.shape)

m = np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])  # Append values to the end of an array.
print(m)


# https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
m = np.concatenate((a, b), axis=0)

print(m)  # Join a sequence of arrays along an existing axis.


