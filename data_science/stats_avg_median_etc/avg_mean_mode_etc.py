
import numpy as np
##https://numpy.org/doc/stable/reference/routines.statistics.html

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
