'''
Created on 2020 M10 15

@author: Danni
'''

from Algo import algo
from generate_puzzle import puzzle

if __name__ == '__main__':
    pass
 
puzzleInstance = puzzle()
puzzleInstance.generateRand()
h1 = algo.h1(puzzleInstance.currState, puzzleInstance.currState, puzzleInstance.goalState)

