# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:10:57 2020

@author: Vasilica
"""
from Problem import Problem
from Controller import Controller

def main():
    p = Problem('output.out', 'sensor_readings_24.data')
    dataset, labels = p.buildDataset()
    c = Controller(p)

    popSize = int(input("Population size: "))
    #popSize = 1000
    replaceP = float(input("Replacement percent: "))
    selection = float(input("Selection percent: "))
    mutation = float(input("Mutation percent: "))
    epsilon = float(input("Epsilon: "))
    #replaceP = 0.5
    #selection = 0.05
    #mutation = 0.2
    #epsilon = 0.62
    c.geneticProgrammingAlgorithm(dataset, labels, popSize, replaceP, selection, mutation, epsilon)
    
main()