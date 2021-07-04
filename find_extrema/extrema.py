import numpy as np
import matplotlib.pyplot as plt

def create_function1():

	x = np.linspace(0, 2*np.pi, 1000)
	sin1 = np.sin(3*x)
	sin2 = np.sin(2*x)
	signal =  sin1 + sin2 + 3
	return signal

# https://www.keldysh.ru/pages/comma/html/nonlinear/extremum.html
def create_function2():
	#f(x)=x4+5x3-10x
	
	x = np.linspace(-1000, 1000, 2000)
	f = x**4+5*x**3-10*x
	return f

### blurred to see just global extrema
def test1(s):
	### test 1
	### for find only global maximums we use gaussian blur

	## blurred
	b1 = gaussian_filter(s, sigma=50)  
	b2 = gaussian_filter(s, sigma=25) 
	b3 = gaussian_filter(s, sigma=12) 
	plt.plot(b1)
	plt.plot(b2)
	plt.plot(b3)
	plt.show()


	d0 = np.gradient(s)
	d1 = np.gradient(b1)
	d2 = np.gradient(b2)
	#d3 = np.gradient(b3)

	dd0 = np.gradient(d0)
	dd1 = np.gradient(d1)
	dd2 = np.gradient(d2)

	plt.plot(s-3)
	plt.plot(dd1*1000)
	#plt.plot(dd2)

	#plt.plot(d1*20)
	#plt.plot(d2*20)
	#plt.plot(d3*20)

	null = np.linspace(0, 0, 100)
	plt.plot(null )
	plt.show()

	### result:
	### за домопогою техніки блюру ми можемо не тільки скрити локальні мінімуми але і змінити місце глобального максимуму, тому техніка блюру може використовуватись для такої задачі дуже обмежено.

## find all extrema fith derivative
def test2(s):
	#s[0]=0
	#s[-1]=0


	
	### gradient to find extrema
	d0 = np.gradient(s)
	dd = np.gradient(d0)
	plt.plot(d0*10)
	#plt.plot(dd*10)


	#d0 = np.diff(s,  n=1)
	#dd = np.diff(d0, n=1)
	### https://numpy.org/doc/stable/reference/generated/numpy.diff.html
	#d0 = np.diff(s)
	#plt.plot(d0)


	## accumulated to restore gradient
	# https://numpy.org/doc/stable/reference/ufuncs.html
	#accumulated1 = np.add.accumulate(d0)
	#accumulated2 = np.add.accumulate(accumulated1/100)
	#plt.plot(accumulated1)
	#plt.plot(accumulated2)

	### get extrema points
	cp = []
	for i in range(len(s)):
		if ( d0[i]<0 != d0[i]<=0  ):
			cp.append(10)
		else:
			cp.append(0)
	cp = np.gradient(cp)

	null = np.linspace(0, 0, 100)
	plt.plot(null )
	plt.plot(s)
	plt.plot(cp)
	plt.show()

def create_function3():
	#with open('signal.npy', 'wb') as f:
	#	np.save(f, data_vector)

	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)

	return data_vector


from scipy.ndimage.filters import gaussian_filter
if __name__ == "__main__":
	### get signal
	s = create_function1()
	#s = create_function3()

	### get extrema points after blur
	#test1(s)

	### get all extrema points
	test2(s)


	
