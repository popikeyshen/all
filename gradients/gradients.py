
import matplotlib.pyplot as plt
import numpy as np
import cv2



def _1Dgradient():
	x = np.linspace(0, 4*np.pi, 200)
	sin1 = np.sin(x)

	grad1 = np.gradient(sin1*5)  
	grad2 = np.gradient(grad1*5)*-1
	### normal gradient and second gradient of sin 

	plt.plot(sin1,'r-')
	plt.plot(grad1,'g-')
	plt.plot(grad2,'g--')
	#plt.savefig('Sin.png')
	plt.show()


	x = np.linspace(0, 4*np.pi, 200)
	sin1 = np.sin(x)

	grad1 = np.gradient(sin1*5)  
	grad2 = np.gradient(grad1*5)*-1
	### normal gradient and second gradient of sin 


	x = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

	grad1 = np.gradient(x)  
	grad2 = np.gradient(grad1*2)*-1

	plt.plot(x,'r-')
	plt.plot(grad1,'g-')
	plt.plot(grad2,'g--')
	#plt.savefig('rec.png')
	plt.show()




def _2Dgradient():
	img = cv2.imread("rec3.png")
	img = cv2.resize(img,(200,200),)
	#img = img.astype('int')

	gradx,grady,gradz = np.gradient(img)  

	cv2.imshow("dx",gradx)
	cv2.imshow("dy",grady)
	cv2.imshow("dz",gradz)
	#cv2.imwrite("dx.jpg",gradx*5)
	#cv2.imwrite("dy.jpg",grady*5)
	#cv2.imwrite("dz.jpg",gradz*5)
	cv2.waitKey(0)

	plt.imshow(gradx)
	#plt.savefig('gradx2d.png')
	plt.show()

	plt.imshow(grady)
	#plt.savefig('grady2d.png')
	plt.show()

	plt.imshow(gradz)
	#plt.savefig('gradz2d.png')
	plt.show()

from scipy import ndimage, misc
def _1Dlaplacian():

	x = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
	x = np.asarray(x)
	gradient  = ndimage.laplace(x)
	gradient2 = ndimage.laplace(gradient)

	plt.plot(x,'r-')
	plt.plot(gradient, 'g-')
	#plt.plot(gradient2,'g--')
	#plt.savefig('1Dlaplace.png')
	plt.show()

from scipy import signal
def _1DlaplaceKernel():
	x = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
	x = np.asarray(x)

	kernel = np.array( [ -1, 2, -1] )
	#kernel = np.array( [ -1,-1, 2, 2,-1,-1] )
	gradient = signal.convolve(x, kernel, mode='same')
	#gradient = np.convolve(x, kernel)

	plt.plot(x,'r-')
	plt.plot(gradient, 'g-')
	plt.show()

#def _2Dlaplacian():

# maybe useful links
# http://www.cs.cmu.edu/~16385/s17/Slides/4.0_Image_Gradients_and_Gradient_Filtering.pdf


_1Dgradient()
_2Dgradient()
_1Dlaplacian()
_1DlaplaceKernel()



