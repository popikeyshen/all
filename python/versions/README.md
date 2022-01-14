
## Multiple python versions 

### Links
https://towardsdatascience.com/installing-multiple-alternative-versions-of-python-on-ubuntu-20-04-237be5177474
https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

### Cases
If installing multiple versions of python with git and make - it can crash the enviroment
To restore the system - remake last working version and install

Good is to install version's with ppa:deadsnakes

```
sudo apt-get install software-properties-common# adding python repository 
sudo add-apt-repository ppa:deadsnakes/ppasudo apt update# install python 3.7
sudo apt install python3.7
```

And Update alternatives with
```
sudo update-alternatives --config python#select the number of python you want then enterpython --version
```
With adding new versions with 
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
```

After you can install virtualenv with
```
sudo pip3 install virtualenv
```
