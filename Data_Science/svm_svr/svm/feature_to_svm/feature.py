
import cv2
import numpy as np


def data_to_vector(img, true_or_false):
	_,_,c = img.shape
	X1 = img.reshape((-1,c))
	
	if true_or_false==1:
		y1 = np.ones( len(X1))
	else:
		y1 = np.zeros( len(X1))
	
	return X1, y1
	
def concatenate(X1,y1, X2,y2):
	if len(X1)>0:
		X1 = np.concatenate((X1,X2))
		y1 = np.concatenate((y1,y2))
	else:
		X1 = X2
		y1 = y2
	return X1, y1
	
def get_true_false(img, true_or_false):

	box = cv2.selectROI('img', img, fromCenter=False, showCrosshair=False)
	(x,y,w,h) = box
	
	crop = img[y:y+h, x:x+w]
	X1, y1 = data_to_vector(crop, true_or_false)

	return X1, y1



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.decomposition import PCA



def PCA_sklearn(X, n):

	print('PCA...')
	pca = PCA(n_components=n)
	pc1 = pca.fit_transform(X)

	return pc1

def vis3d(X,yy):
	X = np.array(X)
	print('pca shape', X.shape)

	#X = PCA_sklearn(X, 3)
	x = X[:,0]
	y = X[:,1]
	z = X[:,2]
	
	length = len(z)
	
	colors = []
	for i in yy:


		if i == 1:
			colors.append( 'red' )
		elif i == 0:
			colors.append( 'brown' )
		elif i == 2:
			colors.append( 'blue' )
		elif i == 5:
			colors.append( 'blue' )
		elif i == 3:
			colors.append( 'green' )
		elif i == 6:
			colors.append( 'yellow' )
		else:
			colors.append( 'gray' )	
			


	fig = plt.figure(figsize=(8,6),dpi=80)
	axis = fig.add_subplot(1,1,1,projection="3d")
	axis.scatter(x.flatten(),y.flatten(),z.flatten(), facecolors=colors,marker='.')
	plt.show()



from sklearn import svm

if __name__ == "__main__":
	img = cv2.imread('./kiev_google_maps.png')
	
	X, y = [],[]
	while(1):
	
		cv2.imshow('img',img)
		key = cv2.waitKey(5)
		
		if key == ord('t'):
			data_X, data_Y = get_true_false(img, true_or_false=1)
			X,y = concatenate(X,y, data_X, data_Y)
			
		if key == ord('f'):
			data_X, data_Y = get_true_false(img, true_or_false=0)
			X,y = concatenate(X,y, data_X, data_Y)
			
		if key == ord('r'):
			print('train')
			
			clf = svm.SVC()
			clf.fit(X, y)
			
			vec = img.reshape((-1,3))
			res = clf.predict(vec)
			
			#from sklearn.mixture import GaussianMixture
			#gm = GaussianMixture(n_components=5, random_state=0,covariance_type='spherical').fit(X)
			#gm.means_
			#res = gm.predict(vec)
			
			w,h,c = img.shape
			mask = res.reshape((w,h))

			#print(res)
			#vis3d(vec,res)
			
			show = img.copy()
			#show[mask==1,0] +=30
			#show[mask==1,1] +=30
			show[mask==1,2]  =200
			
			cv2.imshow('mask', show)
			cv2.waitKey(0)
			
			save_vec(X, y, 'save')
			
		if key == ord('q'):
			exit()


			
			
			
