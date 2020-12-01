# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:34:33 2020

@author: Vasilica
"""
from Problem import Problem
from Controller import Controller
import math
import matplotlib.pyplot as plt
import numpy as np


class Validator:
    def __init__(self, nrOfEvaluations, nrOfRuns, nrOfIndividuals):
        self.__nrOfEvaluations = nrOfEvaluations
        self.__nrOfRuns = nrOfRuns
        self.__nrOfIndividuals = nrOfIndividuals
        
    def plotACO(self):
        p = Problem()
        controller = Controller(self.__nrOfIndividuals , p.getSize(), self.__nrOfEvaluations)
        
        fitnesses = [] 
        
        for i in range(self.__nrOfRuns):
            sol = controller.runAlgorithm()
            permSolution = sol[0]
            print(sol[1])
            fitnesses.append(sol[1])
            
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
        
        