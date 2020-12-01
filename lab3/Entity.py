# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:57:46 2020

@author: Vasilica
"""

import random
import itertools
import operator
from math import sin, pow

class Entity:
    def __init__(self, nrOfIndividuals, crossProb, mutationProb, dimIndividual, firstSet, secondSet):
        self.__nrOfIndividuals = nrOfIndividuals
        self.__crossProb = crossProb
        self.__mutationProb = mutationProb
        self.__dimIndividual = dimIndividual
        self.__firstSet = firstSet
        self.__secondSet = secondSet
        
    def getNrOfIndividuals(self):
        return self.__nrOfIndividuals
        
    def getFirstSet(self):
        return self.__firstSet
    
    def getSecondSet(self):
        return self.__secondSet
    
    def getDimIndividual(self):
        return self.__dimIndividual
    
    def getMutationProb(self):
        return self.__mutationProb
    
    def getCrossProb(self):
        return self.__crossProb
        
    def individual(self, length, firstSet, secondSet):
        '''
        Create a member of the population - an individual
    
        length: the number of genes (components)
        firstSet: the first set of values
        secondSet: the second set of values
        '''
        set = list(range(0, length)) 
        perm = list(itertools.permutations(set))
        n = 2 * length
        perm = perm[:n]
        individ = []
        for i in range(0, length):
            auxSet = []
            for j in range(0, length):
                auxSet.append(firstSet[perm[i][j]])
            individ.append(auxSet)
            
        for i in range(length, len(perm)):
            auxSet = []
            for j in range(0, length):
                auxSet.append(secondSet[perm[i][j]])
            individ.append(auxSet)
        
        return individ 
    
    def population(self, count, length, firstSet, secondSet):
        """
        Create a number of individuals (i.e. a population).
    
        count: the number of individuals in the population
        length: the number of values per individual
        firstSet: the first set of values
        secondSet: the second set of values
        """
        population = []
        for x in range(count):
            individ = self.individual(length, firstSet, secondSet)
            random.shuffle(individ)
            population.append(individ)
        return population
    
    
    def fitness(self, individual):
        """
        Determine the fitness of an individual. How many mistakes has the current  
        individual
        individual: the individual to evaluate
        """
        fitness = 0
        length = len(individual) // 2
        for k in range(len(individual)):
            for i in range(length):
                for j in range(i + 1, length):
                    if individual[k][i] == individual[k][j]:
                        fitness += 1
           
        for k in range(length):
            for i in range(length):
                for j in range(i + 1, length):
                    if individual[i][k] == individual[j][k]:
                        fitness += 1
                        
        for k in range(length):
            for i in range(length, len(individual)):
                for j in range(i + 1, len(individual)):
                    if individual[i][k] == individual[j][k]:
                        fitness += 1
            
        return fitness
    
    def mutate(self, individual, pM, firstSet, secondSet): 
        '''
        Performs a mutation on an individual with the probability of pM.
    
        individual:the individual to be mutated
        pM: the probability the mutation to occure
        firstSet: the first set of values
        secondSet: the second set of values
        '''
        if pM > random.random():
                length = len(individual) // 2
                set = list(range(0, length)) 
                perm = list(itertools.permutations(set))
                if len(individual) > 1:
                    p = random.randint(0, len(individual)-1)
                    
                    if p < length:
                        aux = []
                        for i in range(length):
                            aux.append(firstSet[perm[p][i]])
                        individual[p] = aux
                    else:
                        aux = []
                        for i in range(length):
                            aux.append(secondSet[perm[p][i]])
                        individual[p] = aux
                        
        return individual
    
    
    def crossover(self, parent1, parent2, pC):
        '''
        crossover between 2 parents
        '''
        child=[]
        n = len(parent1)
        t1 = random.randint(0, n - 2)
        t2 = random.randint(t1 + 1, n - 1)
        
        if pC > random.random():
            for i in range(t1):
                child.append(parent1[i])
                
            for i in range(t1, t2):
                child.append(parent2[i])
                
            for i in range(t2, n):
                child.append(parent1[i])
            
            return child
        else:
            return parent1
        
        
        
        
class Particle:        
     def __init__(self, length, firstSet, secondSet):
        self.__length = length
        self.__firstSet = firstSet
        self.__secondSet = secondSet
        self._position = self.individual()
        self.evaluate()
        self.velocity = [ 0 for i in range(length)]
        
        #the memory of that particle
        self._bestPosition=self._position.copy()
        self._bestFitness=self._fitness
        
     def __str__(self):
        return str(self._position)
        
     def individual(self):
        '''
        Create a member of the population - an individual
    
        length: the number of genes (components)
        firstSet: the first set of values
        secondSet: the second set of values
        '''
        set = list(range(0, self.__length)) 
        perm = list(itertools.permutations(set))
        random.shuffle(perm)
        n = 2 * self.__length
        perm = perm[:n]
        individ = []
        for i in range(0, self.__length):
            auxSet = []
            for j in range(0, self.__length):
                auxSet.append(self.__firstSet[perm[i][j]])
            individ.append(auxSet)
            
        for i in range(self.__length, len(perm)):
            auxSet = []
            for j in range(0, self.__length):
                auxSet.append(self.__secondSet[perm[i][j]])
            individ.append(auxSet)
        
        return individ 
    
     def fit(self):
        """
        Determine the fitness of an individual. How many mistakes has the current  
        individual
        individual: the individual to evaluate
        """
        fitness = 0
        length = len(self._position) // 2
        for k in range(len(self._position)):
            for i in range(length):
                for j in range(i + 1, length):
                    if self._position[k][i] == self._position[k][j]:
                        fitness += 1
           
        for k in range(length):
            for i in range(length):
                for j in range(i + 1, length):
                    if self._position[i][k] == self._position[j][k]:
                        fitness += 1
                        
        for k in range(length):
            for i in range(length, len(self._position)):
                for j in range(i + 1, len(self._position)):
                    if self._position[i][k] == self._position[j][k]:
                        fitness += 1
            
        return fitness
    
     def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fit()
        
    
     @property
     def position(self):
        """ getter for pozition """
        return self._position

     @property
     def fitness(self):
        """ getter for fitness """
        return self._fitness

     @property
     def bestPosition(self):
        """ getter for best pozition """
        return self._bestPosition

     @property
     def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness
    
     @position.setter
     def position(self, newPosition):
        self._position = newPosition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self._fitness < self._bestFitness):
            self._bestPosition = self._position
            self._bestFitness  = self._fitness
            
'''  
def main():
    length = 3
    firstSet = [1, 2, 3]
    secondSet = [1, 2, 3]
    particle = Particle(length, firstSet, secondSet)
    print(particle.individual(length, firstSet, secondSet))
    
main()
'''