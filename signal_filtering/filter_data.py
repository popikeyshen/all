import numpy as np
import cv2
from matplotlib import pyplot as plt




def fft_filtering(vector, vis=True):


	print(vector.shape)
	size = int( 276/2 )

	# compute the FFT to find the frequency transform, then shift
	# the zero frequency component (i.e., DC component located at
	# the top-left corner) to the center where it will be more
	# easy to analyze
	fft = np.fft.fft(vector)
	fftShift = np.fft.fftshift(fft)

	# check to see if we are visualizing our output
	if vis:
		# compute the magnitude spectrum of the transform
		magnitude = 20 * np.log(np.abs(fftShift))
		# display the original input vector
		(fig, ax) = plt.subplots(1, 2, )
		ax[0].plot(vector)
		ax[0].set_title("Input")
		ax[0].set_xticks([])
		ax[0].set_yticks([])
		# display the magnitude vector
		ax[1].plot(magnitude)
		ax[1].set_title("Magnitude Spectrum")
		ax[1].set_xticks([])
		ax[1].set_yticks([])
		# show our plots


		plt.show()

	print(fftShift.shape)

	# zero-out the center of the FFT shift (i.e., remove low
	# frequencies), apply the inverse shift such that the DC
	# component once again becomes the top-left, and then apply
	# the inverse FFT

	#fftShift[50:size-50] = 0

	fftShift[:2] 		= 0
	fftShift[size-2:]	= 0

	fftShift = np.fft.ifftshift(fftShift)
	recon = np.fft.ifft(fftShift)

	res = vector - recon


	if vis:

		# display the original input vector
		(fig, ax) = plt.subplots(1, 2, )
		ax[0].plot(np.real(res))
		ax[0].set_title("filtered signal")
		ax[0].set_xticks([])
		ax[0].set_yticks([])
		# display the magnitude vector
		ax[1].plot(np.real(recon))
		ax[1].set_title("high frequency")
		ax[1].set_xticks([])
		ax[1].set_yticks([])
		# show our plots


		plt.show()


	#print(np.abs(recon).shape)
	# compute the magnitude spectrum of the reconstructed vector,
	# then compute the mean of the magnitude values
	magnitude = 20 * np.log(np.abs(recon))
	mean = np.mean(magnitude)
	print("high frequency mean", mean)


def SMA(vector):
	l, = vector.shape
	#print(l)

	window =40
	sma = []
	for i in range(l-window):
		v = vector[i:i+window]
		v = np.average(v)
		sma.append(v)
	


	(fig, ax) = plt.subplots(1, 2, )
	ax[0].plot(vector)
	ax[0].set_title("signal")
	ax[1].plot(sma)
	ax[1].set_title("SMA filtered, window = 20")
	plt.show()

def sinc_filter(vector, size=80):
	## create sinc window
	x = np.linspace(-4, 4, size)
	win = np.sinc(x)/ (size/8.7)

	## process
	res = np.convolve(vector, win)

	## padding
	l = len(res)
	res = res[int(size/2):l-int(size/2)]

	## visualize
	plt.plot(vector)
	plt.show()
	plt.plot(res)
	plt.show()


from scipy import ndimage, misc
def median_filter(vector, size=80):
	res = ndimage.median_filter(vector, size=size)

	plt.plot(vector)
	plt.show()
	plt.plot(res)
	plt.show()

if __name__ == "__main__":

	#with open('signal.npy', 'wb') as f:
	#	np.save(f, data_vector)

	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)


	#fft_filtering(data_vector)
	#SMA(data_vector)
	#sinc_filter(data_vector)
	median_filter(data_vector)

