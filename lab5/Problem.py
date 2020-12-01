# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:34:18 2020

@author: Vasilica
"""


class Problem:
    def __init__(self):
        self.readFromFile()
        
    def giveFinalSolution(self, permSol):
        solution = []
        
        for i in range(self.__size):
            row = []
            for j in range(self.__size):
                if len(permSol) > i + self.__size:
                    row.append((self.__firstSet[permSol[i][j]], self.__secondSet[permSol[i + self.__size][j]]))
                else:
                    row.append((self.__firstSet[permSol[i][j]], -1))
                    
            solution.append(row)
            
        return solution
    
    def readFromFile(self):
        file = open("file.txt", 'r')
        self.__size =  int(file.readline())
        self.__firstSet = file.readline().rstrip().split(",");
        self.__secondSet = file.readline().rstrip().split(",");
        
    def getSize(self):
        return self.__size