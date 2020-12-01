# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:44:20 2020

@author: Vasilica
"""
import numpy as np
import math

#def generateValues():
#    values = np.geomspace(0, 16, 26)
#    return values

#def makeInt(array, size):
#    newArray = []
#    for i in range(0, size):
#        newArray.append(int(array[i]))
#    return newArray

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
        
    
    
def main():
    #dict = {'A':10, 'B':5, 'C':3, 'D':6}
    #sum = "AAD"
    #result = [0, 0, 0, 10, 10, 6]
    #print(check(sum, result, dict))
    while True:
        attempts = int(input("Give number of attempts: "))
        if attempts == 0:
            return
        solveCryptarithmetic(attempts)
        
    
    
main()