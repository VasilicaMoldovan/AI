# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:19:10 2020

@author: Vasilica
"""
import tensorflow as tf

class Problem:
    def __init__(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = tf.keras.datasets.mnist.load_data()
        
    def getTrainImages(self):
        return self.x_train
    
    def getTrainLabels(self):
        return self.y_train
    
    def getTestImages(self):
        return self.x_test
    
    def getTestLabels(self):
        return self.y_test
    