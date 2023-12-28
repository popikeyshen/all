import numpy as np

def calculate_magnetic_power():   #by coil size and current
	### magnetic constant
	u = 4*np.pi*10**(-7)

	### magnetic induction (Tesla)
	### n = N/l
	### I*n - amper-turns

	I = 600#A
	n = 1000
	B = u*I*n

	print(B)  # 0.75 Tl


# resistance of 10m 1mm cupper cable	
# https://www.geeksforgeeks.org/electrical-resistance-formula/
def resistance(l=10 , radius = 0.001):
	ρ = 1.7 * 10**-8
	radius = 0.001 # 1mm
	A = radius**2
	
	R = (ρ*l)/A
	
	print(A, 'Ωm ', l, 'm ', A, 'm2', A*1000**2, 'mm')
	print(R,'Ω')
	
	return R




# coil size of 10m 1mm cable, 5cm radius 
def coil_size(l=10,r=0.05):
	C = 2*3.14*r

	N = l/C
	print(C, 'm', C*100, 'cm')
	print(N, 'turns')
	
	return N


# inductivity coil of radius 5cm, 10m lenghth
# https://www.geeksforgeeks.org/inductance-formula/	
def inductivity(l=10, r= 0.05):
	print('inductivity')
	μ = 4*3.14 * 10**-7   		# Vacuum permeability
	A = 3.14*r**2			# cros section of ricle
	
	C = 2*3.14*r	
	N = l/C			# number of turns
	
	
	print(μ, 'N/A2', l, 'm', A, 'm2', N, 'n')
	
	L = μ* (N**2) * A / l
	
	print(L, 'H')
	
	
def inductivity_by_freq(frequency=2000, cap= 100*10**(-9)):
	inductance = 1./(4*cap*pow(frequency , 2 )*pow(3.14159 , 2))
	print(inductance, 'H')
	return inductance


# 102 = 1   * 10**(-9)  = 1nf
# 103 = 10  * 10**(-9)  = 10nf
# 104 = 100 * 10**(-9)  = 100nf
def rc_filter(R,C):
	f = 1/(2*np.pi*R*C)
	print(2,np.pi,R,C)
	phase_shift = -np.arctan(2*np.pi*f*R*C)
	print('f=',f)
	print('phase_shift=',phase_shift)
	
#resistance(100)
#coil_size(100)
#inductivity(100)
#inductivity_by_freq()
rc_filter(4700+2200,  10 * 10**(-9)  )   # 4700+2200 Om + 103 = 2300 Hz




### etc
# https://pypi.org/project/MagnetiCalc/   # cuda magnetic field calculator
# mmp-203
# http://artradiolab.com/d.g7.htm # ppm
# http://ilotresor.com/build-a-proton-precession-magnetometer/















