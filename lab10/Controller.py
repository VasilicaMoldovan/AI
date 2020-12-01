# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:15:18 2020

@author: Vasilica
"""
from Problem import Problem
import random

class Controller:
    def __init__(self, problem):
        self.__temperatureRegions = problem.getTemperatureRegions()
        self.__humidityRegions = problem.getHumidityRegions()
        self.__rules = problem.getRules()
        
    def getTemperatureRegion(self, name):
        for temp in self.__temperatureRegions:
            if temp.getRegionName() == name:
                return temp 
            
    def getHumidityRegion(self, name):
        for temp in self.__humidityRegions:
            if temp.getRegionName() == name:
                return temp 
    
    def createTempDictionary(self):
        for temp in self.__temperatureRegions:
            self.__tempResults[temp.getRegionName()] = 0
            
    def createHumidityDictionary(self):
        for humidity in self.__humidityRegions:
            self.__humidityResults[humidity.getRegionName()] = 0
            
    def getRulesResults(self):
        resultShort = 0
        resultLong = 0
        resultMedium = 0
        for temp in self.__rules:
            #print(str(temp))
            if ( temp.getTime() == "short" and temp.getValue() > resultShort):
                resultShort = temp.getValue()
            if ( temp.getTime() == "long" and temp.getValue() > resultLong):
                resultLong = temp.getValue()
            if ( temp.getTime() == "medium" and temp.getValue() > resultMedium):
                resultMedium = temp.getValue()
                
        return resultShort, resultLong, resultMedium
    

    def getIntervals(self):
        pass
        
    def solveFuzzy(self):
        T = random.randint(-30, 35)
        H = random.randint(0, 100)
        self.__tempResults = {}
        self.__humidityResults = {}
        
        for rule in self.__rules:
            if rule.getTemperature() not in self.__tempResults:
                aux = self.getTemperatureRegion(rule.getTemperature())
                resultT = aux.computeFunction(T)
                self.__tempResults[rule.getTemperature()] = resultT
            else:
                resultT = self.__tempResults[rule.getTemperature()]
            if rule.getHumidity() not in self.__humidityResults:
                aux = self.getHumidityRegion(rule.getHumidity())
                resultH = aux.computeFunction(H)
                self.__humidityResults[rule.getHumidity()] = resultH
            else:
                resultH = self.__humidityResults[rule.getHumidity()]
                
            result = min(resultT, resultH)
            rule.setValue(result)
        
        partialResult = 0
        aux1 = 0
        aux2 = 0
        denominator = 0
        resultShort, resultLong, resultMedium = self.getRulesResults()
        #print(resultShort)
        #print(resultLong)
        #print(resultMedium)
        for i in range(0, 101):
            if (i < 50):
            #verification for short region
            #we check if the given result does not exced the graph
                aux1 = 1 - (0.02 * i)
                if ( resultShort <= aux1 ):
                    aux1 = resultShort
            #verification for medium region
                aux2 = (0.02) * i
                if resultMedium <= aux2:
                    aux2 = resultMedium
                partialResult += (i * max(aux1, aux2))
            else:
                #verification for medium region
                aux1 = 1 - (0.02 * (i - 50))
                if resultMedium <= aux1:
                    aux1 = resultMedium
                 #verification for long region
                aux2 = (i - 50) * 0.02
                if resultLong <= aux2:
                    aux2 = resultLong
                partialResult += (i * max(aux1, aux2))
                denominator += max(aux1, aux2)
        if denominator > 0:
            partialResult = partialResult / denominator
            
        f = open("output.out", "a")
        string = "For temperature " + str(T) + " and humidty " + str(H) + ", we obtain time = " + str(partialResult)
        f.write(string + "\n")
        f.close()

        print(string)
                
                
                
                
                
                
        