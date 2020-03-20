# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:34:17 2020

@author: Vasilica
"""


import matplotlib.pyplot as plt
import numpy as np

def main():
    lowerBound = int(input("Give the lower bound: "))
    upperBound = int(input("Give the upper bound: "))
    
    print("1. Print random nr with Normal Distribution")
    print("2. Print plot of nr with Normal Distribution")
    print("3. Print random nr with Uniform Distribution")
    print("4. Print plot of nr with Uniform Distribution")
    print("5. Print random nr with Geometric Distribution")
    print("6. Print plot of nr with Geometric Distribution")
    
    while True:
        command = int(input("Option: "))
        if command == 0:
            return 
        elif command == 1:
            mu, sigma = 0, 0.1
            s = np.random.normal((upperBound - lowerBound) / 2 + lowerBound, sigma, upperBound - lowerBound)
            print(s)
        elif command == 2:
            sigma = 0.1
            s = np.random.normal((upperBound - lowerBound) / 2 + lowerBound, sigma, upperBound - lowerBound)
            plt.plot(s, 'ro')
            plt.ylabel('numbers')
            plt.axis([0, upperBound - lowerBound, lowerBound, upperBound])
            plt.show()
        elif command == 3:
            u = np.random.uniform(lowerBound, upperBound, upperBound - lowerBound)
            print(u)
        elif command == 4:
            u = np.random.uniform(lowerBound, upperBound, upperBound - lowerBound)
            plt.plot(u, 'ro')
            plt.ylabel('numbers')
            plt.axis([0, upperBound - lowerBound, lowerBound, upperBound])
            plt.show()
        elif command == 5:
            g = np.geomspace(lowerBound, upperBound, 20)
            print(g)
        elif command == 6:
            g = np.geomspace(lowerBound, upperBound, 20)
            plt.plot(g, 'ro')
            plt.ylabel('numbers')
            plt.axis([0, upperBound - lowerBound, lowerBound, upperBound])
            plt.show()
        elif command == 7:
             u = np.random.uniform(lowerBound, upperBound)
             print(u)
           
            
main()