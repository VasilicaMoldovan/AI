# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:22:11 2020

@author: Vasilica
"""
import copy

class Board:
    def __init__(self, n):
        self.__dimension = n
        self.__board = self.constructBoard(n)
        
    def getDimension(self):
        return self.__dimension
    
    def constructBoard(self, n):
        board = []
        for i in range(0, n):
            aux = []
            for j in range(0, n):
                aux.append(0)
            board.append(aux)
        return board 
    
    def setDimension(self, n):
        self.__dimension = n
        
    def getBoard(self):
        return self.__board
    
    def __str__(self):
        return str(self.__board)
        

class State:
    def __init__(self, board):
        self.__values = board.getBoard()
        self.__dimension = board.getDimension()
    
    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]
    
    def getDimension(self):
        return self.__dimension
    
    def __str__(self):
        s=''
        for x in self.__values:
            s+=str(x)+"\n"
        return s
    
    def isPossible(self, values, row, col): 
        for i in range(0, col): 
            if values[row][i] == 1: 
                return False
            
        for j in range(0, row):
            if values[j][col] == 1:
                return False
  
        for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
            if values[i][j] == 1: 
                return False
  
        for i, j in zip(range(row, self.__dimension, 1),  
                    range(col, -1, -1)): 
            if values[i][j] == 1: 
                return False
        return True
    
    def isFull(self, cnt):
        if cnt >= self.__dimension:
            return True
        return False
    
    

class Problem:
    def __init__(self, state1, state2, n):
        self.initialState = state1
        self.finalState = state2
        self.dimension = n
    
    def expand(self, state):
        return state
    
    def heuristics(self, count):
        return count + 1
    
    def getFinal(self):
        return self.initialState.getValues()

class Controller:
    def __init__(self, newProblem):
        self.problem = newProblem
        self.board = copy.deepcopy(self.problem.initialState.getValues())
        self.dimension = self.problem.initialState.getDimension()
    
    def dfs(self, column):
        if self.problem.initialState.isFull(column) == True:
            return True
        for i in range(0, self.dimension): 
            if self.problem.initialState.isPossible(self.board, i, column): 
                self.board[i][column] = 1
                if self.dfs(column + 1) == True:
                    return True
                self.board[i][column] = 0
           
        return False
    
    def Dfs(self, column):
        self.dfs(column)
        self.problem.finalState.setValues(self.board)
        
        
    def bestFS(self, x):
        queue = [x]
        visited = [x]
        found = False
        while ( len(queue) > 0 and found == False):
            x = queue[0]
            queue.pop(0)
            if self.problem.initialState.isFull(x) == True:
                    return
            for i in range(0, self.dimension):
                if self.problem.initialState.isPossible(self.board, i, x) == True: 
                    self.board[i][x] = 1
                else:
                    self.board[i][x] = 0
                queue.append(self.problem.heuristics(i))
                visited.append(i)
            found = self.problem.initialState.isFull(x)
    
    def greedy(self):
        self.bestFS(0)
        self.problem.finalState.setValues(self.board)
    

class UI:
    def __init__(self):
        self.dimension = self.readFromFile()
        self.board = Board(self.dimension)
        self.initialState = State(self.board)
        self.finalState = State(self.board)
        self.problem = Problem(self.initialState, self.finalState, self.initialState.getDimension())
        self.controller = Controller(self.problem)
    
    def readFromFile(self):
        file = open("lab2file.txt", 'r')
        dimension =  int(file.readline())
        return dimension
        
    def printMainMenu(self):
        print("Choose one of the following: ")
        print("1.Print initial board")
        print("2. Print board after dfs")
        print("3. Print board after greedy")
        print("4. Exit")
        
    def run(self):
        run=True
        self.printMainMenu()
        while run:        
            try: 
                command = int(input(">>"))
                if command == 4:
                    runM = False
                    return
                elif command == 1:
                    print(self.initialState)
                elif command == 2:
                    self.controller.Dfs(0)
                    print(self.controller.problem.finalState)
                elif command == 3:
                    self.controller.greedy()
                    print(self.controller.problem.finalState)
            except:
                print('invalid command')
        

def main():
    ui = UI()
    ui.run()

main()