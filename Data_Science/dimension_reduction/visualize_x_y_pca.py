import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from sklearn.decomposition import PCA


def vis3d(X,yy):

	x = X[:,0]
	y = X[:,1]
	z = X[:,2]
	
	length = len(z)
	
	colors = []
	for i in yy:
		if i == 1:
			colors.append( 'blue' )
		else:
			colors.append( 'red' )
			


	fig = plt.figure(figsize=(8,6),dpi=80)
	axis = fig.add_subplot(1,1,1,projection="3d")
	axis.scatter(x.flatten(),y.flatten(),z.flatten(), facecolors=colors,marker='.')
	plt.show()


def PCA_sklearn(X, n):

	pca = PCA(n_components=n)
	pc1 = pca.fit_transform(X)

	return pc1






if __name__ == "__main__":

	X = np.array([[1,1,1], [2,1,1], [2,2,1],[1,2,1],[0,2,1],[1,0,1] ])
	y = np.array([ 0,1,0,1,0,1 ])

	

	res = PCA_sklearn(X, 3)
	print(res)

	
	vis3d(res,y)



