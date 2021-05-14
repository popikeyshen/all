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

#fft_ifft()

def decompose_fft(data: list, threshold: float = 0.0):
    fft3 = np.fft.fft(data)
    x = np.arange(0, 10, 10 / len(data))
    freqs = np.fft.fftfreq(len(x), .01)
    recomb = np.zeros((len(x),))
    for i in range(len(fft3)):
        if abs(fft3[i]) / len(x) > threshold:
            sinewave = (
                1 
                / len(x) 
                * (
                    fft3[i].real 
                    * np.cos(freqs[i] * 2 * np.pi * x) 
                    - fft3[i].imag 
                    * np.sin(freqs[i] * 2 * np.pi * x)))
            recomb += sinewave
            plt.plot(x, sinewave)
    plt.show()

    plt.plot(x, recomb, x, data)
    plt.show()


x = np.arange(0, 10, 0.01)
x2 = np.arange(0, 20, 0.02)
sin1 = np.sin(x)
sin2 = np.sin(x2)
x2 /= 2
sin3 = sin1 + sin2

import numpy as np
fft3 = np.fft.fft(sin3)

plt.plot(fft3)
plt.show()

# https://stackoverflow.com/questions/59725933/plot-fft-as-a-set-of-sine-waves-in-python
# custom
def c1(x):
	freqs = np.fft.fftfreq(len(x),.01)
	threshold = 0.0
	recomb = np.zeros((len(x),))
	for i in range(len(fft3)):
		if abs(fft3[i])/(len(x)) > threshold:
			recomb += 1/(len(x))*(fft3[i].real*np.cos(freqs[i]*2*np.pi*x)-fft3[i].imag*np.sin(freqs[i]*2*np.pi*x))
			plt.plot(x,1/(len(x))*(fft3[i].real*np.cos(freqs[i]*2*np.pi*x)-fft3[i].imag*np.sin(freqs[i]*2*np.pi*x)))

	plt.show()

	plt.plot(x,recomb,x,sin3)
	plt.show()

x = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
c1(x)



