# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:34:04 2020

@author: Vasilica
"""
import random
import itertools

class Ant:
    def __init__(self, n):
        self.__size = n * 2
        self.__length = n
        self.__individ = self.individual()
        i = random.randint(0, self.__size-1)
        self.__path = [self.__individ[i]]
        
    def getPath(self):
        return self.__path
    
    def setPath(self, newPath):
        self.__path = newPath
        
    def individual(self):
        set = list(range(0, self.__length)) 
        perm = list(itertools.permutations(set))
        random.shuffle(perm)
        n = 2 * self.__length
        perm = perm[:n]
        
        return perm
    
    def nextMoves(self):
        new = []
        perm = self.individual()
        
        for i in range(len(perm)):
            self.__path.append(perm[i])
            
            if self.evaluate() == 0:
                new.append(perm[i])
                
            self.__path.pop()
            
        return new.copy()
    
    def distMove(self, a):
        self.__path.append(a)
        aux = int(self.__length)
        return abs(aux - len(self.nextMoves()))
    
    def evaluate(self):
        fitness = 0
        length = min(len(self.__path), self.__length)
        
        for k in range(length):
            for i in range(self.__length):
                for j in range(i + 1, self.__length):
                    if self.__path[k][i] == self.__path[k][j]:
                        fitness += 1
           
        for k in range(self.__length):
            for i in range(length):
                for j in range(i + 1, length):
                    if self.__path[i][k] == self.__path[j][k]:
                        fitness += 1
                        
        if length == self.__length:
            for k in range(self.__length):
                for i in range(self.__length, len(self.__path)):
                    for j in range(i + 1, len(self.__path)):
                        if self.__path[i][k] == self.__path[j][k]:
                            fitness += 1
            
        return fitness
    
    def addMove(self, q0, trace, alpha, beta):
        p = [1 for i in range(self.__size)]
        nextSteps = self.nextMoves().copy()
        perm = self.individual()
        if (len(nextSteps) == 0):
            return False
        l = 0
        for i in nextSteps:
            p[l] = self.distMove(i)
            l += 1
        p=[ (p[i]**beta)*(trace[self.__path[-1][-1]][i]**alpha) for i in range(len(p))]
        
        if (random.random() < q0):
            p = [ [i, p[i]] for i in range(len(p)) ]
            p = max(p, key=lambda a: a[1])
            self.__path.append(perm[p[0]])
        else:
            s = sum(p)
            p = [ p[i]/s for i in range(len(p)) ]
            p = [ sum(p[0:i+1]) for i in range(len(p)) ]
            r = random.random()
            i=0
            while (r > p[i]):
                i += 1
            self.__path.append(perm[i])
'''
             
def main():
    matrix = [[1,2,3],[2,3,1],[3,1,2],[1,3,2],[2,1,3],[3,2,1]]
    ant = Ant(3)
    #i = ant.individual()
    #print(i)
    print(ant.getPath())
    print(ant.evaluate())
    print(ant.nextMoves())
    
main()         
'''    
        
        
        
        
        
        