import numpy as np
import matplotlib.pyplot as plt

def create_function1():

	x = np.linspace(0, 2*np.pi, 100)
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


	plt.plot(s-3)
	plt.plot(d0)
	plt.plot(d1*20)
	plt.plot(d2*20)
	#plt.plot(d3*20)
	plt.show()

	### result:
	### за домопогою техніки блюру ми можемо не тільки скрити локальні мінімуми але і змінити місце глобального максимуму, тому техніка блюру може використовуватись для такої задачі дуже обмежено.


from scipy.ndimage.filters import gaussian_filter
if __name__ == "__main__":
	### get signal
	s = create_function1()
	plt.plot(s)

	### get extrema points
	test1(s)


	
