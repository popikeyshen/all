from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

import numpy as np


def dendro(X):

	Z = linkage(X, 'ward')
	fig = plt.figure(figsize=(5, 5))
	dn = dendrogram(Z)
	print(dn)
	print(Z)

	#Z = linkage(X, 'single')
	#fig = plt.figure(figsize=(5, 5))
	#dn = dendrogram(Z)

	#print(Z)

	fig = plt.figure(figsize=(5, 5))
	plt.plot(X)
	plt.show()


def skleanr_hierarchy(X):
	from sklearn.cluster import AgglomerativeClustering
	import numpy as np

	clustering = AgglomerativeClustering(n_clusters=10,linkage='complete').fit(X)
	
	print(clustering.labels_)
	return clustering.labels_


def signal2():
	data_vector = 0
	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)

	#plt.plot(data_vector)
	#plt.show()

	return data_vector

def signal3():
	#img = cv2.imread("saak100.jpg",1)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:,:,:2]
	#img = cv2.medianBlur(img,5)

	print(img.shape)
	x, y = np.meshgrid(range(149), range(82))
	s3 = img.reshape(-1, 3)
	x  =  x.reshape(-1, 1)
	y  =  y.reshape(-1, 1)
	s3 = np.concatenate([s3, x, y], axis=1)
	return s3,img

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

import cv2
if __name__ == "__main__":

	s1 = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0, 1,2,3,10,11]]
	print(s1)
	dendro(s1)

	s2 = signal2()
	s2 = s2.reshape(276, -1)
	s3,img = signal3()

	#from sklearn.cluster import AgglomerativeClustering
	#model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
	#model = model.fit(s2)
	#plt.title('Hierarchical Clustering Dendrogram')
	# plot the top three levels of the dendrogram
	#plot_dendrogram(model, truncate_mode='level', p=3)
	#plt.xlabel("Number of points in node (or index of point if no parenthesis).")
	#plt.show()


	#res = skleanr_hierarchy(s3)
	#plt.plot(res)
	#plt.show()

	#res = res.reshape(82, 149)
	#fig = plt.figure(figsize=(5, 5))
	#plt.imshow(img)
	#fig = plt.figure(figsize=(5, 5))
	#plt.imshow(res)
	#plt.show()
	



