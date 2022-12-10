import numpy as np

### calculate resonans frequencies for H

#http://chem.spbu.ru/files/Vladimir/Vasiliev/NMR_1.pdf

## hyromagnetic constant for H^1
y = 2.674*10**8

B2 =  0.1         # N35	

# 30-60 uT normal earth magnetic field
B1 = 52*10**(-6)  # normal Kyiv earth magnetic field



## energy
#E = B*h/(4*pi) 

## frequency
v = y*B1/(2*np.pi)

print(v)


'''
1276 Hz  for 30 uT
2213 Hz  for 52 uT
4.2  Mhz for N35

'''

### for paper  https://www.bu.edu/chemistry/files/cic/nmr/documents/CICNMR_basicconcepts.pdf
### inova 500 has 500 mhz frequency for H1
### cause the B = 500 000 000 *4*pi / y
B = 500000000 *2*np.pi / y
print(B, 'T')  ## 11.74
## 8 μs to rotate 90º

## The 500 MHz magnet system comprises a fully persistent 11.74 Tesla high
## http://www.ietltd.com/pdf_datasheets/Unshielded%20Inova%20500%20Data%20Sheet.pdf
## 11.74 ÷ 0.000430 = 27 302
## 8u * 27 302 = 0.218416s for a 90^ impulse

