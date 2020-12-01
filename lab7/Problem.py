# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:25:25 2020

@author: Vasilica
"""


class Problem:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.readFromFile()
        
    def readFromFile(self):
        self.__x = []
        self.__y = []
        file = open(self.__fileName, 'r')
        line = file.readline()
        while line != "" and line != None:
            values = line.split(" ")
            x_aux = []
            for i in range(5):
                x_aux.append(float(values[i]))
            self.__x.append(x_aux)
            self.__y.append(float(values[5]))
            line = file.readline()
            line = file.readline()
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
'''
def main():
    p = Problem("database.txt")
    print(p.getX())
    print("lala")
    print(p.getY())

main()    
'''