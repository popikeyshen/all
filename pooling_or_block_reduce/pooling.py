import cv2
import numpy as np
import skimage.measure
#https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.block_reduce


def skimage_reduce(img):

	h,w,c = img.shape
	block_size= (150,200,1)
	#block_size= (40,40,1)
	#block_size= (h,w,1)
	print(block_size)

	#reduced = skimage.measure.block_reduce(img, block_size, np.max)
	#reduced = skimage.measure.block_reduce(img, block_size, np.average)
	reduced = skimage.measure.block_reduce(img, block_size, np.median)


	# 'numpy.float64' object cannot be interpreted as an integer
	reduced = reduced.astype(np.uint8)


	reduced = cv2.resize(reduced,(w,h), interpolation = cv2.INTER_NEAREST)
	cv2.imshow("reduced",reduced)
	cv2.imshow("img",img)
	cv2.waitKey(0)

	#res = img-reduced.astype(np.float32)

	return reduced


def my_reduce(img):

	h,w,c = img.shape

	block_size=5
	for y in range(0,h,block_size)[:5]:
		for x in range(0,w,block_size)[:5]:	

			crop = img[y:block_size,x:block_size]

			median = np.median(crop,axis=(0,1))
			median = np.array([[median]]).astype(np.uint8)
			median = cv2.resize(median,(block_size,block_size), interpolation = cv2.INTER_NEAREST)
			
			cv2.imshow("crop",  crop)
			cv2.imshow("median",median)
			cv2.waitKey(0)

			### mode
			#from scipy.stats import mode
			#m = mode(crop,axis=(0,1))
			#print(m)
			#counts = np.bincount(crop,axis=(0,1))
			#print(np.argmax(counts))


if __name__ == "__main__":

	img = cv2.imread("cat.jpg",1)

	#skimage_reduce(img)
	my_reduce(img)

