# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:26:03 2020

@author: Vasilica
"""
import numpy as np
from Problem import Problem
from Controller import Controller

def main():
    theta = np.random.randn(6, 1)
    p = Problem("database.txt")
    #x = p.getX()
    y = p.getY()
    c = Controller(10, p)
    #x_b = np.c_[np.ones((len(x), 1)), x]
    '''
    #theta, cost_history, theta_history = c.gradientDescent(theta, x_b)
    theta, cost_history = c.stochasticGradientDescent(theta)
    error = c.getError(theta)
    print("Theta:")
    print(theta[0][0])
    print("Theta1:")
    print(theta[1][0])
    print("Theta2:")
    print(theta[2][0])
    print("Theta3:")
    print(theta[3][0])
    print("Theta4:")
    print(theta[4][0])
    
    print("Error:")
    print(error)
    '''
    X = 2 * np.random.rand(100,5)
    #y = 4 +3 * X+np.random.randn(100,1)
    print(X)
    print("bine")
    print("bine")
    print("bine")
    print(y)
    
main()


