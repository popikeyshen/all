import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

img= cv2.imread('cat.jpg') 
labimg = img.copy()#cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

n = 0
#while(n<2):
#   labimg = cv2.pyrDown(labimg)  # same size but low resolution
#    n = n+1  

feature_image=np.reshape(labimg, [-1, 3])
rows, cols, chs = labimg.shape

# eps if lower = more clusters
db = DBSCAN(eps=10, min_samples=50, metric = 'euclidean',algorithm ='auto')
db.fit(feature_image)
labels = db.labels_

print(feature_image,labels.shape)

indices = np.dstack(np.indices(labimg.shape[:2]))
xycolors = np.concatenate((labimg, indices), axis=-1) 
feature_image2 = np.reshape(xycolors, [-1,5])
db.fit(feature_image2)
labels2 = db.labels_

print(labels2.shape)

L = labels
U = np.unique(L)
for u in U:   # run over cluster and get colors mean
	mean = np.mean( feature_image[L==u], axis=0 )
	feature_image[L==u] = mean

img = np.reshape(feature_image, (labimg.shape))

cv2.imshow("img",img)
cv2.waitKey(0)
