
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


from sklearn import svm


import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import  torch.nn.functional as F

class fcnet(nn.Module):
	def __init__(self):
		super(fcnet, self).__init__()
		self.lay1 = nn.Linear(3,10)
		self.lay2 = nn.ReLU()
		self.lay3 = nn.Linear(10,1)
	def forward(self, x):
		x = self.lay1(x)
		x = self.lay2(x)
		x = self.lay3(x)
		x = torch.sigmoid(x)
		return x 

class regressor():
	def __init__(self, X,y):
		X = np.array(X)
		y = np.array([y])

		tx = torch.from_numpy(X).float()
		ty = torch.from_numpy(y).float()
		ty = np.transpose( ty, axes=(1, 0))
		
		print(tx.shape,ty.shape)
		
		net = fcnet()

		criterion = nn.MSELoss()
		learning_rate = 0.05
		optimizer = optim.SGD(net.parameters(),lr=learning_rate,momentum=0.9)

		for i in range(1000):
			optimizer.zero_grad()
			
			
			res = net(tx)
			#print(tx,res,ty)
			loss = criterion( ty, res)

			print(loss)
			
			loss.backward()
			optimizer.step() 

		print(tx,ty,res)
		print(loss)
		self.net = net.eval()

	def predict(self, X):
		X = np.array(X)
		X = torch.from_numpy(X).float()
		res = self.net.forward(X)
		return res

if __name__ == "__main__":
	#img = cv2.imread('/home/popikeyshen/all/cat.jpg')
	img = cv2.imread('/home/popikeyshen/kiev_google_maps.png')
	
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
			
			#clf = svm.SVR()
			#clf.fit(X, y)
			
			print(X.shape, y.shape)
			clf = regressor(X,y)
			
			vec = img.reshape((-1,3))
			res = clf.predict(vec)
			
			w,h,c = img.shape
			mask = res.reshape((w,h))

			
			
			show = img.copy()
			#show[mask==1,0] +=30
			#show[mask==1,1] +=30
			show[mask>0.5,2]  =200
			
			cv2.imshow('mask', show)
			cv2.waitKey(0)
			
		if key == ord('q'):
			exit()


			
			
			
