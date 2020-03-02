from darkflow.net.build import TFNet
import cv2
import tensorflow as tf
        

config = tf.ConfigProto(log_device_placement = False)
config.gpu_options.allow_growth = False 

with tf.Session(config=config) as sess:
    options = {
            'model': '', #See Readme
            'load': '', #See Readme
            'threshold': 0.25, 
            'gpu': 1.0
               }
    tfnet = TFNet(options)    
