# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:34:11 2020

@author: Vasilica
"""

from functools import reduce
from math import floor
from random import randint, random, seed
from typing import List
from numpy.random import choice

from Chromosome import Chromosome
from Problem import Problem

DEPTH_MAX = 6
terminals = ['-165', '-150', '-135', '-120', '-105', '-90', '-75',
             '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75',
             '90', '105', '120', '135', '150', '165'] 
functions = ['+', '-', '*', 'sin', 'cos']
unaryFunctions = ['sin', 'cos']
binaryFunctions = ['+', '-', '*']
constants = []
classes = {
    'Slight-Left-Turn':     0,
    'Move-Forward':         1,
    'Slight-Right-Turn':    2,
    'Sharp-Right-Turn':     3
}

class Controller:
    def __init__(self, problem):
        self._problem  = problem
        
    def crossover(self, parent1, parent2):
        offspring = Chromosome(DEPTH_MAX, terminals, functions, constants)
    
        startParent1 = randint(0, parent1.size - 1)
        endParent1 = parent1.traverse(startParent1)
    
        startParent2 = randint(0, parent2.size - 1)
        endParent2 = parent2.traverse(startParent2)
    
        offspring.representation = [0 for _ in range(len(parent1.representation) + len(parent2.representation))]
    
        while len(offspring.representation) < len(parent1.representation) + len(parent2.representation):
            offspring.representation += [0]
        i = -1
        for i in range(startParent1):
            offspring[i] = parent1[i]
        for j in range(startParent2, endParent2):
            i = i + 1
            offspring[i] = parent2[j]
        for j in range(endParent1, parent1.size):
            i = i + 1
            offspring[i] = parent1[j]
        offspring.representation = [x for x in offspring.representation if x != 0]
        offspring.size = len(offspring.representation)
        return offspring
    
    
    def mutation(self, chromosome):
        offspring = Chromosome(DEPTH_MAX, terminals, functions, constants)
        pos = randint(0, chromosome.size-1)
        offspring.representation = chromosome[:]
        offspring.size = chromosome.size
        if offspring[pos] > 0:
            offspring[pos] = randint(1, len(terminals))
        else:
            currentFunction = offspring.getFunctionByIndex(pos)
            if currentFunction in unaryFunctions:
                while True:
                    offspring[pos] = -randint(1, len(functions))
                    newFunction = offspring.getFunctionByIndex(pos)
                    if newFunction in unaryFunctions and newFunction != currentFunction:
                        break
            else:
                while True:
                    offspring[pos] = -randint(1, len(functions))
                    newFunction = offspring.getFunctionByIndex(pos)
                    if newFunction in binaryFunctions and newFunction != currentFunction:
                        break
        return offspring


    def geneticProgrammingAlgorithm(self, dataset, labels, popSize, replaceP, tP, mutation, epsilon):
        dataset = [row + constants for row in dataset]
        output = open(self._problem.getOutputPath(), 'w')
        seed(None)
    
        print('GP Algorithm has started')
        output.write('GP Algorithm has started\n')
        individuals = [Chromosome(DEPTH_MAX, terminals, functions, constants) for _ in range(popSize)]
        for individual in individuals:
            individual.computeFitness(dataset=dataset, labels=labels)
        bestIndividual = None
        tournamentSize = int(floor(popSize * tP))
        popReplace = int(floor(popSize * replaceP))
    
        betterFitness = lambda i1, i2: i1 if i1.fitness < i2.fitness else i2
    
        epochIndex = 0
        while bestIndividual is None or bestIndividual.accuracy < epsilon:
            print(f'Start Epoch {epochIndex+1}')
            output.write(f'Start Epoch {epochIndex+1}\n')
    
            probDistribution = [max(ind.fitness for ind in individuals) - ind.fitness for ind in individuals]
            if sum(probDistribution) != 1:
                probDistribution = [1/len(probDistribution) for p in probDistribution]
            else:
                probDistribution = [p / sum(probDistribution) for p in probDistribution]
            offsprings = []
            for i in range(popReplace):
                selected = list(choice(individuals, size=tournamentSize, replace=False, p=probDistribution))
                selected += list(choice(individuals, size=tournamentSize, replace=False, p=probDistribution))
    
                firstParent = reduce(betterFitness, selected[:tournamentSize])
                secondParent = reduce(betterFitness, selected[tournamentSize:])
    
                offspring = self.crossover(firstParent, secondParent)
                if random() < mutation:
                    offspring = self.mutation(offspring)
    
                offsprings.append(offspring)
            print('Offsprings generated')
            output.write('Offsprings generated\n')
    
            for offspring in offsprings:
                offspring.computeFitness(dataset=dataset, labels=labels)
            individuals += offsprings
            print('Fitness offspring has been calculated')
            output.write('Fitness offspring has been calculated\n')
    
            individuals.sort(key=lambda indiv: indiv.fitness)
            individuals = individuals[:popSize]
    
            if bestIndividual is None or bestIndividual.accuracy < individuals[0].accuracy:
                bestIndividual = individuals[0]
    
            print(f'Best individual(fitness + accuracy) {bestIndividual.fitness} {bestIndividual.accuracy} vs {epsilon}')
            print('*******************')
            output.write(f'Best individual(fitness + accuracy) {bestIndividual.fitness} {bestIndividual.accuracy} vs {epsilon}\n')
            output.write('*******************\n')
            epochIndex += 1
    
        print(str(bestIndividual))
        print(f'{bestIndividual.fitness}, {bestIndividual.accuracy}')
        output.write(str(bestIndividual) + '\n')
        output.write(f'{bestIndividual.fitness}, {bestIndividual.accuracy}\n')
        
        output.close()
        
        