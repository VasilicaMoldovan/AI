# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:19:25 2020

@author: Vasilica
"""
import numpy as np
import math
import copy

''' 
Sudoku Game
'''

array = [[], [], [], [], [], [], [], [], [] ]

def generateRandomNumbers(lowerBound, upperBound):
   #g = np.geomspace(lowerBound, upperBound, 1)
   #return int(g)
   u = np.random.randint(lowerBound, upperBound)
   return int(u)

def generateBoard(aux, size):
    for i in range(0, size):
        for j in range(0, size):
            if aux[i][j] == '-':
                aux[i][j] = int(generateRandomNumbers(1, size + 1))
                

def checkSudokuRow(aux, row, size):
    auxSet = set()
    for i in range(0, size):
        if int(aux[row][i]) in auxSet:
            return False
        else:
            auxSet.add(int(aux[row][i]))
    return True

def checkSudokuColumn(aux, column, size):
    auxSet = set()
    for i in range(0, size):
        if int(aux[i][column]) in auxSet:
            return False
        else:
            auxSet.add(int(aux[i][column]))
            
    return True
        
def checkSudokuBox(aux, startRow, startColumn, size):
    auxSet = set()
    stop = int(math.sqrt(size))
    for row in range(0, stop):
        for column in range(0, stop):
            current = aux[row + startRow][column + startColumn]
            if current in auxSet:
                return False
            else:
                auxSet.add(current)
                
    return True

def validSudoku(aux, row, column, size):
    return (checkSudokuRow(aux, row, size) and checkSudokuColumn(aux, column, size) and
           checkSudokuBox(aux, row - row % (int(math.sqrt(size))), column - column % (int(math.sqrt(size))), size))
    
def checkSudoku(aux, size):
    for i in range(0, size):
        for j in range(0, size):
            if not validSudoku(aux, i, j, size):
                return False
    return True

def readSudokuBoard():
    file = open("file.txt", 'r')
    size = int(file.readline())
    for i in range(0, size):
        line = file.readline().split()
        array[i] = line
    return (size, array)

def printBoard(array, size):
    for i in range(0, size):
        print(array[i])
        

def sudokuSolution(size, attempts):
    for i in range(0, attempts):
        aux = copy.deepcopy(array)
        generateBoard(aux, size)
        if checkSudoku(aux, size) == True:
            printBoard(aux, size)
            break
        
'''
Cryptarithmetic Game
'''        
def readFromFile():
    file = open("file1.txt", 'r')
    read = file.readlines()
    array = []
    if "+" in read[0]:
        sign = '+'
    else:
        sign = '-'
    for line in read:
        array.append(line.strip().split("+="))
    return [array, sign]
    

def generateValues(array):
    dict = {}
    for j in range(0, len(array) - 1):
        for i in range(0, len(array[j][0]) - 1):
            if array[j][0][i] in dict and i == 0 and dict[array[j][0][i]] == 0:
                dict[array[j][0][i]] = np.random.randint(1, 16)
            if array[j][0][i] not in dict:
                if i == 0:
                    dict[array[j][0][i]] = np.random.randint(1, 16)
                else:
                    dict[array[j][0][i]] = np.random.randint(0, 16)
            
    result = array[len(array) - 1]
    for i in range(0, len(result[0])):
        if result[0][i] in dict and i == 0 and dict[result[0][i]] == 0:
            dict[result[0][i]] = np.random.randint(1, 16)
        if result[0][i] not in dict:
            if i == 0:
                dict[result[0][i]] = np.random.randint(1, 16)
            else:
                dict[result[0][i]] = np.random.randint(0, 16)
    return dict
            
def check(result, sum, dict):
    i = 0
    j = 0
    while (i < len(sum) and sum[i] == 0):
        i += 1
        
    while (i < len(sum) and j < len(result[0])):
        if (sum[i] != dict[result[0][j]]):
            return False
        else:
            i += 1
            j += 1
            
    if (i < len(sum) or j < len(result[0])):
        return False
    return True

def computeMoreThan3(partialResult, word, sign, dict):
    m = max(len(partialResult), len(word))
    result = []
    for i in range(0, m + 1):
        result.append(0)
    b = 0
    index = m
    i = len(partialResult) - 1
    j = len(word) - 2
    if sign == '+':
        while(i >= 0 and j >= 0):
            if partialResult[i] + dict[word[j]] > 15:
                result[index] += (partialResult[i] + dict[word[j]] - 16)
                result[index] += b
                b = 1
            else:
                result[index] += (partialResult[i] + dict[word[j]])
                result[index] += b
                b = 0
            i -= 1
            j -= 1
            index -= 1
            
        while(i >= 0):
            result[index] += partialResult[i]
            result[index] += b
            b = 0
            i -= 1 
            index -= 1
            
        while(j >= 0):
            result[index] += dict[word[j]]
            result[index] += b
            b = 0
            j -= 1 
            index -= 1
        
        if (i < 0 and j < 0 and b == 1):
            result[index] += 1
    else:
        b = 0
        while(i >= 0 and j >= 0):
            if partialResult[i] - dict[word[j]] < 0:
                result[index] += (partialResult[i] + 16 - dict[word[j]])
                b = 1
                result[index - 1] -= b 
            else:
                result[index] += (partialResult[i] - dict[word[j]])
                b = 0
                result[index - 1] -= b
            i -= 1
            j -= 1
            index -= 1
            
        while(i >= 0):
            result[index] += partialResult[i]
            b = 0
            result[index] -= b
            i -= 1 
            index -= 1
            
        while(j >= 0):
            result[index] -= dict[word[j]]
            b = 0
            result[index] -= b
            j -= 1 
            index -= 1
        
        if (i < 0 and j < 0 and b == 1):
            result[index] -= 1
    
    return result
    

def solveGame(array, dict, sign):
    result = getList(array[0][0], dict)
    for i in range(1, len(array) - 1):
        result = computeMoreThan3(result, array[i][0], sign, dict)
    return result

def getList(word, dict):
    result = []
    for i in range(0, len(word) - 1):
        result.append(dict[word[i]])
    return result
    
        
def solveCryptarithmetic(attempts):
    read = readFromFile()
    i = 0
    found = False
    while (i < attempts and found == False):
         dict = generateValues(read[0])
         if check(read[0][len(read[0]) - 1], solveGame(read[0], dict, read[1]), dict) == True:
             print(dict)
             print(solveGame(read[0], dict, read[1]))
             found = True
         else:
             i += 1

''' 
Geometric Forms
'''
def readForms():
    file = open("file2.txt", 'r')
    matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
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
    invalid = False 
    list = [0, 1, 2, 3, 4]
    np.random.shuffle(list)
    for i in list:
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
        else:
            invalid = True
            break
        
    if invalid == True:
        return -1
    return board


def main():
   while True:
       print("Menu")
       print("1.Sudoku")
       print("2.Cryptarithmetic Game")
       print("3.Geometric Forms")
       print("0.Exit")
       command = int(input("Choose problem: "))
       attempts = int(input("Give maximum number of attempts: "))
       if command == 0:
           return
       elif command == 1:
           read = readSudokuBoard()
           size = read[0]
           sudokuSolution(size, attempts)
       elif command == 2:
            solveCryptarithmetic(attempts)
       elif command == 3:
           matrix = readForms()
           for i in range(0, attempts):
               checked = checkArrangement(matrix)
               if checked != -1:
                   print(checked)
                   break 
       
main()