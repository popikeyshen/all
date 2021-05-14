

import numpy as np
import matplotlib.pyplot as plt





def DPF_v1(x):
	x = np.asarray(x, dtype=float)
	N = x.shape[0]

	### components V1 poloska
	### create components
	c = np.ones(N).astype("int")
	c[N-1]=0
	c[0]=0
	M = np.asarray([c])


	for i in range(N-1):
		c[i]=0
		M=np.append(M,[c],axis=0)


	## show components shape and one component
	#print(M.shape)
	#print(M)
	#plt.plot(M[10])
	#plt.show()

	res = np.dot(M, x)

	#print(res.shape)
	#plt.plot(res.imag)
	#plt.show()
	#print(res)


	for i in range(1,N):
		plt.plot( res[i] * M[i]/N)
	plt.show()


	#for i in range(1,N):
	#	plt.plot(  M[i]/N)
	#	plt.show()


def DPF_v2(x):
	x = np.asarray(x, dtype=float)
	N = x.shape[0]

	### components V2 like sin
	n = np.arange(N)
	k = n.reshape((N, 1))

	M = np.exp(-2j * np.pi * k * n / N)
	Mr = M.real
	Mi = M.imag*1j

	thresh = 0.01
	indices_0 = Mr < thresh
	indices_1 = Mr > thresh
	Mr[indices_0] = 0
	Mr[indices_1] = 1

	thresh = 0.01j
	indices_0 = Mi < thresh
	indices_1 = Mi > thresh
	Mi[indices_0] = 0j
	Mi[indices_1] = 1j

	#print(Mr[5])
	#print(Mi[5])
	M = Mr+Mi

	## show components shape and one component
	#print(M.shape)
	#print(M)
	#plt.plot(M[10])
	#plt.show()

	res = np.dot(M, x)

	#print(res.shape)
	#plt.plot(res)
	#plt.show()

	#print(res.shape)
	plt.plot(res.imag)
	plt.show()
	#print(res)


	for i in range(1,N):
		plt.plot( res[i] * M[i]/N)
	plt.show()

	#for i in range(1,N):
	#	plt.plot(  M[i]/N)
	#	plt.show()



signal1  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x = np.linspace(0, 4*np.pi, 200)
sin1 = np.sin(3*x)
sin2 = np.sin(2*x)
signal2 =  sin1 + sin2

DPF_v1(signal1)
DPF_v2(signal1)
