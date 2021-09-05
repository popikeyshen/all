

file_ = "sound2.aiff"

def read_by_wave():
	import wave
	import numpy

	# Read file to get buffer
	ifile = wave.open("input.wav")
	samples = ifile.getnframes()
	audio = ifile.readframes(samples)

	# Convert buffer to float32 using NumPy
	audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)
	audio_as_np_float32 = audio_as_np_int16.astype(numpy.float32)

	# Normalise float32 array so that values are between -1.0 and +1.0
	max_int16 = 2**15
	audio_normalised = audio_as_np_float32 / max_int16


### open by scipy
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

def read_by_scipy(file_):
	
	a = read(file_)
	s = np.array(a[1],dtype=float)
	#print(s.shape)

	#s = s.transpose(1,0)

	plt.plot(s)
	plt.show()

	return s




### 1. read wav files
wav1 = read_by_scipy("sound.wav")
wav2 = read_by_scipy("sound2.aiff")



w1 = wav1.transpose(1,0)[0]
w2 = wav2.transpose(1,0)[0]


w1 = w1[:157000]
w2 = w2[:157000]
print(w1.shape,w2.shape)


#result = np.convolve(w1, w1)
#print("reslt.shape", result.shape)
#l, = result.shape
#print("center=",l/2)
#l=int(l/2)
#result[l]=10**10
#plt.plot(result)
#plt.show()

from scipy import signal
result = signal.correlate(w1, w1, mode='full', method='auto')
l, = result.shape
print("center=",l/2)
l=int(l/2)
result[l]=10**10
plt.plot(result)
plt.show()


