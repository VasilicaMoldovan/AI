# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:04:07 2020

@author: Vasilica
"""
import numpy as np
import decimal

class ArtificialNeuralNetwork:
    def __init__(self, x, y, hidden):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],hidden) 
        self.weights2   = np.random.rand(hidden,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self.loss       = []
    
    def sigmoid(self, x):
        return 1.0/(1+ np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1.0 - x)
    
    def feedforward(self):
        self.layer1 = self.sigmoid(np.dot(self.input, self.weights1))
        #print(len(self.layer1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))
        
    def backpropagation(self,l_rate):
         d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) *
                            self.sigmoid_derivative(self.output)))
           
         d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y -
                            self.output) * self.sigmoid_derivative(self.output),
                            self.weights2.T) *
                             self.sigmoid_derivative(self.layer1)))
           
         self.weights1 += l_rate * d_weights1
         self.weights2 += l_rate * d_weights2
         self.loss.append(sum((self.y - self.output)**2))
         
    
         
         
         