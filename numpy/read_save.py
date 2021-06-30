import numpy as np



if __name__ == "__main__":

	data_vector = np.array([0,0,0,1,2,3,4,5,0,0,0])

	with open('signal.npy', 'wb') as f:
		np.save(f, data_vector)

	with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)
