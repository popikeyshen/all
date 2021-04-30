
from sklearn.cluster import MeanShift
import numpy as np
import cv2

# the complexity is omg -  will tend towards O(T*n*log(n)) in lower dimensions, with n the number of samples and T the number of points.

img = cv2.imread('./cat.jpg')
img = cv2.resize(img,(300,210))
Z = img.reshape((-1,3))


clustering = MeanShift(bandwidth=20, n_jobs=8).fit(Z)
print(clustering.labels_,clustering.labels_.shape)

L = clustering.labels_
U = np.unique(L)
for u in U:   # run over cluster and get colors mean
	mean = np.mean( Z[L==u], axis=0 )
	Z[L==u] = mean


res2 = Z.reshape((210,300,3))

cv2.imwrite("./cat_mean_shift.png",res2)
cv2.imwrite("./cat_orig.png",img)

cv2.imshow("res2",res2)
cv2.waitKey(0)
