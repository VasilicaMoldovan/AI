# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:54:16 2020

@author: Vasilica
"""


class Rule:
    def __init__(self, temperature, humidity, time, intervalStart, intervalEnd):
        self.__value = 0
        self.__temperature = temperature
        self.__humidity = humidity
        self.__time = time
        self.__intervalStart = intervalStart 
        self.__intervalEnd = intervalEnd
        
    def addToValue(self, val):
        self.__value += val 
        
    def setValue(self, val):
        if val > self.__value:
            self.__value = val
        
    def getValue(self):
        return self.__value
    
    def getTemperature(self):
        return self.__temperature
    
    def getHumidity(self):
        return self.__humidity
    
    def getTime(self):
        return self.__time
    
    def getIntervalStart(self):
        return self.__intervalStart
    
    def getIntervalEnd(self):
        return self.__intervalEnd
    
    def __str__(self):
        return self.__temperature + " " + self.__humidity + " " + self.__time + " " + str(self.__value); 
