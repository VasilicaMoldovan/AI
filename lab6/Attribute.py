# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:53:29 2020

@author: Vasilica
"""
class Attribute:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.__header = None

    def compare(self, attribute):
        auxVal = attribute[self.__name]
        if isinstance(auxVal, int) or isinstance(auxVal, float):
            return auxVal >= self.__value
        else:
            return auxVal == self.__value