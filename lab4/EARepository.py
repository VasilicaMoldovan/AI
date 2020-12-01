# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:24:10 2020

@author: Vasilica
"""

import random
import itertools
import operator
from Entity import Entity


class EA:
    def __init__(self, nrOfIterations, entity):
        self.__nrOfIterations = nrOfIterations
        self.__entity = entity
        
    
    def iteration(self, population, pC, pM, firstSet, secondSet):
        '''
        an iteration
    
        population: the current population
        pM: the probability the mutation to occure
        firstSet: the first set of values
        secondSet: the second set of values
        '''
        i1 = random.randint(0, len(population) - 1)
        i2 = random.randint(0, len(population) - 1)
        
        if (i1 != i2):
            c = self.__entity.crossover(population[i1], population[i2], pC)
            c = self.__entity.mutate(c, pM, firstSet, secondSet)
            f1 = self.__entity.fitness(population[i1])
            f2 = self.__entity.fitness(population[i2])
            fc = self.__entity.fitness(c)
            
            if(f1 > f2) and (f1 > fc):
                population[i1] = c
                
            if(f2 > f1) and (f2 > fc):
                population[i2] = c
                
            if (f1 > f2) and (f2 > fc):
                return (population, f1)
            
            elif (f1 < f2) and (f2 < fc):
                return (population, fc)
            
            else:
                return (population, f2)
            
        return (population, self.__entity.fitness(population[i1]))
        

    def eaIteration(self, population, pC, pM, firstSet, secondSet):
        fit = {}
        for i in range(len(population)):
            fit[i] = self.__entity.fitness(population[i])
            
        sorted_fit = sorted(fit.items(), key=operator.itemgetter(1))
        f1 = population[list(fit.keys())[list(fit.values()).index(sorted_fit[0][1])]]
        f2 = population[list(fit.keys())[list(fit.values()).index(sorted_fit[1][1])]]
        
        c = self.__entity.crossover(f1, f2, pC)
        c = self.__entity.mutate(c, pM, firstSet, secondSet)
        
        fc = self.__entity.fitness(c)
        n = len(sorted_fit) - 1
        
        lastParent = population[list(fit.keys())[list(fit.values()).index(sorted_fit[n][1])]]
        fl = self.__entity.fitness(lastParent)
        f = self.__entity.fitness(f1)
        
        if fc > fl:
            for i in range(len(population)):
                if population[i] == lastParent:
                    population[i] = c
                    break 
        if fc > f:
            return (population, fc)
        else:
            return (population, f)


    def solveEA(self):
        P = self.__entity.population(self.__entity.getNrOfIndividuals(), self.__entity.getDimIndividual(), self.__entity.getFirstSet(), self.__entity.getSecondSet())
        
        for i in range(self.__nrOfIterations):
            P = self.eaIteration(P, self.__entity.getCrossProb(), self.__entity.getMutationProb(), self.__entity.getFirstSet(), self.__entity.getSecondSet())[0]
            #P = self.iteration(P, self.__entity.getCrossProb(), self.__entity.getMutationProb(), self.__entity.getFirstSet(), self.__entity.getSecondSet())[0]
            
        graded = [ (self.__entity.fitness(x), x) for x in P]
        graded = sorted(graded, key=lambda x: x[0])
        result = graded[0]
        fitnessOptim = result[0]
        individualOptim = result[1]
        '''
        print(individualOptim)
        print(fitnessOptim)
        print(self.__nrOfIterations)
        '''
        return fitnessOptim







