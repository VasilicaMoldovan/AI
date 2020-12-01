# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:36:43 2020

@author: Vasilica
"""

from Problem import Problem
from Controller import Controller
from random import seed

def main():
    seed(6)
    fileName = 'database.txt'
    p = Problem(fileName)
    
    n_folds = 5
    l_rate = 0.01
    n_epoch = 5
    p.prepareDataSet()
    dataset = p.getDataSet()
    c = Controller(p)
    sol = c.solveGradientDescent(dataset, c.regressionGradientDescent, n_folds, l_rate, n_epoch)
    scores = sol[0]
    print('Error: %.5f' % sol[1])
    
main()
