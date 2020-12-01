# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:55:20 2020

@author: Vasilica
"""

class DecisionTree:
    def __init__(self, attribute, goodBranch, falseBranch):
        self.__attribute = attribute
        self.__goodBranch = goodBranch
        self.__falseBranch = falseBranch
        
    def getAttribute(self):
        return self.__attribute
    
    def getGoodBranch(self):
        return self.__goodBranch
    
    def getFalseBranch(self):
        return self.__falseBranch