
#     part1   part2
#  E = mc^2 =  hV

# part 1 ###############################

m_e = 9.1*(10**(-31)) # Kg
c   = 3*(10**8)       # m/s

print("mc^2=", m_e*(c**2))  # 8.19e-14 J

# 1ev   = 1.6*10**(-19) J
J_eV = 1.6*10**(-19)

E = 8.19*10**(-14)/J_eV
print("E to eV=",E)
print("MeV=",E/1000)

# E = (pc)^2  + (mc^2)^2


# part 2 ###############################

# proton 2.5 * 10^15
lambda_kompton_e=2.42*10**(-12) # kompton lambda from book
print("lambda_kompton",lambda_kompton_e)
f_kompton = c/lambda_kompton_e   #c/v
print("f_kompton",f_kompton)     # 1.2396694214876034e+20 Hz       123  ExaHz 


# exp 1 - sample rate / 2 = max energy
h2 = 4.135*10**(-15)# EV/s
print("test1",h2/)
