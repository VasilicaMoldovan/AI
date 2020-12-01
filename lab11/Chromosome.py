import math
from math import sin, cos
from random import random, randint
from typing import List, Tuple


class Chromosome:

    def __init__(self, maximumDepth, terminals, functions, constants):
        self._constants = constants
        self._maximumDepth = maximumDepth
        self._terminals = terminals
        self._functions = functions
        self._representation = [0 for _ in range(2 ** (self._maximumDepth + 1) - 1)]
        self._fitness = 0
        self._accuracy = 0
        self._size = 0
        self.growExpression()
        self._representation = [x for x in self._representation if x != 0]

    def getTerminalNodeByIndex(self, pos):
        return self._terminals[self._representation[pos] - 1]

    def getFunctionByIndex(self, pos):
        return self._functions[-self._representation[pos] - 1]

    def growExpression(self, pos=0, depth=0):
        if pos == 0 or depth < self._maximumDepth:
            if pos != 0 and random() < 0.4:
                self._representation[pos] = randint(1, len(self._terminals))
                self._size = pos + 1
                return pos + 1
            else:
                self._representation[pos] = -randint(1, len(self._functions))
                if self._functions[-self._representation[pos] - 1] in ['sin', 'cos']:
                    childEndIndex = self.growExpression(pos + 1, depth + 1)
                    return childEndIndex
                else:
                    firstChildEndIndex = self.growExpression(pos + 1, depth + 1)
                    secondChildEndIndex = self.growExpression(firstChildEndIndex, depth + 1)
                    return secondChildEndIndex
        else:
            self._representation[pos] = randint(1, len(self._terminals))
            self._size = pos + 1
            return pos + 1

    def evaluateExpression(self, pos, dataRow):
        pos = min(pos, len(self._representation) - 1)
        if self._representation[pos] > 0:
            #Terminal
            #print(dataRow)
            #print(self._representation[pos] - 1)
            return dataRow[self._representation[pos] - 1], pos
        elif self._representation[pos] < 0:
            # Function
            nodeFunction = self.getFunctionByIndex(pos)
            if nodeFunction == '+':
                auxFirst = self.evaluateExpression(pos + 1, dataRow)
                auxSecond = self.evaluateExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] + auxSecond[0], auxSecond[1]
            elif nodeFunction == '-':
                auxFirst = self.evaluateExpression(pos + 1, dataRow)
                auxSecond = self.evaluateExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] - auxSecond[0], auxSecond[1]
            elif nodeFunction == '*':
                auxFirst = self.evaluateExpression(pos + 1, dataRow)
                auxSecond = self.evaluateExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] * auxSecond[0], auxSecond[1]
            elif nodeFunction == 'sin':
                aux = self.evaluateExpression(pos + 1, dataRow)
                return sin(aux[0]), aux[1]
            elif nodeFunction == 'cos':
                aux = self.evaluateExpression(pos + 1, dataRow)
                return cos(aux[0]), aux[1]

    def calculateOutputClass(self, dataRow):
            output = self.evaluateExpression(0, dataRow)[0]
            if output < 2:
                return 1
            if output < 4:
                return 2
            if output < 6:
                return 3
            if output < 8:
                return 4
            return 5
        
    def computeFitness(self, dataset, labels):
        totalError = 0.0
        correct, total = 0, 0
        nExamples = len(dataset)
        for index in range(nExamples):
            error = abs(labels[index] - self.calculateOutputClass(dataRow=dataset[index]))
            totalError += error
            if error == 0:
                correct += 1
            total += 1
        accuracy = correct / total
        self._fitness = totalError
        self._accuracy = accuracy

    def traverse(self, pos):
        if self._representation[pos] > 0:  # terminal
            return min(pos + 1, len(self._representation) - 1)
        else:
            return self.traverse(self.traverse(pos + 1))

    def __getitem__(self, key):
        return self._representation[key]

    def __setitem__(self, key, value):
        self._representation[key] = value

    @property
    def representation(self):
        return self._representation

    @representation.setter
    def representation(self, value):
        self._representation = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def fitness(self):
        return self._fitness

    @property
    def accuracy(self):
        return self._accuracy

    def __str__(self):
        strRepr = ''
        for pos in range(len(self._representation)):
            if self._representation[pos] < 0:
                strRepr += self.getFunctionByIndex(pos) + ' '
            else:
                strRepr += self.getTerminalNodeByIndex(pos) + ' '
        return strRepr