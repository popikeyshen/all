import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 5.0   # in seconds, may be float
line = np.arange(fs*duration)



f1 = 132.0        # sine frequency, Hz, may be float
s1 = np.sin(2*np.pi*line*f1/fs)

f2 = 250.0      
s2 = np.sin(2*np.pi*line*f2/fs)*0.5

f3 = 445.0      
s3 = np.sin(2*np.pi*line*f3/fs)*0.5

f4 = 585.0      
s4 = np.sin(2*np.pi*line*f4/fs)*0.5

f = 700.0      
s5 = np.sin(2*np.pi*line*f/fs)*0.5

f = 800.0      
s6 = np.sin(2*np.pi*line*f/fs)*0.5

f = f  + 90    
s7 = np.sin(2*np.pi*line*f/fs)*0.5

f = f  + 80  
s8 = np.sin(2*np.pi*line*f/fs)*0.5

f = f  + 70  
s9 = np.sin(2*np.pi*line*f/fs)*0.5

f = f  + 60  
s9 = np.sin(2*np.pi*line*f/fs)*0.5

f = f  + 50  
s10 = np.sin(2*np.pi*line*f/fs)*0.5

#f2 = 300.0      
#s2 = np.sin(2*np.pi*line*f/fs)*0.9

sound = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10



# generate samples, note conversion to float32 array
samples = (sound).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
