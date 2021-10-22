import numpy as np

def stack():
	### Using your two example arrays:

	a =[[0, 3],
	    [1, 4],
	    [2, 5]]
	    
	b = [[ 6,  9],
	     [ 7, 10],
	     [ 8, 11]]

	print(a.shape, b.shape)
	# (3, 2) (3, 2)

	#np.vstack concatenates along the first dimension...
	print(np.vstack((a, b)).shape)
	# (6, 2)

	#np.hstack concatenates along the second dimension...
	print(np.hstack((a, b)).shape)
	# (3, 4)

	#and np.dstack concatenates along the third dimension.
	print(np.dstack((a, b)).shape)
	## (3, 2, 2)

	#h,w,c = data.shape 
	#channel8 =  np.zeros((h,w,8), dtype='uint8')
	#channel8[:,:,:3]=crop
	#channel8[:,:,3]=cropN[:,:]
	#channel8[:,:,4:7]=crop2
	#channel8[:,:,7]=cropN2[:,:]
	### make 4 channel pixels
	#channel8 = np.dstack((  crop[:,:,0],crop[:,:,1],crop[:,:,2],cropN,  crop2[:,:,0],crop2[:,:,1],crop2[:,:,2],cropN2  ))
	#channel8 = np.dstack((  crop,cropN,  crop2,cropN2, features  ))

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




