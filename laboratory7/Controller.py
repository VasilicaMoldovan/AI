# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:36:30 2020

@author: Vasilica
"""
from math import sqrt, isnan
from Problem import Problem
import numpy as np

class Controller:
    def __init__(self, problem):
        self.__problem = problem 
        
    def getError(self, actual, predicted):
    	sum_error = 0.0
    	for i in range(len(actual)):
            prediction_error = predicted[i] - actual[i]
            sum_error += abs(prediction_error)
    	mean_error = sum_error / float(len(actual))
    	return abs(mean_error)
    
    
    def solveGradientDescent(self, dataset, algorithm, n_folds, *args):
        folds = self.__problem.cross_validation_split(n_folds)
        #print(folds)
        scores = list()
        error = 0.0
        predicted = list()
        for fold in folds:
            train_set = list(folds)
            train_set.remove(fold)
            train_set = sum(train_set, [])
            test_set = list()
            #print(fold)
            for row in fold:
                #print(row)
                row_copy = list(row)
                test_set.append(row_copy)
                row_copy[-1] = None
            predicted = algorithm(train_set, test_set, *args)
            actual = [row[-1] for row in fold]
            #print(actual)
            rmse = self.getError(actual, predicted)
            error = rmse
            scores.append(rmse)
        return (scores, error)
    
    def predict(self, row, coefficients):
        yhat = coefficients[0]
        for i in range(len(row) - 1):
            yhat += coefficients[i + 1] * row[i]
        return yhat
    
    def coefficientsGradientDescent(self, train, l_rate, n_epoch):
        coef = []
        for i in range(len(train[0])):
            coef.append(0.0)
        #print(coef)
        cnt = 0
        for epoch in range(n_epoch):
            for row in train:
                #    print(coef)
                yhat = self.predict(row, coef)
                #print(yhat)
                error = yhat - row[-1]  
                coef[0] = coef[0] - l_rate * error    		  
                for i in range(len(row)-1):
                    coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
                if isnan(coef[0]):
                    cnt += 1
                #print(l_rate, n_epoch, error)
        return coef
                
    
    def regressionGradientDescent(self, train, test, l_rate, n_epoch):
        predictions = list()
        coef = self.coefficientsGradientDescent(train, l_rate, n_epoch)
        #print(coef)
        for row in test:
            #print(coef)
            yhat = self.predict(row, coef)
            predictions.append(yhat)
        return predictions
    