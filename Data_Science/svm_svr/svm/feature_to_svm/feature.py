
import cv2
import numpy as np
import pickle

def save_vec(vec_X,vec_y, name):
	print('len ',len(vec_X), ', data save..')
	if len(vec_X)>0:
		with open(name+'.pickle', 'wb') as f_out:
			pickle.dump((vec_X,vec_y), f_out)

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
			
			w,h,c = img.shape
			mask = res.reshape((w,h))

			
			show = img.copy()
			#show[mask==1,0] +=30
			#show[mask==1,1] +=30
			show[mask==1,2]  =200
			
			cv2.imshow('mask', show)
			cv2.waitKey(0)
			
			save_vec(X, y, 'save')
			
		if key == ord('q'):
			exit()


			
			
			
