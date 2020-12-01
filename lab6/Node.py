# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:49:21 2020

@author: Vasilica
"""
from collections import Counter

class Node:
     def __init__(self, rows):
        self.__classes = self.classDistribution(rows)
        
     def classDistribution(self, rows):
        return Counter([row[-1] for row in rows])
    
     def getClasses(self):
         return self.__classes
     
     def setClasses(self, classes):
         self.__classes = classes