import numpy as np
import cv2



img = cv2.imread('./cat.jpg')

def points(event, x, y, flags, param):
	# grab references to the global variables
	global  img
	if event == cv2.EVENT_LBUTTONDBLCLK:
		print(x,y)
		cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
		cv2.imshow('img',img)
		
cv2.namedWindow("img")
cv2.setMouseCallback("img", points)

cv2.imshow('img',img)
cv2.waitKey(0)


