import cv2
import numpy as np


def block_thrashold(image, block=[50,50,150],size =[50,50,50]):
	img = image.copy()

	### block 2 [0:50...] masks
	b= (img[:,:,0]>block[0]) * (img[:,:,0]<block[0]+size[0]) 
	g= (img[:,:,1]>block[1]) * (img[:,:,1]<block[1]+size[1])
	r= (img[:,:,2]>block[2]) * (img[:,:,2]<block[2]+size[2])
	res = g * b * r

	#img[ res ]=(255,255,255)
	img[ np.invert(res) ]=(0,0,0)

	return img


import time
if __name__ == "__main__":

	img = cv2.imread("cat.jpg")

	
	t0 = time.time()
	thrasholded = block_thrashold(img, block=[30,80,100], size =[60,50,100])
	t1 = time.time()
	print(t1-t0)

	cv2.imshow("",thrasholded)
	cv2.waitKey(0)
