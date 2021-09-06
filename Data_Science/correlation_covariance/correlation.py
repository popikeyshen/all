
import numpy as np

def correlate_from_scratch():
	a = [1, 2, 3]
	b = [0, 1, 1]
	c = np.conj(b)	

	k1 = np.array([1, 2, 3, 0, 0]) * np.array([0, 0, 0, 1, 1])
	k2 = np.array([0, 1, 2, 3, 0]) * np.array([0, 0, 0, 1, 1])
	k3 = np.array([0, 0, 1, 2, 3]) * np.array([0, 0, 0, 1, 1])
	k4 = np.array([0, 0, 1, 2, 3]) * np.array([0, 0, 1, 1, 0])
	k5 = np.array([0, 0, 1, 2, 3]) * np.array([0, 1, 1, 0, 0])
	print(k1)
	print(k2)
	print(k3)
	print(k4)
	print(k5)

	res = [ sum(k5), sum(k4), sum(k3), sum(k2), sum(k1) ]
	print(res)

# https://numpy.org/doc/stable/reference/generated/numpy.correlate.html
def correlate_numpy():
	a = [1, 2, 3]
	b = [0, 1, 1]

	res1 = np.correlate(a, b)
	res2 = np.correlate(a, b, "same")
	res3 = np.correlate(a, b, "full")
	print(res1)
	print(res2)
	print(res3)
	#[5]
	#[3 5 3]
	#[1 3 5 3 0]


def correlation_scipy():
	from scipy import signal
	from matplotlib import pyplot as plt

	x   = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	y   = [9, 8, 7, 6, 5, 4, 3, 2, 1]

	corr1 = signal.correlate(x,x)
	corr2 = signal.correlate(x,y)

	plt.plot(corr1)
	plt.plot(corr2)
	plt.show()

	## https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html
	### just for python 3.10
	#res = statistics.correlation( x,x)


def correlation_scipy_example():
	from scipy import signal
	import matplotlib.pyplot as plt
	rng = np.random.default_rng()

	sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
	sig_noise = sig + rng.standard_normal(len(sig))
	corr = signal.correlate(sig_noise, np.ones(128), mode='same') / 128

	clock = np.arange(64, len(sig), 128)
	fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)
	ax_orig.plot(sig)
	ax_orig.plot(clock, sig[clock], 'ro')
	ax_orig.set_title('Original signal')
	ax_noise.plot(sig_noise)
	ax_noise.set_title('Signal with noise')
	ax_corr.plot(corr)
	ax_corr.plot(clock, corr[clock], 'ro')
	ax_corr.axhline(0.5, ls=':')
	ax_corr.set_title('Cross-correlated with rectangular pulse')
	ax_orig.margins(0, 0.1)
	fig.tight_layout()
	plt.show()

	x = np.arange(128) / 128
	sig = np.sin(2 * np.pi * x)
	sig_noise = sig + rng.standard_normal(len(sig))
	corr = signal.correlate(sig_noise, sig)
	lags = signal.correlation_lags(len(sig), len(sig_noise))
	corr /= np.max(corr)

	fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, figsize=(4.8, 4.8))
	ax_orig.plot(sig)
	ax_orig.set_title('Original signal')
	ax_orig.set_xlabel('Sample Number')
	ax_noise.plot(sig_noise)
	ax_noise.set_title('Signal with noise')
	ax_noise.set_xlabel('Sample Number')
	ax_corr.plot(lags, corr)
	ax_corr.set_title('Cross-correlated signal')
	ax_corr.set_xlabel('Lag')
	ax_orig.margins(0, 0.1)
	ax_noise.margins(0, 0.1)
	ax_corr.margins(0, 0.1)
	fig.tight_layout()
	plt.show()




if __name__ == '__main__':
	correlate_from_scratch()
	correlate_numpy()


## links
## https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
## https://youtu.be/qtaqvPAeEJY  ## covariance and correlation




