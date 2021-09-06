



#import statistics
### just for python 3.8
#res = statistics.covariance( x,x)

import numpy as np

# добуток відхиленнь двох величин АБО в теорії ймовірності міра лінійної залежності двух випадкових величин
def cov_from_scratch(a, b):

    if len(a) != len(b):
        return

    a_mean = np.mean(a)
    b_mean = np.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)


if __name__ == '__main__':
	x   = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	y   = [9, 8, 7, 6, 5, 4, 3, 2, 1]

	res = cov_from_scratch(x,y)
	res = np.cov(x,y)
	print(res)

	#  matrix = 	[cov(x*x), cov(y*x)]
	# 	 	[cov(y*y), cov(y*y)]




## Links
## https://en.wikipedia.org/wiki/Covariance_matrix
## https://youtu.be/qtaqvPAeEJY  ## covariance and correlation
