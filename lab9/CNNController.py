# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:48:46 2020

@author: Vasilica
"""
import numpy as np
from Problem import Problem
from Convolutional import Convolutional3x3
from Maxpool import MaxPool
from Softmax import Softmax

class CNNController:
    def __init__(self, problem):
        self.train_images = problem.getTrainImages()[:5000]
        self.train_labels = problem.getTrainLabels()[:5000]
        self.test_images = problem.getTestImages()[:1000]
        self.test_labels = problem.getTestLabels()[:1000]
        
        self.conv = Convolutional3x3(8)                  
        self.pool = MaxPool()                
        self.softmax = Softmax(13 * 13 * 8, 10) 
        
    def forward(self, image, label):
      out = self.conv.forward((image / 255) - 0.5)
      out = self.pool.forward(out)
      out = self.softmax.forward(out)
    
      loss = -np.log(out[label])
      acc = 1 if np.argmax(out) == label else 0
    
      return out, loss, acc
  
    def train(self, im, label, lr=.005):
      out, loss, acc = self.forward(im, label)
    
      gradient = np.zeros(10)
      gradient[label] = -1 / out[label]
    
      gradient = self.softmax.backprop(gradient, lr)
      gradient = self.pool.backprop(gradient)
      gradient = self.conv.backprop(gradient, lr)
    
      return loss, acc
  
    
    def solve(self):
        print('MNIST CNN initialized!')

        for epoch in range(3):
          print('--- Epoch %d ---' % (epoch + 1))
        
          permutation = np.random.permutation(len(self.train_images))
          self.train_images = self.train_images[permutation]
          self.train_labels = self.train_labels[permutation]
        
          loss = 0
          num_correct = 0
          for i, (im, label) in enumerate(zip(self.train_images, self.train_labels)):
            if i % 100 == 99:
              print(
                '[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%' %
                (i + 1, loss / 100, num_correct)
              )
              loss = 0
              num_correct = 0
        
            l, acc = self.train(im, label)
            loss += l
            num_correct += acc
        
        print('\n--- Testing the CNN ---')
        loss = 0
        num_correct = 0
        for im, label in zip(self.test_images, self.test_labels):
          _, l, acc = self.forward(im, label)
          loss += l
          num_correct += acc
        
        num_tests = len(self.test_images)
        print('Test Loss:', loss / num_tests)
        print('Test Accuracy:', num_correct / num_tests)



    