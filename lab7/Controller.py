# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:05:40 2020

@author: Vasilica
"""
import numpy as np
from Problem import Problem

class Controller:
    def __init__(self, noOfIterations, problem):
        self.__learningRate = 0.1
        self.__noOfIterations = noOfIterations
        self.__problem = problem
        aux = self.__problem.getX()
        self.__x = np.c_[np.ones((len(aux), 1)), aux]
        self.__y = self.__problem.getY()
        
    def costFunction(self, theta, x, y):
        m = len(y)
        predictions = x.dot(theta)
        cost = (1/2 * m) * np.sum(np.square(predictions - y))
        return cost 
    
    def gradientDescent(self, theta, x):
        m = len(self.__y)
        cost_history = np.zeros(self.__noOfIterations)
        theta_history = np.zeros((self.__noOfIterations, len(self.__y)))
        
        for i in range(self.__noOfIterations):
            prediction = np.dot(x, theta)
            theta = theta - (1/m) * self.__learningRate * (x.T.dot((prediction - self.__y)))
            theta_history = theta.T
            cost_history[i] = self.costFunction(theta, x, self.__y)
            
        return theta, cost_history, theta_history
    
    def stochasticGradientDescent(self, theta):
        m = len(self.__y)
        cost_history = np.zeros(self.__noOfIterations)
        
        for i in range(self.__noOfIterations):
            cost = 0.0
            for j in range(m):
                rand_ind = np.random.randint(0, m)
                x_j = self.__x[rand_ind, :].reshape(1, self.__x.shape[1])
                y_j = self.__y[rand_ind].reshape(1, 1)
                prediction = np.dot(x_j, theta)
                theta = theta - (1/m) * self.__learningRate * (x_j.T.dot((prediction - y_j)))
                cost += self.costFunction(theta, x_j, y_j)
            cost_history[i] = cost
            
        return theta, cost_history
    
    def getError(self, theta):
        self.__x = self.__problem.getX()
        n = len(self.__y)
        error = 0.0
        for i in range(n):
            for j in range(5):
                error += abs(self.__y[i] - self.__x[i][j])
                
        error = error / n
        return error
        
        
            
                
            
       
    