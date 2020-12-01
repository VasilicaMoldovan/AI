# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:35:33 2020

@author: Vasilica
"""
from random import randrange

class Problem:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__dataset = self.readFromFile()
        self.__minMax = self.dataset_minmax()
        
    def readFromFile(self):
        self.__x = []
        self.__y = []
        dataset = list()
        file = open(self.__fileName, 'r')
        line = file.readline()
        while line != "" and line != None:
            values = line.split(" ")
            x_aux = []
            for i in range(6):
                x_aux.append(float(values[i]))
            dataset.append(x_aux)
            line = file.readline()
            line = file.readline()
            
        return dataset
    
            
    def dataset_minmax(self):
        minmax = list()
        for i in range(len(self.__dataset[0])):
            col_values = [row[i] for row in self.__dataset]
            value_min = min(col_values)
            value_max = max(col_values)
            minmax.append([value_min, value_max])
        return minmax
        
    def normalize_dataset(self):
        for row in self.__dataset:
            for i in range(len(row)):
                row[i] = (row[i] - self.__minMax[i][0]) / (self.__minMax[i][1] - self.__minMax[i][0])
        
        
    def cross_validation_split(self, n_folds):
        dataset_split = list()
        dataset_copy = list(self.__dataset)
        fold_size = int(len(self.__dataset) / n_folds)
        for i in range(n_folds):
            fold = list()
            while len(fold) < fold_size:
                index = randrange(len(dataset_copy))
                fold.append(dataset_copy.pop(index))
            dataset_split.append(fold)
        return dataset_split
    
    def prepareDataSet(self):
        self.normalize_dataset()
    
    
    def getDataSet(self):
        return self.__dataset
    
    def getY(self):
        return self.__y