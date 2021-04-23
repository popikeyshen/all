
import cv2
import numpy as np




import math
def rgbToVec(bgr):

	# https://en.wikipedia.org/wiki/Spherical_coordinate_system
	# we convert the rgb coordinates like and xyz сartesian to spherical coordinate system where the value component will be L, and color component - teta and phi angle

	x,y,z=bgr 
	## add little number to avoid division by 0
	x+=1
	y+=1
	z+=1

	# get the value component
	l = (x**2+y**2+z**2)**0.5
	teta = math.acos(z/l)
	phi =  math.atan(y/x)

	gray = l # get the value component

	l=255.0 # set all pixels of gray by 255 to see just the color component with this value
	x = l*math.cos(phi)*math.sin(teta)
	y = l*math.sin(phi)*math.sin(teta)
	z = l*math.cos(teta)
	bgr = x,y,z # get the color component


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

def hsv():
	img = cv2.imread("cat.jpg")
	img = cv2.resize(img, (500,300), interpolation = cv2.INTER_AREA)
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # hue, saturation, value

	### you can look on the hsv components separately
	v = hsv[:,:,2]
	s = hsv[:,:,1]
	h = hsv[:,:,0]
	## the gray part of image (Value)
	cv2.imshow("value(gray)",v)
	cv2.imshow("saturation", s)
	#cv2.imshow("hue", h) # gue in gray scale

	## set all pixels of gray by 255 to see just the color component with this value
	hsv[:,:,2] = hsv[:,:,2]*0+255
	#hsv[:,:,1] = hsv[:,:,1]*0+255  # set saturation to one value

	bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	cv2.imshow("img_hsv",bgr)
	cv2.waitKey(0)

pixToVec()
hsv()
