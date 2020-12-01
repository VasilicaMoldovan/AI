# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:00:08 2020

@author: Vasilica
"""
classes = {
    'Slight-Left-Turn': 0,
    'Move-Forward': 1,
    'Slight-Right-Turn': 2,
    'Sharp-Right-Turn': 3
}

class Problem:
    instance = None
    
    def __init__(self, path, inputpath):
        self._outputPath = path
        self._inputPath = inputpath
        
    def buildDataset(self):
        inp_dataset, inp_labels = [], []
        with open(self._inputPath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data_row = line.strip().split(',')
                data_row, label = data_row[:-1], data_row[-1]
                data_row = [float(x) for x in data_row]
                inp_dataset.append(data_row)
                inp_labels.append(classes[label])
        return inp_dataset, inp_labels
    
    def getOutputPath(self):
        return self._outputPath
    