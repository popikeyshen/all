

### https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
### identifier		class name		args		distance function
### “euclidean”							sqrt(sum((x - y)^2))
### “manhattan”							sum(|x - y|)

### https://scikit-learn.org/stable/modules/metrics.html#metrics
### distance metrics
###
### Distance metrics are functions d(a, b). To be a ‘true’ metric, it must obey the following four conditions:
### 1. d(a, b) >= 0, for all a and b
### 2. d(a, b) == 0, if and only if a = b, positive definiteness
### 3. d(a, b) == d(b, a), symmetry
### 4. d(a, c) <= d(a, b) + d(b, c), the triangle inequality

from numpy import linalg as LA
from sklearn.metrics.pairwise import cosine_distances
### 1) cosine similarity


X=[[0,0],[1,0]]
Y=[[0,1],[1,1]]
dist = cosine_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)

X=[[0,0],[1,1]]
Y=[[0,0],[1,1]]
dist = cosine_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)

X=[[0,0],[1,1]]
Y=[[1,1],[0,0]]
dist = cosine_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)


from sklearn.metrics.pairwise import euclidean_distances
### 2) euclidean similarity


X=[[0,0],[1,0]]
Y=[[0,1],[1,1]]
dist = euclidean_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)

X=[[0,0],[1,1]]
Y=[[0,0],[1,1]]
dist = euclidean_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)

X=[[0,0],[1,1]]
Y=[[1,1],[0,0]]
dist = euclidean_distances(X, Y)
print( dist )
det = LA.det(dist )
print(det)


### 3) manhattan_distances
### https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances
from sklearn.metrics.pairwise import manhattan_distances
dist = manhattan_distances([[3]], [[3]])
print(dist)

dist = manhattan_distances([[1]], [[3]])
print(dist)

X=[[0,0],[2,0]]
Y=[[0,2],[2,2]]
dist = manhattan_distances(X, Y)
print(dist)
det = LA.det(dist )
print(det)


