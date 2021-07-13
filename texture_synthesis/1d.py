

import numpy as np
from matplotlib import pyplot as plt 

tx1= np.array([ 0,1,2,3,4,5,4,3,2,1,0])
tx2= np.array([ 0,1,0,1,0,1,0,1,0,1,0])

tx3 = tx1*tx2
tx4 = tx1+tx2


fig = plt.figure()
plt.title("signals")
plt.plot(tx1)
plt.plot(tx2)


fig = plt.figure()
plt.title("tx1+tx2, tx1*tx2")
plt.plot(tx3)
plt.plot(tx4)


plt.show()
