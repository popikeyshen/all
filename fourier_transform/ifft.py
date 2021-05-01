import cv2
from matplotlib import pyplot as plt
import numpy as np

def fft_ifft():
	a1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	a = np.array(a1)

	sp = np.fft.fft(a)

	print(sp, sp.shape,a.shape)

	#sp = [0,1+1j,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	s = np.fft.ifft(sp)

	#plt.plot(a)
	#plt.show()
	plt.plot(s)
	plt.show()

fft_ifft()
