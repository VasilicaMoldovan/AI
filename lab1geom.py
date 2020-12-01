# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:54:39 2020

@author: Vasilica
"""


import numpy as np
import math
import copy

def readForms():
    file = open("file2.txt", 'r')
    matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    forms = []
    for i in range(0, 5):
        for j in range(0, 6):
            read = file.readline().strip().split()
            matrix[i][j] = read
        
        read = file.readline()
            
    return matrix

def generateCoordinates():
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 6)
    return (i, j)

def isValid(matrix, coordinates):
    i = coordinates[0]
    j = coordinates[1]
    firstC = getFirstCoordinates(matrix)
    i1 = firstC[0]
    j1 = firstC[1]
    valid = True
    
    if j < j1 and  j1 - getLeftCorner(matrix) > abs(j - getLeftCorner(matrix)):
        valid = False
    
    #if j + getRightCorner(matrix) - getLeftCorner(matrix) + 1 > 0:
    #    valid = False
    else:
        while (i < 6 and i1 < 6):
            j = coordinates[1]
            j1 = firstC[1]
            while (j < 5 and j1 < 5):
                j += 1
                j1 += 1
            while ( j1 < 5):
                if ( j == 5 and j1 < 5 and matrix[i1][j1] == '1'):
                    valid = False
                    break
                else:
                    j1 +=1 
            i += 1
            i1 += 1
                    
        while (i1 < 6):
            for j1 in range(0, 5):
                if ( i == 6 and i1 < 6 and matrix[i1][j1] == '1'):
                    valid = False
                    break
            i1 += 1
            
    return valid
            
def getFirstCoordinates(matrix):
    i = 0
    j = 0
    found  = False
    while (i < 6):
        j = 0
        while (j < 5):
            if (matrix[i][j] == '1'):
                return (i, j)
            else:
                j += 1
        i += 1
    return (i, j)    

def getLeftCorner(matrix):
    j = 0
    i = 0
    while j < 5:
        i = 0
        while i < 6:
            if matrix[i][j] == '1':
                return j
            i += 1
        j += 1
        
    return -1

def getRightCorner(matrix):
    j = 4
    i = 0
    while j < 5:
        i = 0
        while i < 6:
            if matrix[i][j] == '1':
                return j
            i += 1
        j += 1
        
    return -1
    

def doNotOverlap(copy1, matrix, coordinates):
     i = coordinates[0]
     j = coordinates[1]
     firstC = getFirstCoordinates(matrix)
     i1 = firstC[0]
     j1 = firstC[1]
     while (i < 6 and i1 < 6):
         j = coordinates[1]
         j1 = firstC[1]
         while (j < 5 and j1 < 5):
             copy1[i][j] += int(matrix[i1][j1])
             j += 1
             j1 += 1
         i += 1
         j += 1
         
     overlap = True
     for i in range(0, 6):
         for j in range(0, 5):
             if copy1[i][j] > 1:
                 overlap = False
                 break
                     
     return overlap

def checkArrangement(matrix):
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    i = 0
    invalid = False 
    while (i < 5 and invalid == False):
        coordinates = generateCoordinates()
        if isValid(matrix[i], coordinates) == True and doNotOverlap(copy.deepcopy(board), matrix[i], coordinates) == True:
            i1 = coordinates[0]
            j1 = coordinates[1]
            firstC = getFirstCoordinates(matrix[i])
            i2 = firstC[0]
            j2 = firstC[1]
            while (i1 < 6 and i2 < 6):
                j1 = coordinates[1]
                j2 = firstC[1]
                while (j1 < 5 and j2 < 5):
                    if (board[i1][j1] == 0):
                        board[i1][j1] = int(matrix[i][i2][j2])
                    j1 += 1
                    j2 += 1
                i1 += 1
                i2 += 1
            i += 1
        else:
            invalid = True
    if invalid == True:
        return -1
    return board

def main():
    while True:
        attempts = int(input("Give number of attempts: "))
        matrix = readForms()
        #board = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        if attempts == 0:
            return 
        else:
            #print(isValid(matrix[4], (2, 1)))
            for i in range(0, attempts):
                checked = checkArrangement(matrix)
                if checked != -1:
                   print(checked)
                   break 

main()