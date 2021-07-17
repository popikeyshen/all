import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



def signal1():
	#Generate a test signal, a 2 Vrms sine wave at 1234 Hz, corrupted by 0.001 V**2/Hz of white noise sampled at 10 kHz.
	rng = np.random.default_rng()
	fs = 10e3
	N = 1e5
	amp = 2*np.sqrt(2)
	freq = 1234.0
	noise_power = 0.001 * fs / 2
	time = np.arange(N) / fs
	x = amp*np.sin(2*np.pi*freq*time)
	x += rng.normal(scale=np.sqrt(noise_power), size=time.shape)

	plt.plot(x)
	plt.show()

	return x

def signal2():
	data_vector = 0
	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)

	plt.plot(data_vector)
	plt.show()

	return data_vector


def welch(x):
	fs = 10e3
	#Compute and plot the power spectral density.
	f, Pxx_den = signal.welch(x, fs, nperseg=1024)
	plt.semilogy(f, Pxx_den)
	plt.xlabel('frequency [Hz]')
	plt.ylabel('PSD [V**2/Hz]')
	plt.show()

if __name__ == "__main__":

	s = signal2()
	welch(s)


