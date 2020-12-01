# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:57:53 2020

@author: Vasilica
"""

from Problem import Problem
from ArtificialNeuralNetwork import ArtificialNeuralNetwork
import matplotlib as mpl

class Controller:
    def __init__(self, filename):
        self.__problem = Problem(filename)
        self.__x = self.__problem.getX()
        self.__y = self.__problem.getY()
        self.__nn = ArtificialNeuralNetwork(self.__x, self.__y, 2)
        
    def solve(self):
        self.__nn.loss=[]
        iterations =[]
        for i in range(4000):
            self.__nn.feedforward()
            learning_rate = 0.5
            self.__nn.backpropagation(learning_rate)
            iterations.append(i)
    
        print(self.__nn.output)
        mpl.pyplot.plot(iterations, self.__nn.loss, label='loss value vs iteration')
        mpl.pyplot.xlabel('Iterations')
        mpl.pyplot.ylabel('loss function')
        mpl.pyplot.legend()
        mpl.pyplot.show()
        
        
