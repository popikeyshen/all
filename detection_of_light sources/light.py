
import cv2

# 2d 
def d2():
	## 1) read image

	img = cv2.imread("ball.jpg")

	## 2) remove light

	cv2.imshow("img",img)
	cv2.waitKey(0)


	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	## set all pixels of gray by 255 to see just the color component with this value
	value = hsv.copy()
	hsv[:,:,2] = hsv[:,:,2]*0+200

	img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

	cv2.imshow("img",img)
	cv2.imshow("value",value)
	cv2.waitKey(0)

	from matplotlib import pyplot as plt
	res = abs(hsv.astype(np.float32)-value.astype(np.float32))
	plt.imshow(res)

	line = res[100]
	plt.plot(line)

	plt.show()

from matplotlib import pyplot as plt
import numpy as np
def d1():

	s = np.array([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,10,10,10,10])
	l = np.array([5,5,5,5,5,5,5,5,5,5,5,4,3,2,1,0,10,10,10,10,10,10,10,10,10,10])

	plt.plot(s)
	plt.plot(l)
	plt.show()


if __name__ == '__main__':
	d2()
