import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import numpy as np
import cv2


### 3d array visualization
def show3d(img):

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	r,g,b = cv2.split(img)
	#print(cv2.split(img))
	fig = plt.figure(figsize=(8,6),dpi=80)
	axis = fig.add_subplot(1,1,1,projection="3d")

	# Pixel color settings
	pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1],3))

	# Normalized
	norm = colors.Normalize(vmin=-1.,vmax=1.)
	norm.autoscale(pixel_colors)
	# Convert to list
	pixel_colors = norm(pixel_colors).tolist()
	# print('*'*20)

	# Display 3D scatterplot
	axis.scatter(r.flatten(),g.flatten(),b.flatten(),facecolors=pixel_colors,marker='.')
	axis.set_xlabel("Red")
	axis.set_ylabel("Green")
	axis.set_zlabel("Bule")
	plt.show()


def stem_vis():
	func1 = np.array([0,1,2,3,4,5,6,7,8,9,10])
	func2 = np.array([0,1,2,3,4,5,4,3,2,1,0])

	index = range(11)

	plt.stem(index, func1, 'b', markerfmt='bo', label='f1')
	plt.stem(index, func2, 'r', markerfmt='ro', label='f2')
	plt.show()

def title():

	tx1= np.array([ 0,1,2,3,4,5,4,3,2,1,0])
	tx2= np.array([ 0,1,0,1,0,1,0,1,0,1,0])

	tx3 = tx1*tx2
	tx4 = tx1+tx2


	fig = plt.figure()
	plt.title("signals")
	plt.plot(tx1)
	plt.plot(tx2)


	fig = plt.figure()
	plt.title("tx1+tx2, tx1*tx2")
	plt.plot(tx3)
	plt.plot(tx4)

	plt.show()


import torch
import torch.nn as nn
### torch fast big size convolution

if __name__ == "__main__":

	img = cv2.imread("cat.jpg")

	h,w,c = img.shape
	h = int(h/6)
	w = int(w/6)
	img = cv2.resize(img,(w,h))

	#show3d(img)
	stem_vis()
