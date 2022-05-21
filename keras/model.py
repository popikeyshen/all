from tensorflow.keras.layers.experimental import RandomFourierFeatures
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.utils import to_categorical  
from tensorflow.keras.regularizers import l2

from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.activations import sigmoid
	
from tensorflow.keras import Sequential
import tensorflow as tf

def get_keras_net(X,y):
	n_features = 10


	with tf.device("/GPU:0"):



		model = Sequential()
		model.add(Dense(n_features))
		model.add(Activation(sigmoid))
		model.add(Dense(1))
		model.add(Activation(sigmoid))

		model.compile(loss='MSE',
		              optimizer='adam',
		              metrics=['accuracy'])



		#y = y[:,0,:]      
		#with tf.device("/GPU:0"):
		#print(X.shape,y.shape,'one hot X')

		t = time.time()
		model.fit(X, y, epochs=10000, batch_size=10000,verbose=1) #   , sample_weight=weight
		print('train no cuda',time.time()-t)
			
		return model

from tensorflow import keras
def run_model():
	with tf.device('/GPU:0'):		
		model = keras.models.load_model('/home/popikeyshen/da_popika_prod/keras_water_msva_noNorm_timeline3-10.h5')
		model.summary()
		print(model.summary())
					
		#vec = tf.constant(vec)
			
		# https://stackoverflow.com/questions/48796619/why-is-tf-keras-inference-way-slower-than-numpy-operations
		res2 = model.predict(vec, batch_size=10000)  ## wtf


