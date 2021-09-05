import pyaudio
import numpy  as np
import cv2



def show(k):
	cap = cv2.VideoCapture(0)

	#while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	w,h,c = frame.shape
	print(w,h,c)

	y=int(470)
	x=int(640*k)

	# Start coordinate, here (100, 50) 
	# represents the top left corner of rectangle 
	start_point = (x, 10) 
	   
	# Ending coordinate, here (125, 80) 
	# represents the bottom right corner of rectangle 
	end_point = (x+10, y) 
	   
	# Black color in BGR 
	color = (0, 0, 255) 
	   
	# Line thickness of -1 px 
	# Thickness of -1 will fill the entire shape 
	thickness = 2
	frame = cv2.rectangle(frame, start_point, end_point, color, thickness) 

	cv2.imshow("", frame)
	cv2.waitKey(0)

RATE= 128000
RECORD_SECONDS = 2
CHUNKSIZE = 1024

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=2, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

frames_L = [] # A python-list of chunks(numpy.ndarray)
frames_R = []

for _ in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)

    frame = np.frombuffer(data, dtype=np.int16)       # interleaved channels
    frame = np.stack((frame[::2], frame[1::2]), axis=0)  # channels on separate axes
    print(frame.shape)

    frames_L.append(frame[0])
    frames_R.append(frame[1])

#Convert the list of numpy-arrays into a 1D array (column-wise)
numpydata_L = np.hstack(frames_L)
numpydata_R = np.hstack(frames_R)

# close stream
stream.stop_stream()
stream.close()
p.terminate()

import matplotlib.pyplot as plt
plt.plot(numpydata_L)
plt.plot(numpydata_R)
plt.show()

plt.plot(numpydata_R-numpydata_L)
plt.show()

L = np.argmax(numpydata_L)
R = np.argmax(numpydata_R)
print(R,L, R-L)

numpydata_L = numpydata_L[L-50:L+50]+100000
numpydata_R = numpydata_R[L-50:L+50]+100000

print("conv")




conv = np.convolve(numpydata_L, numpydata_R)
#plt.plot(conv)
#plt.show()

import scipy.io.wavfile as wav
wav.write('out_L.wav',RATE,numpydata_L)
wav.write('out_R.wav',RATE,numpydata_R)

import matplotlib.pyplot as plt
plt.plot(numpydata_L)
plt.plot(numpydata_R)
plt.show()



def get_phase(numpydata_L,numpydata_R):
	
	# find center
	mi = np.min(numpydata_L)
	ma = np.max(numpydata_L)
	ce = (ma+mi)/2
	print("center = ",ce)

	#loop over massive and calc len of + part of sin
	points=0
	accumulated = []
	for i in numpydata_L:
		if i > ce:
			points +=1
		else:
			accumulated.append(points)
			points = 0

	accu2 = []
	for a in accumulated:
		if a>0:
			accu2.append(a)
	print(accu2)
	avg = np.mean(accu2)
	print(avg)


	time_d1=[]
	time_d2=[]
	## time difference
	for i in range(len(numpydata_L)-1):

		if numpydata_L[i]>ce and numpydata_L[+1]<ce:
			time_d1.append(i)

	for i in range(len(numpydata_R)-1):

		if numpydata_R[i]>ce and numpydata_R[+1]<ce:
			time_d2.append(i)

	print("d1 ",time_d1)
	print("d2 ",time_d2)
	dif =0
	for i in range(5):
		dif += time_d1[i]-time_d2[i]
	print("dif = ",dif)

	show(1-dif/40)



get_phase(numpydata_L,numpydata_R)


#from scipy import signal
#result = signal.correlate(numpydata_L, numpydata_R)
#print("corelate",result.argmax())


#l, = result.shape
#print("center=",l/2)
#l=int(l/2)
#result[l]=10**10
#plt.plot(result)
#plt.show()
