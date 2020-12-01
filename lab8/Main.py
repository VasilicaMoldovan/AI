# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:58:04 2020

@author: Vasilica
"""


from Controller import Controller

def main():
    controller = Controller("database.txt")
    controller.solve()
    
main()