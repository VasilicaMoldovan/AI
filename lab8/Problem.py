# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:56:48 2020

@author: Vasilica
"""
import numpy as np

class Problem:
    def __init__(self, filename):
        self.__filename = filename 
        self.readData()
        
    def readData(self):
        self.__x = []
        self.__y = []
        file = open(self.__filename, 'r')
        line = file.readline()
        while line != "":
            values = line.split(" ")
            aux_x = [float(values[i]) for i in range(5)]
            self.__x.append(aux_x)
            self.__y.append([float(values[5])])
            line = file.readline()
            line = file.readline()
            
    def dataset_minmax(self, x):
        minmax = list()
        for i in range(len(x[0])):
            col_values = [row[i] for row in x]
            value_min = min(col_values)
            value_max = max(col_values)
            minmax.append([value_min, value_max])
        return minmax
        
    def normalize_dataset(self, x):
        for row in x:
            for i in range(len(row)):
                row[i] = (row[i] - self.__minMax[i][0]) / (self.__minMax[i][1] - self.__minMax[i][0])
    
            
    def getX(self):
        self.__minMax = self.dataset_minmax(self.__x)
        self.normalize_dataset(self.__x)
        return np.array(self.__x,dtype=np.float64)

    def getY(self):
        self.__minMax = self.dataset_minmax(self.__y)
        self.normalize_dataset(self.__y)
        return np.array(self.__y,dtype=np.float64)
            
            