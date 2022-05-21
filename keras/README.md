 
 
Keras / Tensorflow error:
```
 Could not load dynamic library 'libcudnn.so.8'; 
 dlerror: libcudnn.so.8: cannot open shared object file: 
 No such file or directory; LD_LIBRARY_PATH
```
``` ndivia-smi ``` says i have ```CUDA Version: 11.4```

Because i need to install 

Go to: https://developer.nvidia.com/rdp/cudnn-archive
Find link for cuDNN v8 and CUDA 11.4: ```Download cuDNN v8.2.4 (September 2nd, 2021), for CUDA 11.4```

And try to install same versions of tensofrlow-gpu and keras
```
 sudo pip3 install tensorflow-gpu==2.8.0rc0
 sudo pip3 install keras==2.8.0rc0
```
