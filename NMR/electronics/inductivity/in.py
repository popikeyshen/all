import numpy as np

### magnetic constant
u = 4*np.pi*10**(-7)

### magnetic induction (Tesla)
### n = N/l
### I*n - amper-turns

I = 600#A
n = 1000
B = u*I*n

print(B)  # 0.75 Tl
