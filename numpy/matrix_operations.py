import numpy as np

# [[0]	                0 0 0 
#  [1]  x  [0,1,0]   =  0 1 0
#  [0]]                 0 0 0

a = np.array([[0], [1], [0]])
b = np.array( [0,   1,   0 ])

print(a*b)

