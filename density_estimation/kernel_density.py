import numpy as np
import sklearn.neighbors import KernelDensity


# https://scikit-learn.org/stable/modules/density.html
def density(X):
	kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
	kde.score_samples(X)

if __name__ == "__main__":
	data_vector = 0

	#with open('signal.npy', 'wb') as f:
	#	np.save(f, data_vector)

	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)


	density(data_vector)
