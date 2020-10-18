'''
Created on 2020 M10 14

@author: Danni
'''

import generate_puzzle


class algo(object):

    def __init__(self):
        self.open = []
        self.closed = []
        self.moves = 0
        self.deadend = False
    
    def h1(self, currState, goalState):
        
        mismatch = 0
        for i, j in zip(currState, goalState):
            for m, n in zip(i, j):               
                if m != n and m != 0:
                    mismatch += 1
        print("Mismatch: ", mismatch)
                
        return mismatch
    
    def nextMove(self, puzzle):
        numStates = 0
        heuristic = []
        # finds all children (possible moves)
        if puzzle.empty[0] == 0:
            numStates += 1
            if puzzle.empty[1] == 0:
                numStates += 1
                possibleMoves = [[1, 0], [0, 1]]
            elif puzzle.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 0], [0, 2], [1, 1]]
            elif puzzle.empty[1] == 2:
                numStates += 1
                possibleMoves = [[0, 1], [1, 2]]
        elif puzzle.empty[0] == 1:
            numStates += 2
            if puzzle.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 0], [1, 1], [2, 0]]
            elif puzzle.empty[1] == 1:
                numStates += 2
                possibleMoves = [[1, 0], [1, 2], [0, 1], [2, 1]]
            elif puzzle.empty[1] == 2:
                numStates += 1
                possibleMoves = [[0, 2], [1, 1], [2, 2]]
        elif puzzle.empty[0] == 2:
            numStates += 1
            if puzzle.empty[1] == 0:
                numStates += 1
                possibleMoves = [[2, 1], [1, 0]]
            elif puzzle.empty[1] == 1:
                numStates += 2
                possibleMoves = [[2, 0], [2, 2], [1, 1]]
            elif puzzle.empty[1] == 2:
                numStates += 1
                possibleMoves = [[2, 1], [1, 2]]
        
        print("Children:")
        countV = 0
        # print each child
        for v in possibleMoves:
            if v in self.closed:
                possibleMoves.remove(v)
            if v not in self.closed: 
                countV += 1
                print(v)
                # temporary swap of empty space and child
                tempEmpty = puzzle.empty  # [1,0]
                tempV = v  # [0,0]
                tempValue = puzzle.currState[tempV[0]][tempV[1]]  # 3
                # tempCurr = puzzle.currState 
                puzzle.currState[tempV[0]][tempV[1]] = 0
                puzzle.currState[puzzle.empty[0]][puzzle.empty[1]] = tempValue
                puzzle.empty = v
                
                # find heuristic; append to list
                h1 = self.h1(puzzle.currState, puzzle.goalState)
                h1 += self.moves
                heuristic.append(h1)
                
                # swap back
                puzzle.currState[tempV[0]][tempV[1]] = tempValue
                puzzle.empty = tempEmpty
                puzzle.currState[puzzle.empty[0]][puzzle.empty[1]] = 0 
        
        print(countV)
        if countV == 0: 
            self.deadend = True
            return
        
        # find the smallest heuristic
        smallest = heuristic[0]
        count = 0
        index = 0
        for i in heuristic:
            if i < smallest:
                smallest = i
                index = count
            count += 1
        
        # append child with smallest heuristic to closed list
        self.closed.append(possibleMoves[index])
        
        tempEmpty = puzzle.empty  # [1,0]
        tempV = possibleMoves[index]  # [0,0]
        tempValue = puzzle.currState[tempV[0]][tempV[1]]  # 3
        puzzle.currState[tempV[0]][tempV[1]] = 0 
        puzzle.currState[puzzle.empty[0]][puzzle.empty[1]] = tempValue
        puzzle.empty = possibleMoves[index]
        
        possibleMoves.remove(possibleMoves[index])
        
        # append other children to open list
        for v in possibleMoves:
            self.open.append(v)
        
        self.moves += 1
        
        # print closed and open iists
        print("\n")
        print("Closed:")
        for v in self.closed:
            print(v)
        print("\n")
        
        print("Open:")
        for v in self.open:
            print(v)
        print("\n")
        
        print("New current state: ")
        for v in puzzle.currState:
            print(*v)
        
        return
    
    def solved(self, puzzle):
        
        if puzzle.currState == puzzle.goalState:
            solved = True
            # print(solved)
        else:
            solved = False
            # print(solved)
        return solved
    # open list
    # contains all the nodes that are being generated and don't exist in closed list
    # initially holds the start node
    # next node chosen from the open list is based on its f score (heuristic); node with the least f score is explored
    
    # closed list
    # after a node is explored, it's put in the closed list and its neighbors are put in the open list
    # each node has a pointer to its parent so that at any given point it can retrace the path to the parent

    
    # not being used:
class node(object):
    
    def __init__(self, value, heuristic):
        self.parent = None
        self.value = value
        self.heuristic = heuristic
        
