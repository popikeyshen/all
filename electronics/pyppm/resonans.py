import numpy as np

### calculate resonans frequencies for H

#http://chem.spbu.ru/files/Vladimir/Vasiliev/NMR_1.pdf

## hyromagnetic constant
y = 2.674*10**8

B2 =  0.1         # N35	
B1 = 30*10**(-6)  # normal earth magnetic field

## energy
#E = B*h/(4*pi) 

## frequency
v = y*B2/(2*np.pi)

print(v)


'''
1276 Hz  for 30 uTl
4.2  Mhz for N35

'''
