# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:46:19 2020

@author: Vasilica
"""
from math import floor
from random import shuffle

class Problem:
    def __init__(self, path):
        self.__path = path
        
    def readData(self):
        dataSet = []
        with open(self.__path, 'r') as f:
            for line in f.readlines():
                row = line.split(',')
                record = row.pop(0)
                aux = []
                for val in row:
                    aux.append(int(val))
                row = aux
                row.append(record)
    
                dataSet.append(row)
                
        return dataSet
    
    def splitData(self, data, p):
        if p == 1:
            return data, data
        length = len(data)
        split = floor(p * length)
        shuffle(data)
        return data[:split], data[split:]
