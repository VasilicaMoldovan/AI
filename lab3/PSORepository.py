# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:42:24 2020

@author: Vasilica
"""


from random import randint, random
from Entity import Particle

class PSO:
    def __init__(self, n, nrOfParticles, noOfIterations, firstSet, secondSet, w, c1, c2, sizeOfNeighborhood):
        self.__n = n 
        self.__nrOfParticles = nrOfParticles
        self.__noOfIterations =  noOfIterations
        self.__firstSet = firstSet
        self.__secondSet = secondSet
        self.__w = w
        self.__c1 = c1
        self.__c2 = c2
        self.__sizeOfNeighborhood = sizeOfNeighborhood
        
    def population(self):
        """
        Create a number of particles (i.e. a population).
    
        input --
           count: the number of individuals in the population
           l: the number of values in the pozition of a particle
           vmin: the minimum possible value 
           vmax: the maximum possible value
    
        output --
           the random created population of count particles
        """
        return [ Particle(self.__n, self.__firstSet, self.__secondSet) for x in range(self.__nrOfParticles) ]
    
    
    def selectNeighbors(self, pop, nSize):
        """  the selection of the neighbours for each particle
        
        input --
           pop: current population
           nSize: the number of neighbours of a particle
    
        output--
           ln: list of neighblours for each particle
        """
    
        if ( nSize >len(pop)):
            nSize = len(pop)
    
        # Attention if nSize==len(pop) this selection is not a propper one
        # use a different approach (like surfle to form a permutation)
        neighbors=[]
        for i in range(len(pop)):
            localNeighbor=[]
            for j in range(nSize):
                x = pop[i]
                aux = i
                while (x in localNeighbor):
                    aux  = randint(0, len(pop) - 1)
                    x = pop[aux]
                localNeighbor.append(aux)
            neighbors.append(localNeighbor.copy())
            
        return neighbors
    
    def difference(self, pop1, pop2):
        diff = 0
        for i in range(0, len(pop1)):
            if pop1[i] != pop2[i]:
                    diff += 1
        return diff 
    
    def add(self, position, velocity):
        for i in range(0, len(position)):
            if (position[i] + velocity < len(position)):
                position[i] += int(velocity)
                
        return position 
    
    def iteration(self, pop, neighbors, c1, c2, w ):
        """
        an iteration
    
        pop: the current state of the population
        
    
        for each particle we update the velocity and the position
        according to the particle's memory and the best neighbor's pozition 
        """
        bestNeighbors=[]
        #determine the best neighbor for each particle
        for i in range(len(pop)):
            bestNeighbors.append(neighbors[i][0])
            for j in range(1,len(neighbors[i])):
                if (pop[bestNeighbors[i]].fitness > pop[neighbors[i][j]].fitness):
                    bestNeighbors[i] = neighbors[i][j]
                    
        #update the velocity for each particle
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity)):
                newVelocity = w * pop[i].velocity[j]
                newVelocity += newVelocity + c1*random()*(self.difference(pop[bestNeighbors[i]].position[j], pop[i].position[j]))    
                newVelocity += newVelocity + c2*random()*(self.difference(pop[i].bestPosition[j], pop[i].position[j]))
                pop[i].velocity[j] = newVelocity
        
        #update the pozition for each particle
        for i in range(len(pop)):
            newPosition=[]
            for j in range(len(pop[0].position)):
                if j < len(pop[0].velocity):
                    newPosition.append(self.add(pop[i].position[j], pop[i].velocity[j]))
                else:
                    newPosition.append(pop[i].position[j])
            pop[i].position=newPosition
        return pop
    
    def solve(self, pop):
        neighborhoods = self.selectNeighbors(pop, self.__sizeOfNeighborhood)
        for i in range(self.__noOfIterations):
            pop = self.iteration(pop, neighborhoods, self.__c1, self.__c2, self.__w/(i+1))
    
        best = 0
        for i in range(1, len(pop)):
            if (pop[i].fitness < pop[best].fitness):
                best = i
        
        fitnessOptim = pop[best].fitness
        individualOptim = pop[best].position
        
        return (fitnessOptim, individualOptim)
        
        
'''    
def main():
        #PARAMETERS:
        noIteratii=100
        #number of particles
        noParticles = 100
        #individual size
        dimParticle = 3
        #the boundries of the search interval
        firstSet = [1, 2, 3]
        secondSet = [1, 2, 3]
        #specific parameters for PSO
        w=1.0
        c1=1.
        c2=2.5
        sizeOfNeighborhood=20
        pso = PSO(dimParticle, noParticles, noIteratii, firstSet, secondSet, w, c1, c2, sizeOfNeighborhood)
        P = pso.population()
        
        sol = pso.solve(P)
        print(sol[1])
        print(sol[0])        
        
main()
'''