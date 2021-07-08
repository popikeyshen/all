
# feature matching 
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import cv2
import numpy as np

im1 = cv2.imread("im1.jpg",0)
im2 = cv2.imread("im2.jpg",0)

#cv2.imshow("im1",im1)
#cv2.imshow("im2",im2)
#cv2.waitKey(0)

# Initiate SIFT detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(im1,None)
kp2, des2 = orb.detectAndCompute(im2,None)

dist = cv2.norm(des1,des2,cv2.NORM_HAMMING)
print(dist)



