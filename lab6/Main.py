# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:20:34 2020

@author: Vasilica
"""
from Problem import Problem
from Controller import Controller 

def main():
    p = Problem("balance-scale.data")
    c = Controller(p)
    prob = 0.9
    c.solve(prob)
    
main()