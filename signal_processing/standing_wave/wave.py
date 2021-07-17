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
           #plt.plot(s)
           r += s
           
           #plt.show()
	plt.plot(r)
	#  print(abs(fft3[i]),i)
	#plt.savefig('components.png')
	plt.show()

# signal that we wanna become
res = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
res2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.plot(res)
plt.show()

fft = np.fft.fft(res)
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
