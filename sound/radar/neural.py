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
RECORD_SECONDS = 4
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

k=1.1
plt.plot(numpydata_L)
plt.plot(numpydata_R*k)
plt.show()
plt.plot(numpydata_L - numpydata_R*k)
plt.show()



