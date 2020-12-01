# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:04:00 2020

@author: Vasilica
"""


class TriangularRegion:
    def __init__(self, a, b, c, name):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__name = name
        
    def getRegionName(self):
        return self.__name
    
    def computeFunction(self, x):
        aux1 = 1
        if (self.__b - self.__a != 0):
            aux = (x - self.__a) / (self.__b - self.__a)
            if aux1 > aux:
                aux1 = aux
        if (self.__c - self.__b != 0):
            aux = (self.__c - x) / (self.__c - self.__b)
            if aux1 > aux:
                aux1 = aux
                
        if aux1 < 0:
            return 0
        else:
            return aux1
        
    def __str__(self):
        return str(self.__a) + " " + str(self.__b) + " " + str(self.__c) + " " + self.__name; 