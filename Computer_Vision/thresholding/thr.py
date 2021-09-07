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


## 3 types of thr from opencv documentation
# documentation https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html
# source https://github.com/opencv/opencv/blob/master/modules/imgproc/src/thresh.cpp
# for adaptive threshold we use not the mean full image threshold, but we have cell mean
def adaptive_gaussian():
	import cv2 as cv
	import numpy as np
	from matplotlib import pyplot as plt
	img = cv.imread('sudoku.png',0)
	#img = cv.medianBlur(img,5)
	ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
	th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,     cv.THRESH_BINARY,11,2)
	th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
	titles = ['Original Image', 'Global Thresholding (v = 127)',
		    'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
	images = [img, th1, th2, th3]
	for i in range(4):
	    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	    plt.title(titles[i])
	    plt.xticks([]),plt.yticks([])
	plt.show()


import time
if __name__ == "__main__":

	img = cv2.imread("cat.jpg")

	
	t0 = time.time()
	thrasholded = block_thrashold(img, block=[30,80,100], size =[60,50,100])
	t1 = time.time()
	print(t1-t0)

	cv2.imshow("",thrasholded)
	cv2.waitKey(0)

	adaptive_gaussian()
