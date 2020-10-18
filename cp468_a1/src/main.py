'''
Created on 2020 M10 15

@author: Danni
'''
import time
from Algo import algo
from generate_puzzle import puzzle

if __name__ == '__main__':
    pass
 
puzzleInstance = puzzle()
puzzleInstance.generateRand()
algoInstance = algo()
# h1 = algo.h1(algoInstance, puzzleInstance.currState, puzzleInstance.goalState)
# print(algoInstance.closed)
while algoInstance.deadend == False and algo.solved(algoInstance, puzzleInstance) == False: 
    algo.nextMove(algoInstance, puzzleInstance)
    time.sleep(0.5)

if algoInstance.deadend == True:
    print("Deadend")
elif algo.solved(algoInstance, puzzleInstance) == True:
    print("Solved in ")
    print(algoInstance.moves)
    print(" moves.")

