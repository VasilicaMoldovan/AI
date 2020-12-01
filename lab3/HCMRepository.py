# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:11:39 2020

@author: Vasilica
"""

import random
import itertools
import operator
from Entity import Entity

class HillClimbing:
    def __init__(self, nrOfIterations, entity):
        self.__nrOfIterations = nrOfIterations
        self.__entity = entity
        
    def hillClimbingMethod(self):
        pop = self.__entity.population(self.__entity.getNrOfIndividuals(), self.__entity.getDimIndividual(), self.__entity.getFirstSet(), self.__entity.getSecondSet())
        index = random.randint(0, len(pop) - 1)
        initialState = pop[index]
        index1 = index 
        bestScore = self.__entity.fitness(pop[index])
        
        if bestScore == 0:
            return (bestScore, pop[index])
        else:
            index = random.randint(0, len(pop) - 1)
            
            while index1 == index:
                index = random.randint(0, len(pop) - 1)
                
            bestScore = min(bestScore, self.__entity.fitness(pop[index]))
            solution = pop[index]
        
            graded = [ (self.__entity.fitness(x), x) for x in pop]
            graded = sorted(graded, key=lambda x: x[0])
            target = graded[0]
            
            index1 = 1   
            i = 0
            while bestScore != 0 and solution != initialState and i < self.__nrOfIterations:
               child = self.__entity.crossover(initialState, pop[index], self.__entity.getCrossProb())
               child = self.__entity.mutate(child, self.__entity.getMutationProb(), self.__entity.getFirstSet(), self.__entity.getSecondSet())
               score = self.__entity.fitness(child)
                
               if score == 0: 
                   return (score, child)
                   
               if score < bestScore:
                    initialState = solution
                    solution = child
                    bestScore = score 
               else:
                   if target[0] < bestScore:
                       initialState = solution 
                       solution = target[1]
                       bestScore = self.__entity.fitness(solution)
                       target = graded[index1]
                       index1 += 1
                    
               i += 1
                    
            return (bestScore, solution)
      
        
def main():
    dimIndividual = 3
    firstSet = [1, 2, 3]
    secondSet = [1, 2, 3]
    pM=0.01
    pC = 0.8
    e = Entity(40, pC, pM, dimIndividual, firstSet, secondSet)
    nrOfIterations = 100000
    hillClimb = HillClimbing(nrOfIterations, e)
    sol = hillClimb.hillClimbingMethod()
    print(sol[1])
    print(sol[0])

main()    
        
             
                    
                    