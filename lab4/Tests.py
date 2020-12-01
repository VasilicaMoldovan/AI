# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:28:15 2020

@author: Vasilica
"""
from Entity import *
from EARepository import *
from PSORepository import *
import math
import matplotlib.pyplot as plt
import numpy as np

class Test:
    def __init__(self, nrOfEvaluations, nrOfRuns, nrOfIndividuals):
        self.__nrOfEvaluations = nrOfEvaluations
        self.__nrOfRuns = nrOfRuns
        self.__nrOfIndividuals = nrOfIndividuals
        
    def testEa(self):
        dimIndividual = 4
        firstSet = ['$', '#', '@', '&']
        secondSet = [1, 2, 3, 4]
        pM=0.01
        pC = 0.8
        e = Entity(self.__nrOfIndividuals, pC, pM, dimIndividual, firstSet, secondSet)
        ea = EA(self.__nrOfEvaluations, e)
        mean = 0
        stdDev = 0
        fitnesses = []
        
        for i in range(self.__nrOfRuns):
            aux = ea.solveEA()
            fitnesses.append(aux)
            mean += aux
            
        mean = mean / self.__nrOfRuns
        for i in range(self.__nrOfRuns):
            stdDev += ((fitnesses[i] - mean) * (fitnesses[i] - mean))
            
        stdDev = stdDev / self.__nrOfRuns
        stdDev = math.sqrt(stdDev)
        
        print(mean)
        print(stdDev)
        
    def plotPSO(self):
        firstSet = [1, 2, 3, 4]
        secondSet = [1, 2, 3, 4]
        dimParticle = 4
        #specific parameters for PSO
        w=1.0
        c1=1.
        c2=2.5
        sizeOfNeighborhood=20
        
        pso = PSO(dimParticle, self.__nrOfIndividuals, self.__nrOfEvaluations, firstSet, secondSet, w, c1, c2, sizeOfNeighborhood)
        fitnesses = []
        
        for i in range(self.__nrOfRuns):
            P = pso.population()
            sol = pso.solve(P)
            print(sol[0])
            fitnesses.append(sol[0])
            
        print(sol[1])    
        m = np.mean(fitnesses, axis=0)
        std = np.std(fitnesses, axis=0)
        means = []
        stddev = []
        
        for i in range(self.__nrOfRuns):
            means.append(m)
            stddev.append(std)
            
        plt.plot(range(self.__nrOfRuns), means)
        plt.plot(range(self.__nrOfRuns), stddev)
        plt.plot(range(self.__nrOfRuns), fitnesses)
        plt.show()
        
        
    def plotEa(self):
        dimIndividual = 4
        firstSet = ['$', '#', '@', '&']
        secondSet = [1, 2, 3, 4]
        pM=0.01
        pC = 0.8
        e = Entity(self.__nrOfIndividuals, pC, pM, dimIndividual, firstSet, secondSet)
        ea = EA(self.__nrOfEvaluations, e)
        fitnesses = []
        
        for i in range(self.__nrOfRuns):
            sol = ea.solveEA()
            print(sol)
            fitnesses.append(sol)
            
        m = np.mean(fitnesses, axis=0)
        std = np.std(fitnesses, axis=0)
        means = []
        stddev = []
        
        for i in range(self.__nrOfRuns):
            means.append(m)
            stddev.append(std)
            
        plt.plot(range(self.__nrOfRuns), means)
        plt.plot(range(self.__nrOfRuns), stddev)
        plt.plot(range(self.__nrOfRuns), fitnesses)
        plt.show()
            

def main():
    test = Test(1000, 30, 40)
    #test.plotEa()
    test.plotPSO()
    
main()