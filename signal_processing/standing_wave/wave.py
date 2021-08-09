import numpy as np
from matplotlib import pyplot as plt


def decompose(fft3):

	#for i in range(1,81):
	#  plt.plot(np.sin(i*x)/81)
	#plt.show()
	x = np.linspace(0, 4*np.pi, 200)
	r= fft3[0] * np.sin(0*x)/29
	for i in range(1,29):
		s = fft3[i] * np.sin(i*x)/29
		plt.plot(s)
		r += s
           
		plt.plot(r)
		plt.show()
	plt.plot(r)
	#  print(abs(fft3[i]),i)
	#plt.savefig('components.png')
	plt.show()

def wave1():
	# signal that we wanna become
	res = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
	res2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
	res3 = np.array([0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,3,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0])
	plt.plot(res3)
	plt.show()

	fft = np.fft.fft(res3)
	plt.plot(np.fft.fftshift(fft))  # with frequency shift to center
	plt.show()

	decompose(fft)

	print(fft)


	### to have 10 cm area 
	### we need f = c/l (l = c/f)
	### f = c/l = 3*10^8/0.1 = 3*10^7 Hz = 30 MHz signal f1 to become 5     cm hight voltage area
	###                                    60 MHz signal f2 to become 2.5   cm hight voltage area
	###                                   120 MHz signal f3 to become 1.25  cm hight voltage area
	f = 30 
	l = 5
	for i in range(10):
		f = f*2
		l = l/2
		print(f, " \tMHz signal f1 to become", l ," \tcm hight voltage area")

import cv2
def wave2():
	signal = np.array([0,0,0,5,4,3,2,1,0,0,0])
	signal = (np.diff(signal)+10).astype(np.uint8)*10

	plt.plot(signal)  # with frequency shift to center
	plt.show()



	for loops in range(100):

		for shift in range(0,10):

			arr = np.zeros((40,40),np.uint8)
			for i in range(0,30,10):
				arr[20,i+shift+1:i+10+shift+1] += signal
				arr[i+shift:i+10+shift,20] += signal

			#plt.imshow(arr)
			#plt.show()

			arr = cv2.resize(arr,(300,300))
			cv2.imshow("arr",arr)
			cv2.waitKey(100)


def wave3():

	x = np.linspace(0, 4*np.pi, 200)
	phi = 0

	for t in range(0,100):
		t = t/5
		phi +=0.1
			
		s1 =  np.sin(x+t)	
		s2 =  np.sin(x+t+phi)
		res = s1+s2

		plt.plot(s1)
		plt.plot(s2)
		plt.plot(res)
		plt.show()	


if __name__ == '__main__':
	#wave1()
	#wave2()
	wave3()


