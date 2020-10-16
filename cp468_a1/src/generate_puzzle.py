
# Created on 2020 M10 14

# @author: Danni

import random


class puzzle:

    def __init__(self): 
        self.goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.moves = 0
        self.empty = [0, 0]
        self.currState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
    def generateRand(self):
        
        self.print()
        randNum = random.randint(0, 20)
        for i in range(randNum):
            self.slide()
            self.print()
        
        return
    
    def slide(self):

        numStates = 0
        if self.empty[0] == 0:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[1, 0], [0, 1]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 0], [0, 2], [1, 1]]
            elif self.empty[1] == 2:
                numStates += 1
                possibleMoves = [[0, 1], [1, 2]]
        elif self.empty[0] == 1:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 0], [1, 1], [2, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[1, 0], [1, 2], [0, 1], [2, 1]]
            elif self.empty[1] == 2:
                numStates += 1
                possibleMoves = [[0, 2], [1, 1], [2, 2]]
        elif self.empty[0] == 2:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[2, 1], [1, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[2, 0], [2, 2], [1, 1]]
            elif self.empty[1] == 2:
                numStates += 1
                possibleMoves = [[2, 1], [1, 2]]
        
        randNum = random.randint(0, numStates - 1)
        temp = possibleMoves[randNum]
        value = self.currState[temp[0]][temp[1]]
        temp2 = self.empty
        self.currState[temp2[0]][temp2[1]] = value
        self.currState[temp[0]][temp[1]] = 0 
        self.empty = possibleMoves[randNum]

        return
    
    def print(self):
        for v in self.currState:
            print(*v)
        print("\n")

