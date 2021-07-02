import cv2
import numpy as np
import skimage.measure
#https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.block_reduce


def skimage_reduce(img):

	h,w,c = img.shape
	#block_size= (40,40,1)
	#block_size= (40,40,1)
	block_size= (h,w,1)
	print(block_size)

	reduced = skimage.measure.block_reduce(img, block_size, np.max)
	#reduced = skimage.measure.block_reduce(img, block_size, np.average)
	#reduced = skimage.measure.block_reduce(img, block_size, np.median)


	# 'numpy.float64' object cannot be interpreted as an integer
	reduced = reduced.astype(np.uint8)


	reduced = cv2.resize(reduced,(w,h), interpolation = cv2.INTER_NEAREST)
	cv2.imshow("reduced",reduced)
	cv2.imshow("img",img)
	cv2.waitKey(0)

	#res = img-reduced.astype(np.float32)

	return reduced


if __name__ == "__main__":

	img = cv2.imread("cat.jpg",1)

	skimage_reduce(img)
