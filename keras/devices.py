

import tensorflow as tf
devices = tf.config.list_physical_devices("GPU") 
print(devices)

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
