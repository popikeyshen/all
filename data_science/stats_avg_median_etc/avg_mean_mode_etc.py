
import numpy as np


def mode():
	data = np.arange(1, 5)
	#array([1, 2, 3, 4])
	res  = np.average(data)
	# 2.5

	a = np.array([[6, 8, 3, 0],
		      [3, 2, 1, 7],
		      [8, 1, 8, 4],
		      [5, 3, 0, 5],
		      [4, 7, 5, 9]])
	from scipy import stats

	res = stats.mode(a)
	#ModeResult(mode=array([[3, 1, 0, 0]]), count=array([[1, 1, 1, 1]]))

	res = stats.mode(a, axis=None)
	#ModeResult(mode=array([3]), count=array([3]))


from scipy import stats
import statistics
if __name__ == '__main__':

	vec = np.array([1,2,3,4,5])

	m 	  = np.mean(vec)
	deviation = np.abs(vec-m)
	print(m,deviation)

	s 	 		= np.std(vec)
	standart_deviation 	= np.sqrt(np.mean(deviation**2))
	print(s,standart_deviation)

	var = statistics.variance(vec) # or
	var = np.var(vec)
	# or 
	## ExpectedValue(deviation)  -мат очікування
	E   = np.sum( vec * 1/5) 	# or sigma
	v = np.sum( (vec - E)**2 )*1/5  #  variance - дисперсія випадкової величини
	print( v, var)

	# np.mean()				Середнє			(1+2+2+3+4+7+9) / 7	4
	# numpy.median()			Медіана			1, 2, 2, 3, 4, 7, 9	3
	# stats.mode()				Мода			1, 2, 2, 3, 4, 7, 9	2
	# np.std()				Стандартне відхилення
	# scipy.stats.rv_discrete.expect() 	Мат очікування


## Links
## https://numpy.org/doc/stable/reference/routines.statistics.html
## https://youtu.be/SzZ6GpcfoQY
## https://en.wikipedia.org/wiki/Variance
## https://docs.python.org/3/library/statistics.html#statistics.variance
## https://machinelearningmastery.com/introduction-to-expected-value-variance-and-covariance/
## https://en.wikipedia.org/wiki/Expected_value






