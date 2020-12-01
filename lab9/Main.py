# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:23:05 2020

@author: Vasilica
"""
from Problem import Problem
from CNNController import CNNController

def main():
    p = Problem()
    c = CNNController(p)
    c.solve()
    
main()