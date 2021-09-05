import pyaudio
import wave

# sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
# sudo apt install audacity

import numpy as np
import matplotlib.pyplot as plt


CHUNK = 10240
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    #frames.append(data)

    numpydata = np.frombuffer(data, dtype=np.int16)
    print(numpydata.shape)
    plt.plot(numpydata)
    plt.show()

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


