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

def makeInt(array, size):
    newArray = []
    for i in range(0, size):
        newArray.append(int(array[i]))
    return newArray

def readFromFile():
    file = open("file1.txt", 'r')
    firstWord = file.readline()
    secondWord = file.readline()
    result = file.readline()
    sign = firstWord[len(firstWord) - 2]
    return [firstWord, secondWord, result, sign]
    

def generateValues(firstWord, secondWord, result):
    dict = {}
    for i in range(0, len(firstWord) - 2):
        if i == 0:
            dict[firstWord[i]] = np.random.randint(1, 16)
        else:
            dict[firstWord[i]] = np.random.randint(0, 16)
    for i in range(0, len(secondWord) - 2):
        if secondWord[i] in dict and i == 0 and dict[secondWord[i]] == 0:
            dict[secondWord[i]] = np.random.randint(1, 16)
        if secondWord[i] not in dict:
            if i == 0:
                dict[secondWord[i]] = np.random.randint(1, 16)
            else:
                dict[secondWord[i]] = np.random.randint(0, 16)
            
    
    for i in range(0, len(result)):
        if result[i] in dict and i == 0 and dict[result[i]] == 0:
            dict[result[i]] = np.random.randint(1, 16)
        if result[i] not in dict:
            if i == 0:
                dict[result[i]] = np.random.randint(1, 16)
            else:
                dict[result[i]] = np.random.randint(0, 16)
    return dict
            
def compute(firstWord, secondWord, sign, dict):
    m = max(len(firstWord), len(secondWord))
    result = []
    for i in range(0, m + 1):
        result.append(0)
    b = 0
    index = m
    i = len(firstWord) - 3
    j = len(secondWord) - 3
    if sign == '+':
        while(i >= 0 and j >= 0):
            if dict[firstWord[i]] + dict[secondWord[j]] > 15:
                result[index] += (dict[firstWord[i]] + dict[secondWord[j]] - 16)
                result[index] += b
                b = (dict[firstWord[i]] + dict[secondWord[j]]) // 16
            else:
                result[index] += (dict[firstWord[i]] + dict[secondWord[j]])
                result[index] += b
                b = 0
            i -= 1
            j -= 1
            index -= 1
            
        while(i >= 0):
            result[index] += dict[firstWord[i]]
            result[index] += b
            b = 0
            i -= 1 
            index -= 1
            
        while(j >= 0):
            result[index] += dict[secondWord[j]]
            result[index] += b
            b = 0
            j -= 1 
            index -= 1
        
        if (i < 0 and j < 0 and b == 1):
            result[index] += 1
    else:
        b = 0
        while(i >= 0 and j >= 0):
            if dict[firstWord[i]] - dict[secondWord[j]] < 0:
                result[index] += (dict[firstWord[i]] + 16 - dict[secondWord[j]])
                b = 1
                result[index - 1] -= b 
            else:
                result[index] += (dict[firstWord[i]] - dict[secondWord[j]])
                b = 0
                result[index - 1] -= b
            i -= 1
            j -= 1
            index -= 1
            
        while(i >= 0):
            result[index] += firstWord[i]
            b = 0
            result[index] -= b
            i -= 1 
            index -= 1
            
        while(j >= 0):
            result[index] -= secondWord[j]
            b = 0
            result[index] -= b
            j -= 1 
            index -= 1
        
        if (i < 0 and j < 0 and b == 1):
            result[index] -= 1
    
    return result

def check(result, sum, dict):
    i = 0
    j = 0
    while (i < len(sum) and sum[i] == 0):
        i += 1
        
    while (i < len(sum) and j < len(result)):
        #print(sum[i])
        #print(result[j])
        #print(dict[result[j]])
        if (sum[i] != dict[result[j]]):
            return False
        else:
            i += 1
            j += 1
    if (i < len(sum) or j < len(result)):
        return False
    return True

def solveCryptarithmetic(attempts):
    read = readFromFile()
    i = 0
    found = False
    while (i < attempts and found == False):
         dict = generateValues(read[0], read[1], read[2])
         if check(read[2], compute(read[0], read[1], read[3], dict), dict) == True:
             print(dict)
             print(compute(read[0], read[1], read[3], dict))
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