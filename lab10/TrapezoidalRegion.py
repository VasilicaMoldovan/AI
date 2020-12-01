# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:12:36 2020

@author: Vasilica
"""


class TrapezoidalRegion:
    def __init__(self, a, b, c, d, name):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__name = name
        
    def getRegionName(self):
        return self.__name
    
    def computeFunction(self, x):
        aux1 = 1
        if (self.__b - self.__a != 0):
            aux = (x - self.__a) / (self.__b - self.__a)
            if aux1 > aux:
                aux1 = aux
        if (self.__d - self.__c != 0):
            aux = (self.__d - x) / (self.__d - self.__c)
            if aux1 > aux:
                aux1 = aux
                
        if aux1 < 0:
            return 0
        else:
            return aux1
        