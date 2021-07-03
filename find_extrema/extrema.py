import numpy as np


def create_function():
	x = np.linspace(0, 4*np.pi, 200)
	sin1 = np.sin(3*x)
	sin2 = np.sin(2*x)
	signal =  sin1 + sin2
	return signal



if __name__ == "__main__":
	
