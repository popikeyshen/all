
import cv2
import numpy as np


# https://en.wikipedia.org/wiki/Spherical_coordinate_system

import math
def rgbToVec(bgr):
	x,y,z=bgr
	x+=10
	y+=10
	z+=10


	l = (x**2+y**2+z**2)**0.5
	teta = math.acos(z/l)
	phi =  math.atan(y/x)

	gray = l

	l=255.0
	x = l*math.cos(phi)*math.sin(teta)
	y = l*math.sin(phi)*math.sin(teta)
	z = l*math.cos(teta)
	bgr = x,y,z


	return bgr, int(gray/2)

def pixToVec():
	img = cv2.imread("cat.jpg")
	img = cv2.resize(img, (500,300), interpolation = cv2.INTER_AREA)
	cv2.imwrite("./orig.jpg",img)
	#gray = cv2.imread("123.jpg",0)
	#gray = gray*0+100
	h,w,c = img.shape

	gray = np.zeros((h,w,1),  np.uint8)

	cv2.imshow("orig",img)

	for hh in range(h):
		for ww in range(w):
			bgr          = img[hh,ww]
			bgr,g	     = rgbToVec(bgr)
			img[hh,ww]   = bgr
			gray[hh,ww]  = g
			
	cv2.imshow("rgb",img)
	cv2.imshow("gray",gray)

	cv2.imwrite("./rgb.jpg",img)
	cv2.imwrite("./gray.jpg",gray)

	cv2.waitKey(0)

pixToVec()

