
import cv2
import numpy as np
import matplotlib.pyplot as plt




# ffttools
def fftd(img, backwards=False):	
	# shape of img can be (m,n), (m,n,1) or (m,n,2)	
	# in my test, fft provided by numpy and scipy are slower than cv2.dft
	return cv2.dft(np.float32(img), flags = ((cv2.DFT_INVERSE | cv2.DFT_SCALE) if backwards else cv2.DFT_COMPLEX_OUTPUT))   # 'flags =' is necessary!

def createGaussianPeak( sizey, sizex):
		padding = 2.5
		output_sigma_factor = 0.125

		syh, sxh = sizey/2, sizex/2
		output_sigma = np.sqrt(sizex*sizey) / padding * output_sigma_factor
		mult = -0.5 / (output_sigma*output_sigma)
		y, x = np.ogrid[0:sizey, 0:sizex]
		y, x = (y-syh)**2, (x-sxh)**2
		res = np.exp(mult * (y+x))
		#plt.imshow(res)  #gauss
		#plt.show()
		return fftd(res)

def subPixelPeak( left, center, right):
		divisor = 2*center - right - left   #float
		return (0 if abs(divisor)<1e-3 else 0.5*(right-left)/divisor)



def subwindow(img, window, borderType=cv2.BORDER_CONSTANT):
	cutWindow = [x for x in window]
	limit(cutWindow, [0,0,img.shape[1],img.shape[0]])   # modify cutWindow
	assert(cutWindow[2]>0 and cutWindow[3]>0)
	border = getBorder(window, cutWindow)
	res = img[cutWindow[1]:cutWindow[1]+cutWindow[3], cutWindow[0]:cutWindow[0]+cutWindow[2]]

	if(border != [0,0,0,0]):
		res = cv2.copyMakeBorder(res, border[1], border[3], border[0], border[2], borderType)
	return res

def createHanningMats(size):
	w,h = size
	print("hann size",size)
	hann2t, hann1t = np.ogrid[0:w, 0:h]

	hann1t = 0.5 * (1 - np.cos(2*np.pi*hann1t/(w-1)))
	hann2t = 0.5 * (1 - np.cos(2*np.pi*hann2t/(h-1)))
	hann2d = hann2t * hann1t

	hann = hann2d
	hann = hann.astype(np.float32)
	return hann


def getFeatures(image,extracted_roi , scale=1.0):
	
	z = image[extracted_roi[2]:extracted_roi[0], extracted_roi[3]:extracted_roi[1]]  # crop 

	
	#cv2.imshow("z",z)
	#cv2.waitKey(0)
	FeaturesMap = cv2.cvtColor(z, cv2.COLOR_BGR2GRAY)

	FeaturesMap = FeaturesMap.astype(np.float32) / 255.0 - 0.5
	size_patch = [z.shape[0], z.shape[1], 1]

	#plt.imshow(createHanningMats())  # hann
	#plt.show()

	size = (roi[0]-roi[2],roi[1]-roi[3])
	FeaturesMap = FeaturesMap * createHanningMats(size)
	return FeaturesMap

def complexDivision(a, b):
	res = np.zeros(a.shape, a.dtype)
	divisor = 1. / (b[:,:,0]**2 + b[:,:,1]**2)
	
	res[:,:,0] = (a[:,:,0]*b[:,:,0] + a[:,:,1]*b[:,:,1]) * divisor
	res[:,:,1] = (a[:,:,1]*b[:,:,0] + a[:,:,0]*b[:,:,1]) * divisor
	return res

def complexMultiplication(a, b):
	res = np.zeros(a.shape, a.dtype)
	
	res[:,:,0] = a[:,:,0]*b[:,:,0] - a[:,:,1]*b[:,:,1]
	res[:,:,1] = a[:,:,0]*b[:,:,1] + a[:,:,1]*b[:,:,0]
	return res

def gaussianCorrelation( x1, x2):  #?
	c = cv2.mulSpectrums(fftd(x1), fftd(x2), 0, conjB = True)   # 'conjB=' is necessary!
	c = fftd(c, True)
	c = real(c)
	c = rearrange(c)

	#d = (np.sum(x1[:,:,0]*x1[:,:,0]) + np.sum(x2[:,:,0]*x2[:,:,0]) - 2.0*c) / (100*100*0)
	d = (np.sum(x1*x1) + np.sum(x2*x2) - 2.0*c) / (100*100*1)

	sigma = 0.2
	d = d * (d>=0)
	d = np.exp(-d / (sigma*sigma))

	return d

	
