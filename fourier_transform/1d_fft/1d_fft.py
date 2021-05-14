

import numpy as np
import matplotlib.pyplot as plt

def get_signals():
	signal1  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	x = np.linspace(0, 4*np.pi, 200)
	sin1 = np.sin(3*x)
	sin2 = np.sin(2*x)
	signal2 =  sin1 + sin2

	plt.plot(signal2)
	#plt.savefig('signal.png')
	plt.show()

	return signal1,signal2




def decompose(fft3):

	#for i in range(1,81):
	#  plt.plot(np.sin(i*x)/81)
	#plt.show()
	x = np.linspace(0, 4*np.pi, 200)
	for i in range(1,71):
	   plt.plot(fft3[i] * np.sin(i*x)/81)
	#  print(abs(fft3[i]),i)
	#plt.savefig('components.png')
	plt.show()



def numpy_fft(a):
	#a = np.array(a)
	sp = np.fft.fft(a)

	plt.plot(sp)
	plt.show()
	plt.plot(a)
	plt.show()

def DFT_slow(x):
	"""Compute the discrete Fourier Transform of the 1D array x"""
	x = np.asarray(x, dtype=float)
	N = x.shape[0]
	n = np.arange(N)
	k = n.reshape((N, 1))
	print(k,n,N)

	

	M = np.exp( -2j *np.pi * k * n / N)
	res = np.dot(M, x)

	plt.plot(np.fft.fftshift(res))  # with frequency shift to center
	#plt.savefig('res.png')
	plt.show()
	#plt.plot(M.real)
	#plt.plot(M.imag)

	#plt.show()
	#print(M[1])
	#print(M[1].real)
	#print(M[1].imag)
	#print(M.shape)
	#print(x.shape)

	return res



signal1, signal2 = get_signals()
fft3 = np.fft.fft(signal2)
fft3 = DFT_slow(signal2)
decompose(fft3)




