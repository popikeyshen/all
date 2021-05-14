# 1d Fourier transform

1d discrete fourier transform looks like 


```signal * M = fft```

Where 

<p align="center"> 
<img src="https://github.com/popikeyshen/all/blob/main/fourier_transform/1d_fft/signal.png" width = 30% /> * <img src="https://github.com/popikeyshen/all/blob/main/fourier_transform/1d_fft/M.png" width = 30% /> = <img src="https://github.com/popikeyshen/all/blob/main/fourier_transform/1d_fft/res.png" width = 30% /> 
</p>

And the components of fft

```
	for i in range(1,200):
	   plt.plot(fft[i] * np.sin(i*x)/200)
```
<p align="center"> 
<img src="https://github.com/popikeyshen/all/blob/main/fourier_transform/1d_fft/components.png" width = 40% />
</p>