def real(img):
	return img[:,:,0]

def rearrange(img):
	return np.fft.fftshift(img, axes=(0,1))
	#assert(img.ndim==2)
	#img_ = np.zeros(img.shape, img.dtype)
	#xh, yh = int(img.shape[1]/2), int(img.shape[0]/2)
	#img_[0:yh,0:xh], img_[yh:img.shape[0],xh:img.shape[1]] = img[yh:img.shape[0],xh:img.shape[1]], img[0:yh,0:xh]
	#img_[0:yh,xh:img.shape[1]], img_[yh:img.shape[0],0:xh] = img[yh:img.shape[0],0:xh], img[0:yh,xh:img.shape[1]]
	#return img_

def detect(z, x, _alphaf):

	print("detect",z.shape, x.shape, _alphaf.shape)

	k = gaussianCorrelation(x, z)
	print("corelation",k.shape)
	res = real(fftd(complexMultiplication(_alphaf, fftd(k)), True))

	print("res",res.shape)
	plt.imshow(res)
	plt.show()

	_, pv, _, pi = cv2.minMaxLoc(res)   # pv:float  pi:tuple of int
	p = [float(pi[0]), float(pi[1])]   # cv::Point2f, [x,y]  #[float,float]

	if(pi[0]>0 and pi[0]<res.shape[1]-1):
		p[0] += subPixelPeak(res[pi[1],pi[0]-1], pv, res[pi[1],pi[0]+1])
	if(pi[1]>0 and pi[1]<res.shape[0]-1):
		p[1] += subPixelPeak(res[pi[1]-1,pi[0]], pv, res[pi[1]+1,pi[0]])

	p[0] -= res.shape[1] / 2.
	p[1] -= res.shape[0] / 2.

	return p, pv



image = cv2.imread("/home/popikeyshen/faces.jpg")
#b = cv2.imread("/home/popikeyshen/face.jpg")

h,w,c = image.shape
print(h,w,c)


### init
roi = [300,250,200,150]
cv2.rectangle(image,(roi[3],roi[2]), (roi[1],roi[0]), (0,255,255), 1)
cv2.imshow("image1",image)
cv2.waitKey(0)


_tmpl   = getFeatures(image,roi)
_prob   = createGaussianPeak(100, 100)
_alphaf = np.zeros((100, 100, 2), np.float32)

#def train( x, train_interp_factor, _prob, _tmpl):
lambdar = 0.0001   # regularization
k = gaussianCorrelation(_tmpl, _tmpl)
alphaf = complexDivision(_prob, fftd(k)+lambdar)

x = _tmpl 
train_interp_factor=1
_tmpl = (1-train_interp_factor)*_tmpl + train_interp_factor*x
_alphaf = (1-train_interp_factor)*_alphaf + train_interp_factor*alphaf



image = cv2.imread("/home/popikeyshen/faces.jpg")
### update 

### conv
#for y in range(0,50):
y=0
for x in range(0,50):
		roi = [roi[0]+y*10,roi[1]+x*10,roi[2]+y*10,roi[3]+x*10]

		im = image.copy()
		cv2.rectangle(im,(roi[3],roi[2]), (roi[1],roi[0]), (0,255,255), 1)
		cv2.imshow("image1",im)
		cv2.waitKey(1)

		loc, peak_value = detect(_tmpl, getFeatures(image,roi), _alphaf)


print(loc, peak_value)

_scale=1
cell_size=100

cx = roi[0] + roi[2]/2.
cy = roi[1] + roi[3]/2.
print("cxcy", cx, cy)

roi[0] = cx - roi[2]/2.0 + loc[0]*cell_size*_scale
roi[1] = cy - roi[3]/2.0 + loc[1]*cell_size*_scale

boundingbox = list(map(int, roi))
cv2.rectangle(image,(boundingbox[0],boundingbox[1]), (boundingbox[0]+boundingbox[2],boundingbox[1]+boundingbox[3]), (0,255,255), 1)

cv2.imshow("image2",image)
cv2.waitKey(0)



# https://www.programcreek.com/python/example/110719/cv2.mulSpectrums # examples




