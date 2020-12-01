# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:34:25 2020

@author: Vasilica
"""
from Ant import Ant

class Controller:
    def __init__(self, noOfAnts, size, noOfIterations):
        self.__size = size
        self.__trace = [[]]
        self.__noOfAnts = noOfAnts
        self.__population = [ Ant(self.__size) for x in range(0, noOfAnts) ]
        self.__noOfIterations = noOfIterations
        self.__alpha = 1.9
        self.__beta = 0.9
        self.__rho = 0.05
        self.__q0 = 0.5
        
    def iteration(self):
        antSet = [Ant(self.__size) for i in range(self.__noOfAnts)]
        for i in range(2 * self.__size):
            for x in antSet:
                x.addMove(self.__q0, self.__trace, self.__alpha, self.__beta)
                
        dTrace = []
        for i in range(len(antSet)):
            eval = antSet[i].evaluate()
            if eval == 0:
                dTrace.append(100)
            else:
                dTrace.append(1.0 / eval)
        for i in range(2 * self.__size):
            for j in range (2 * self.__size):
                self.__trace[i][j] = (1 - self.__rho) * self.__trace[i][j]
                
        for i in range(len(antSet)):
            for j in range(len(antSet[i].getPath())-1):
                x = antSet[i].getPath()[j]
                y = antSet[i].getPath()[j+1]
                for k in range(len(x)):
                    for l in range(len(y)):
                        self.__trace[k][l] = self.__trace[k][l] + dTrace[i]
        
        f = [ [antSet[i].evaluate(), i] for i in range(len(antSet))]
        f = max(f)
        
        return (antSet[f[1]].getPath(), f)
    
    def runAlgorithm(self):
        sol=[]
        bestSol=[]
        f = 0
        n = 2 * self.__size
        self.__trace = [[1 for i in range(n)] for j in range (n)]
        print("The program has started")
        
        for i in range(self.__noOfIterations):
            aux = self.iteration()
            sol = aux[0].copy()
            print(i)
            if len(sol[0]) > len(bestSol):
                bestSol = sol.copy()
                f = aux[1]
                
        return (bestSol[:n], f)
'''    
def main():
    c = Controller(5, 4, 100)
    print(c.runAlgorithm())
    
main()
'''