import numpy as np
import cv2 as cv

def kmeansOpenCV(img):
	Z = img.reshape((-1,3))

	# convert to np.float32
	Z = np.float32(Z)
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	K = 8
	ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
	print("centroidsOpencv",center)

	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv.imwrite("./cat_res.png",res2)
	cv.imshow('res2',res2)
	cv.waitKey(0)
	cv.destroyAllWindows()

import numpy as np
from numpy.linalg import norm

class Kmeans:
    '''Implementing Kmeans algorithm.'''

    def __init__(self, n_clusters, max_iter=100, random_state=123):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state

    #1) compute random centroids 
    def initializ_centroids(self, X):
        np.random.RandomState(self.random_state)         # just a random seed =123
        random_idx = np.random.permutation(X.shape[0])   # max index X.shape[0] = w*h
        centroids = X[random_idx[:self.n_clusters]]      # get random pixels from w*h
        return centroids

    #2) compute distance for pixels (elements of vector)
    def compute_distance(self, X, centroids):
        distance = np.zeros((X.shape[0], self.n_clusters))   
        for k in range(self.n_clusters):
            d = X - centroids[k, :]                 # distance of pixels from centroid k
            row_norm = norm(d, axis=1)              # Frobenius norm = sqrt( sum( element^2))
            distance[:, k] = np.square(row_norm)    # ^2
        return distance				    # get distances for every pixel w*h,k for all centers

    #3) get nearest for every pixel
    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)        # get index of to nearest cluster for every pixel

    #4) recompute centroids
    def compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            m = X[labels == k, :]                           # get all pixels for current centroid
            centroids[k, :] = np.mean(m, axis=0)            # get mean for this pull
        return centroids



    def compute_sse(self, X, labels, centroids):
        distance = np.zeros(X.shape[0])
        for k in range(self.n_clusters):
            distance[labels == k] = norm(X[labels == k] - centroids[k], axis=1)
        return np.sum(np.square(distance))
    
    def fit(self, X):
        self.centroids = self.initializ_centroids(X)  			# 1) random centroids
        for i in range(self.max_iter):
            old_centroids = self.centroids
            distance = self.compute_distance(X, old_centroids)		# 2) get distances, every pixel from centers
            self.labels = self.find_closest_cluster(distance)           # 3) get nearest center for every pixel
            self.centroids = self.compute_centroids(X, self.labels)     # 4) recompute centroids, get mean for pixel pulls
            if np.all(old_centroids == self.centroids):
                break

        self.error = self.compute_sse(X, self.labels, self.centroids)
        print(self.error)
    
    def predict(self, X):
        distance = self.compute_distance(X, old_centroids)
        return self.find_closest_cluster(distance)

def kmeansMy(img):
	Z = img.reshape((-1,3))
	# Run local implementation of kmeans
	km = Kmeans(n_clusters=8, max_iter=10)
	km.fit(Z)
	centroids = km.centroids
	label = km.labels
	print("centroidsMy",centroids)

	center = np.uint8(centroids)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv.imwrite("./cat_res.png",res2)
	cv.imshow('res2',res2)
	cv.waitKey(0)
	cv.destroyAllWindows()

# main
img = cv.imread('./cat.jpg')
kmeansOpenCV(img)
kmeansMy(img)










