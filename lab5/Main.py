# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:15:45 2020

@author: Vasilica
"""

from Controller import Controller
from Problem import Problem 
from Validator import Validator

def main():
    p = Problem()
    controller = Controller(15, p.getSize(), 100)
    
    permSolution = controller.runAlgorithm()
    finalSolution = p.giveFinalSolution(permSolution[0])
    
    validator = Validator(1000, 30, 40)
    validator.plotACO
    
    for i in range(len(finalSolution)):
        print(finalSolution[i])
    
main()
    