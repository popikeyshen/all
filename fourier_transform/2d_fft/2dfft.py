
import numpy as np
import cv2
from matplotlib import pyplot as plt

def fft_to_image():
	sp_matrix = np.zeros([100,100],dtype=int)
	sp_matrix[95,95]=3000
	sp_matrix[50,50]=3000
	sp_matrix[25,25]=3000

	plt.imshow(sp_matrix)
	plt.show()

	sig = np.fft.ifft(sp_matrix)

	sig+=30
	sig/=100.0

	plt.plot(sig[50])
	plt.imshow(abs(sig))
	plt.show()


def d1_sin_to_2dfft():
	#1) create sin
	x = np.linspace(0, 1, 100)
	sin = (np.sin(x*10)+1)*100
	plt.plot(sin)
	plt.show()
	sin = np.array(sin)

	#2) add in to matrix
	image = np.zeros([100,100],dtype=int)
	image[:,50]=sin
	image[:,49]=sin
	image[:,48]=sin
	image[:,47]=sin
	image[:,46]=sin
	
	plt.imshow(image)
	plt.show()


	#3) sin image to spectre
	sp = np.fft.fft(image)

	plt.imshow(abs(sp))
	plt.show()


	sp_shifted = np.fft.fftshift(sp) # null freq is in center
	plt.imshow(abs(sp_shifted))
	plt.show()

def detect_blur_fft(image=0, size=60, thresh=10, vis=True):
	image  = cv2.imread("/home/popikeyshen/circle.jpg",0)

	# grab the dimensions of the image and use the dimensions to
	# derive the center (x, y)-coordinates
	(h, w) = image.shape
	(cX, cY) = (int(w / 2.0), int(h / 2.0))

	# compute the FFT to find the frequency transform, then shift
	# the zero frequency component (i.e., DC component located at
	# the top-left corner) to the center where it will be more
	# easy to analyze
	fft = np.fft.fft2(image)
	fftShift = np.fft.fftshift(fft)

	# check to see if we are visualizing our output
	if vis:
		# compute the magnitude spectrum of the transform
		magnitude = 20 * np.log(np.abs(fftShift))
		# display the original input image
		(fig, ax) = plt.subplots(1, 2, )
		ax[0].imshow(image, cmap="gray")
		ax[0].set_title("Input")
		ax[0].set_xticks([])
		ax[0].set_yticks([])
		# display the magnitude image
		ax[1].imshow(magnitude, cmap="gray")
		ax[1].set_title("Magnitude Spectrum")
		ax[1].set_xticks([])
		ax[1].set_yticks([])
		# show our plots

		plt.plot(magnitude[50])
		plt.show()

	print(fftShift)

	# zero-out the center of the FFT shift (i.e., remove low
	# frequencies), apply the inverse shift such that the DC
	# component once again becomes the top-left, and then apply
	# the inverse FFT
	fftShift[cY - size:cY + size, cX - size:cX + size] = 0
	fftShift = np.fft.ifftshift(fftShift)
	recon = np.fft.ifft2(fftShift)


	print(np.abs(recon).shape)
	# compute the magnitude spectrum of the reconstructed image,
	# then compute the mean of the magnitude values
	magnitude = 20 * np.log(np.abs(recon))
	mean = np.mean(magnitude)
	# the image will be considered "blurry" if the mean value of the
	# magnitudes is less than the threshold value
	
	return (mean, mean <= thresh)


def fft_ifft_image():
	a  = cv2.imread("/home/popikeyshen/circle.jpg",0)
	a  = cv2.imread("/home/popikeyshen/convolution/test_conv.png",1)
	#a = cv2.resize(a, (100,100), interpolation = cv2.INTER_AREA)

	#a = a[50:52]

	sp = np.fft.fft2(a)

	fftShift = np.fft.fftshift(sp)

	#fftShift[:45,:45]=0
	#fftShift[:45,55:]=0
	#fftShift[55:,:45]=0
	#fftShift[55:,55:]=0  # center 

	fftShift[:6,:6]=0
	fftShift[:6,14:]=0
	fftShift[14:,:6]=0
	fftShift[14:,14:]=0  # center 

	#fftShift[45:55]=0    # contours
	#fftShift[:,45:55]=0


	#fftShift *=2  # amplitude
	print(fftShift)

	magnitude = (np.abs(fftShift))
	plt.imshow(magnitude, cmap="gray")
	#plt.plot(magnitude[50])
	plt.show()

	sp = np.fft.ifftshift(fftShift)

	s = np.fft.ifft2(sp)

	print(sp.shape)

	print("a")
	plt.imshow(a.astype("int32"))
	plt.show()
	print("s")
	plt.imshow( s.astype("int32") )
	plt.show()

	cv2.imshow("res",s.astype("uint8"))
	cv2.waitKey(0)




