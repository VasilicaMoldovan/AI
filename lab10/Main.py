# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:33:04 2020

@author: Vasilica
"""
from Problem import Problem
from Controller import Controller 

def main():
    problem = Problem("temperature.in", "humidity.in", "rules.in")
    c = Controller(problem)
    c.solveFuzzy()
    c.solveFuzzy()
    c.solveFuzzy()
    c.solveFuzzy()
    
main()