# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:05:12 2020

@author: Vasilica
"""

from Node import Node
from Attribute import Attribute
from DecisionTree import DecisionTree
from Problem import Problem
import numpy as np

class Controller:
    def __init__(self, problem):
        self.__problem = problem 
    
    def classify(self, row, node):
        if isinstance(node, Node):
            return node.getClasses().most_common(1)[0][0]

        if node.getAttribute().compare(row):
            return self.classify(row, node.getGoodBranch())
        else:
            return self.classify(row, node.getFalseBranch())
        
    def giniIndex(self, rows):
        node = Node(rows)
        distr = node.getClasses()
        index = 1
        
        for i in distr:
            if len(rows) == 0:
                continue
            pi = distr[i] / float(len(rows))
            index -= pi**2
            
        return index
    
    def infoGain(self, firstPart, secondPart, currentInfo):
        p = float(len(firstPart)) / (len(firstPart) + len(secondPart))
        return currentInfo - p * self.giniIndex(firstPart) - (1 - p) * self.giniIndex(secondPart)

    def partition(self, rows, attribute):
        goodRows = [row for row in rows if attribute.compare(row)]
        falseRows = [row for row in rows if not attribute.compare(row)]
        return goodRows, falseRows


    def bestSplit(self, rows):
        bestGain = 0
        bestAttribute = None
        currentVal = self.giniIndex(rows)
        features = len(rows[0]) - 1  
    
        for f in range(features):
            values = set([row[f] for row in rows])
            for val in values:
                attribute = Attribute(f, val)
                goodRows, falseRows = self.partition(rows, attribute)
                if len(goodRows) == 0 or len(falseRows) == 0:
                    continue
                gain = self.infoGain(goodRows, falseRows, currentVal)
                if gain > bestGain:
                    bestGain = gain
                    bestAttribute = attribute
                    
        return bestGain, bestAttribute
    
    def buildTree(self, rows):
        gain, attribute = self.bestSplit(rows)

        if gain == 0:
            return Node(rows)

        goodRows, falseRows = self.partition(rows, attribute)
        goodBranch = self.buildTree(goodRows)
        falseBranch = self.buildTree(falseRows)
    
        return DecisionTree(attribute, goodBranch, falseBranch)

   
    def solve(self, p):
        dataset = self.__problem.readData()
        runs = 1000
        accuracy = []

        for i in range(runs):
            print(i)
            train, test = self.__problem.splitData(dataset, p)
            dTree = self.buildTree(train)
    
            correct, total = 0, 0
            for row in test:
                prediction = self.classify(row, dTree)
                actual = row[-1]
                if prediction == actual:
                    correct += 1 
                total += 1
    
            accuracy.append(correct/total)
            
        mean = np.mean(accuracy) * 100
        ma = np.max(accuracy) * 100
        mi = np.min(accuracy) * 100
    
        print("Max accuracy " + str(ma))
        print("Mean accuracy " + str(mean))
        print("Min accuracy " + str(mi))        