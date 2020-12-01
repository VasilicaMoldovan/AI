# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:16:01 2020

@author: Vasilica
"""
from TriangularRegion import TriangularRegion
from TrapezoidalRegion import TrapezoidalRegion
from Rule import Rule

class Problem:
    def __init__(self, fileName1, fileName2, fileName3):
        self.__fileName1 = fileName1
        self.__fileName2 = fileName2
        self.__fileName3 = fileName3
        self.createTemperatureRegions()
        self.createHumidityRegions()
        self.createRules()
        
        
    def createTemperatureRegions(self):
        file = open(self.__fileName1)
        self.__temperatureRegions = []
        trapez = ["very cold", "normal", "hot"]
        line = file.readline().strip()
        while (line != ""):
            name = line
            line = file.readline()
            parameters = line.split(" ")
            
            if name in trapez:
                region = TrapezoidalRegion(int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3]), name)
                self.__temperatureRegions.append(region)
            else:
                region = TriangularRegion(int(parameters[0]), int(parameters[1]), int(parameters[2]), name)
                self.__temperatureRegions.append(region)
           
            line = file.readline().strip()  
            
        file.close()
            
    def createHumidityRegions(self):
        file = open(self.__fileName2)
        self.__humidityRegions = []
        line = file.readline().strip()
        while (line != ""):
            name = line
            line = file.readline()
            parameters = line.split(" ")
            
            region = TriangularRegion(int(parameters[0]), int(parameters[1]), int(parameters[2]), name)
            self.__humidityRegions.append(region)
            
            line = file.readline().strip()
            
        file.close()
            
    def createRules(self):
        file = open(self.__fileName3)
        self.__rules = []
        line = file.readline().strip()
        while (line != ""):
            parameters = line.split(" ")
            if parameters[0] == "very":
                rule = Rule(parameters[0] + " " + parameters[1], parameters[2], parameters[3], int(parameters[4]), int(parameters[5]))
            else:
                rule = Rule(parameters[0], parameters[1], parameters[2], int(parameters[3]), int(parameters[4]))
            self.__rules.append(rule)
            
            line = file.readline().strip()
            
        file.close()
            
    def getTemperatureRegions(self):
         return self.__temperatureRegions
     
    def getHumidityRegions(self):
        return self.__humidityRegions
    
    def getRules(self):
        return self.__rules