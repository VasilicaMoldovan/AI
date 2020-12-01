# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:23:59 2020

@author: Vasilica
"""

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QListView                                              
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QSize, QThread
from Entity import Entity
from PSORepository import PSO
from EARepository import EA
from HCMRepository import HillClimbing
import threading
     
class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(800, 600))    
        self.setWindowTitle("EA, Hill Climbing Method and PSO for Euler Square:") 
        
        centralWidget = QWidget(self)  
        self.setCentralWidget(centralWidget)  
        
        formLayout = QFormLayout(self)
        
        self.__mutationProbLineEdit = QLineEdit(self)
        self.__crossProbLineEdit = QLineEdit(self)
        self.__nrOfIndividualsLineEdit = QLineEdit(self)
        self.__nrOfIterationsLineEdit = QLineEdit(self)
        self.__neighborhoodSizeLineEdit = QLineEdit(self)
        self.__inertiaCoeffLineEdit = QLineEdit(self)
        self.__cognitiveCoeffLineEdit = QLineEdit(self)
        self.__socialCoeffLineEdit = QLineEdit(self)
        
        formLayout.addRow(self.tr("&Mutation Probability:"), self.__mutationProbLineEdit)
        formLayout.addRow(self.tr("&Crossover Probability:"), self.__crossProbLineEdit)
        formLayout.addRow(self.tr("&Population size:"), self.__nrOfIndividualsLineEdit)
        formLayout.addRow(self.tr("&Number of generations:"), self.__nrOfIterationsLineEdit)
        formLayout.addRow(self.tr("&Size of neighborhood:"), self.__neighborhoodSizeLineEdit)
        formLayout.addRow(self.tr("&Inertia Coefficient:"), self.__inertiaCoeffLineEdit)
        formLayout.addRow(self.tr("&Cognitive Learning Coefficient:"), self.__cognitiveCoeffLineEdit)
        formLayout.addRow(self.tr("&Social Learning Coefficient:"), self.__socialCoeffLineEdit)
        
        buttonGroup = QVBoxLayout(self)
        
        self.__eaButton = QPushButton("&Run EA", self)
        self.__hcButton = QPushButton("&Run Hill Climbing Method", self)
        self.__psoButton = QPushButton("&Run PSO", self)
        self.__stopButton = QPushButton("&Stop Execution", self)
        
        self.__eaButton.clicked.connect(self.runEA)
        self.__hcButton.clicked.connect(self.runHillClimbing)
        self.__psoButton.clicked.connect(self.runPSO)
        self.__stopButton.clicked.connect(self.stopCurrentThread)
        
        #self.__eaButton.clicked.connect(self.eaAlgorithm)
        #self.__hcButton.clicked.connect(self.hillClimbingAlgorithm)
        #self.__psoButton.clicked.connect(self.runPSO)
        
        buttonGroup.addWidget(self.__eaButton)
        buttonGroup.addWidget(self.__hcButton)
        buttonGroup.addWidget(self.__psoButton)
        buttonGroup.addWidget(self.__stopButton)
        
        self.__EAlistView = QListView(self)
        self.__HClistView = QListView(self)
        self.__PSOlistView = QListView(self)
        
        auxLayout = QGridLayout(self)
        auxLayout.addLayout(formLayout, 0, 0)
        auxLayout.addLayout(buttonGroup, 0, 1)
        auxLayout.addWidget(self.__EAlistView)
        auxLayout.addWidget(self.__HClistView)
        auxLayout.addWidget(self.__PSOlistView)
        
        centralWidget.setLayout(auxLayout)
        
        menu = self.menuBar().addMenu('Action for quit')
        action = menu.addAction('Quit')
        
        action.triggered.connect(QtWidgets.QApplication.quit)
        
    def stopCurrentThread(self):
        self.t1.exit(0)
        
    def createEntity(self):
        dimIndividual = 3
        firstSet = [1, 2, 3]
        secondSet = [1, 2, 3]
        entity = Entity(self.__nrOfIndividuals, self.__crossProb, self.__mutationProb, dimIndividual, firstSet, secondSet)
 
        return entity
    
    def runEA(self):
        #self.__thread = QThread()
        #self.__thread.started.connect(lambda: self.eaAlgorithm())
        self.t2 = threading.Thread(target=self.eaAlgorithm) 
        self.t2.start()
        self.t2.join()
        #self.eaAlgorithm()
        
    def eaAlgorithm(self):
        self.__nrOfIndividuals = int(self.__nrOfIndividualsLineEdit.text())
        self.__nrOfIterations = int(self.__nrOfIterationsLineEdit.text())
        self.__crossProb = float(self.__crossProbLineEdit.text())
        self.__mutationProb = float(self.__mutationProbLineEdit.text())
        self.__entity = self.createEntity()
        
        ea = EA(self.__nrOfIterations, self.__entity)
        P = self.__entity.population(self.__entity.getNrOfIndividuals(), self.__entity.getDimIndividual(), self.__entity.getFirstSet(), self.__entity.getSecondSet())
        model = QStandardItemModel(self);
        self.__EAlistView.setModel(model)
        
        for i in range(self.__nrOfIterations):
            iteration = ea.eaIteration(P, self.__entity.getCrossProb(), self.__entity.getMutationProb(), self.__entity.getFirstSet(), self.__entity.getSecondSet())
            P = iteration[0]
            f = iteration[1]
            string = "fitness: " + str(f) + "  " + str(P)
            print(string)
            item = QStandardItem(string)
            model.appendRow(item)
            
        graded = [ (self.__entity.fitness(x), x) for x in P]
        graded = sorted(graded, key=lambda x: x[0])
        result = graded[0]
        fitnessOptim = result[0]
        individualOptim = result[1]
        string = "Final Solution: "
        item = QStandardItem(string)
        model.appendRow(item)
        string = "fitness: " + str(fitnessOptim) + "  " + str(individualOptim)
        item = QStandardItem(string)
        model.appendRow(item)
            
        
    def hillClimbingAlgorithm(self):
        self.__nrOfIndividuals = int(self.__nrOfIndividualsLineEdit.text())
        self.__nrOfIterations = int(self.__nrOfIterationsLineEdit.text())
        self.__crossProb = float(self.__crossProbLineEdit.text())
        self.__mutationProb = float(self.__mutationProbLineEdit.text())
        self.__entity = self.createEntity()
        
        model = QStandardItemModel(self);
        self.__HClistView.setModel(model)
        
        hillClimb = HillClimbing(self.__nrOfIterations, self.__entity)
        result = hillClimb.hillClimbingMethod()
        
        string = "Final Solution: "
        item = QStandardItem(string)
        model.appendRow(item)
        string = "fitness: " + str(result[0]) + "  " + str(result[1])
        item = QStandardItem(string)
        model.appendRow(item)
        
        
    def runHillClimbing(self):
        self.t1 = threading.Thread(target=self.hillClimbingAlgorithm) 
        self.t1.start()
        self.t1.join()
        
    def psoAlgorithm(self):
        dimParticle = 3
        firstSet = [1, 2, 3]
        secondSet = [1, 2, 3]
        self.__nrOfIndividuals = int(self.__nrOfIndividualsLineEdit.text())
        self.__nrOfIterations = int(self.__nrOfIterationsLineEdit.text())
        self.__neighborhoodSize = int(self.__neighborhoodSizeLineEdit.text())
        self.__inertiaCoeff = float(self.__inertiaCoeffLineEdit.text())
        self.__cognitiveCoeff = float(self.__cognitiveCoeffLineEdit.text())
        self.__socialCoeff = float(self.__socialCoeffLineEdit.text())
        
        pso = PSO(dimParticle, self.__nrOfIndividuals, self.__nrOfIterations, firstSet, secondSet, self.__inertiaCoeff, self.__cognitiveCoeff, self.__socialCoeff, self.__neighborhoodSize)
        pop = pso.population()
        model = QStandardItemModel(self);
        self.__PSOlistView.setModel(model)
        
        neighborhoods = pso.selectNeighbors(pop, self.__neighborhoodSize)
        for i in range(self.__nrOfIterations):
            pop = pso.iteration(pop, neighborhoods, self.__cognitiveCoeff, self.__socialCoeff, self.__inertiaCoeff/(i+1))
    
        best = 0
        for i in range(1, len(pop)):
            string = "fitness: " + str(pop[i].fitness) + "  " + str(pop[i].position)
            item = QStandardItem(string)
            model.appendRow(item)
            if (pop[i].fitness < pop[best].fitness):
                best = i
        
        fitnessOptim = pop[best].fitness
        individualOptim = pop[best].position
        
        string = "Final Solution: "
        item = QStandardItem(string)
        model.appendRow(item)
        string = "fitness: " + str(fitnessOptim) + "  " + str(individualOptim)
        item = QStandardItem(string)
        model.appendRow(item)
    
    def runPSO(self):
        self.t2 = threading.Thread(target=self.psoAlgorithm) 
        self.t2.start()
        self.t2.join()
        
          
def run_app():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    app.exec_()
    
run_app()