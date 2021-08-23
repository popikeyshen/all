import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from sklearn.decomposition import PCA


def vis3d(X):

	x = X[:,0]
	y = X[:,1]
	z = X[:,2]


	fig = plt.figure(figsize=(8,6),dpi=80)
	axis = fig.add_subplot(1,1,1,projection="3d")
	axis.scatter(x.flatten(),y.flatten(),z.flatten(), facecolors='red',marker='.')
	plt.show()


def PCA_sklearn(X, n):

	pca = PCA(n_components=n)
	pc1 = pca.fit_transform(X)

	return pc1


def PCA_from_scratch(X , num_components):
     
    #Step-1
    X_meaned = X - np.mean(X , axis = 0)
     
    #Step-2
    cov_mat = np.cov(X_meaned , rowvar = False)
     
    #Step-3
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
     
    #Step-4
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
     
    #Step-5
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]
     
    #Step-6
    X_reduced = np.dot(eigenvector_subset.transpose() , X_meaned.transpose() ).transpose()
     
    return X_reduced





if __name__ == "__main__":

	X = np.array([[1,1,1], [2,1,1], [2,2,1],[1,2,1],[0,2,1],[1,0,1] ])
	vis3d(X)


	#res = PCA_sklearn(X, 2)
	res = PCA_from_scratch(X , 2)
	print(res)


	plt.plot(res[:,0],res[:,1], '.')
	plt.show()




