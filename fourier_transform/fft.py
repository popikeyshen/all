
import numpy as np
import matplotlib.pyplot as plt

# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.inf)

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


def fft():
	a1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	a = np.array(a1)
	a2 = np.gradient(a)
	a = np.gradient(a2)
	print(a)

	t = np.arange(len(a))
	sp = np.fft.fft(a)
	freq = np.fft.fftfreq(t.shape[-1])
	plt.plot(freq, sp.real, freq, sp.imag)

	t = np.arange(256)
	sp = np.fft.fft(np.sin(t))

	freq = np.fft.fftfreq(t.shape[-1])

	#plt.plot(np.sin(t))
	plt.plot(a2)
	plt.plot(a1)
	plt.plot(a)
	#plt.plot(freq, sp.real, freq, sp.imag)
	plt.show()

import cv2
from matplotlib import pyplot as plt

def grad():
	img = cv2.imread("/home/popikeyshen/textures/1.jpg")
	h,w,c = img.shape

	for hh in range(h):
		for ww in range(w):
			bgr          = img[hh,ww]
			bgr,g	     = distance(bgr)
			img[hh,ww]   = bgr
			gray[hh,ww]  = g
	

def image():
	img  = cv2.imread("/home/popikeyshen/snr1.jpg",0).astype('float32')
	img  = cv2.imread("/home/popikeyshen/convolution/test_conv.png",1)
	img_gradient_x = np.gradient(img)[0]
	img_gradient_y = np.gradient(img)[1]
	#kernel = cv2.imread("/home/popikeyshen/eye.jpg",0).astype('float32')
	#kernel_x = np.gradient(kernel)[0]
	#kernel_y = np.gradient(kernel)[1]
	#kernel_xy = kernel_x+kernel_y

	img_gradient_xy = img_gradient_x+img_gradient_y
	#print(img_gradient0)
	#plt.imshow(img)
	#img_gradient0 = abs(img_gradient0)
	#kernel = abs(kernel)
	plt.imshow(img_gradient_xy)
	plt.show()



	#res = np.convolve(img,img2)  // just 1d 
	res = cv2.filter2D(img_gradient_xy,-1,kernel_xy)

	#res[  res < 40000 ] =0

	#print(img)
	plt.imshow(res)
	plt.show()

	#from scipy import signal
	#cor = signal.correlate2d (img, kernel)
	#print(cor.shape)
	#plt.imshow(cor)
	#plt.show()

	#cv2.imshow("res",res)
	#cv2.waitKey(0)

def fft_ifft():
	a1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	a = np.array(a1)

	sp = np.fft.fft(a)
	s = np.fft.ifft(sp)

	plt.plot(a)
	plt.show()
	plt.plot(s)
	plt.show()

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

def kcf():
	a  = cv2.imread("/home/popikeyshen/snr2.jpg",1)
	b  = cv2.imread("/home/popikeyshen/eye.jpg",1)



image()
#detect_blur_fft()

#fft_ifft()
#fft_ifft_image()

#def full_conv():

#full_conv()

















