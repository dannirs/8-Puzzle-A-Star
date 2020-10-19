'''
Created 2020 M10 14
Author: Danni Shang - 150675520
'''

from copy import deepcopy
from math import sqrt
from queue import PriorityQueue
import itertools
import random

size = 3
heuristic1 = []
heuristic2 = []
heuristic3 = []


class puzzle8:

    def __init__(self): 
        self.goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.moves = 0
        self.empty = [0, 0]
        self.currState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
    def generateRand(self):

        randNum = random.randint(0, 100)
        for i in range(randNum):
            self.slide()
            # self.print()
            # print()
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
        for i in range(len(self.currState)):
            for j in range(len(self.currState[0])):
                print(self.currState[i][j], end='\t')
            print()
        return

    
class puzzle15:

    def __init__(self): 
        self.goalState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.moves = 0
        self.empty = [0, 0]
        self.currState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        
    def generateRand(self):
        
        # self.print()
        randNum = random.randint(0, 50)
        for i in range(randNum):
            self.slide()
            # self.print()
        
        return
    
    def slide(self):

        numStates = 0
        if self.empty[0] == 0:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 1], [1, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 0], [0, 2], [1, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[0, 1], [0, 3], [1, 2]]
            elif self.empty[1] == 3:
                numStates += 1
                possibleMoves = [[0, 2], [1, 3]]
        elif self.empty[0] == 1:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 0], [1, 1], [2, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 1], [1, 0], [1, 2], [2, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[0, 2], [1, 1], [1, 3], [2, 2]]
            elif self.empty[1] == 3:
                numStates += 1
                possibleMoves = [[0, 3], [1, 2], [2, 3]]
        elif self.empty[0] == 2:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[1, 0], [2, 1], [3, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[1, 1], [2, 0], [2, 2], [3, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[1, 2], [2, 1], [2, 3], [3, 2]]
            elif self.empty[1] == 3:
                numStates += 1
                possibleMoves = [[1, 3], [2, 2], [3, 3]]
        elif self.empty[0] == 3:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[2, 0], [3, 1]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[2, 1], [3, 0], [3, 2]]
            elif self.empty[1] == 2:
                numStates += 1
                possibleMoves = [[2, 2], [3, 1], [3, 3]]
            elif self.empty[1] == 3:
                numStates += 1
                possibleMoves = [[2, 3], [3, 2]]
        
        randNum = random.randint(0, numStates - 1)
        temp = possibleMoves[randNum]
        value = self.currState[temp[0]][temp[1]]
        temp2 = self.empty
        self.currState[temp2[0]][temp2[1]] = value
        self.currState[temp[0]][temp[1]] = 0 
        self.empty = possibleMoves[randNum]

        return
    
    def print(self):
        
        '''
        for i in range(len(self.currState)):
            for j in range(len(self.currState[i])):
                print(self.currState[i][j])
                # if self.currState[i][j] < 10:
                #    print(" ")
        '''

        mx = len(max((str(sub[0]) for sub in self.currState), key=len))

        for row in self.currState:
            print("  ".join(["{:<{mx}}".format(ele, mx=mx) for ele in row]))
        # print("\n")


class puzzle24:

    def __init__(self): 
        self.goalState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        self.moves = 0
        self.empty = [0, 0]
        self.currState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        
    def generateRand(self):
        
        # self.print()
        randNum = random.randint(0, 50)
        for i in range(randNum):
            self.slide()
        # self.print()
        
        return
    
    def slide(self):

        numStates = 0
        if self.empty[0] == 0:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 1], [1, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 0], [0, 2], [1, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[0, 1], [0, 3], [1, 2]]
            elif self.empty[1] == 3:
                numStates += 2
                possibleMoves = [[0, 2], [0, 4], [1, 3]]
            elif self.empty[1] == 4:
                numStates += 1
                possibleMoves = [[0, 3], [1, 4]]
        elif self.empty[0] == 1:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[0, 0], [1, 1], [2, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[0, 1], [1, 0], [1, 2], [2, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[0, 2], [1, 1], [1, 3], [2, 2]]
            elif self.empty[1] == 3:
                numStates += 2
                possibleMoves = [[0, 3], [1, 2], [1, 4], [2, 3]]
            elif self.empty[1] == 4:
                numStates += 1
                possibleMoves = [[0, 4], [1, 3], [2, 4]]
        elif self.empty[0] == 2:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[1, 0], [2, 1], [3, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[1, 1], [2, 0], [2, 2], [3, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[1, 2], [2, 1], [2, 3], [3, 2]]
            elif self.empty[1] == 3:
                numStates += 2
                possibleMoves = [[1, 3], [2, 2], [2, 4], [3, 3]]
            elif self.empty[1] == 4:
                numStates += 1
                possibleMoves = [[1, 4], [2, 3], [3, 4]]
        elif self.empty[0] == 3:
            numStates += 2
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[2, 0], [3, 1], [4, 0]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[2, 1], [3, 0], [3, 2], [4, 1]]
            elif self.empty[1] == 2:
                numStates += 2
                possibleMoves = [[2, 2], [3, 1], [3, 3], [4, 2]]
            elif self.empty[1] == 3:
                numStates += 2
                possibleMoves = [[2, 3], [3, 2], [3, 4], [4, 3]]
            elif self.empty[1] == 4:
                numStates += 1
                possibleMoves = [[2, 4], [3, 3], [4, 4]]
        elif self.empty[0] == 4:
            numStates += 1
            if self.empty[1] == 0:
                numStates += 1
                possibleMoves = [[3, 0], [4, 1]]
            elif self.empty[1] == 1:
                numStates += 2
                possibleMoves = [[3, 1], [4, 0], [4, 2]]
            elif self.empty[1] == 2:
                numStates += 1
                possibleMoves = [[3, 2], [4, 1], [4, 3]]
            elif self.empty[1] == 3:
                numStates += 1
                possibleMoves = [[3, 3], [4, 2], [4, 4]]
            elif self.empty[1] == 4:
                numStates += 1
                possibleMoves = [[3, 4], [4, 3]]
        
        randNum = random.randint(0, numStates - 1)
        temp = possibleMoves[randNum]
        value = self.currState[temp[0]][temp[1]]
        temp2 = self.empty
        self.currState[temp2[0]][temp2[1]] = value
        self.currState[temp[0]][temp[1]] = 0 
        self.empty = possibleMoves[randNum]

        return
    
    def print(self):
        
        '''
        for i in range(len(self.currState)):
            for j in range(len(self.currState[i])):
                print(self.currState[i][j])
                # if self.currState[i][j] < 10:
                #    print(" ")
        '''

        mx = len(max((str(sub[0]) for sub in self.currState), key=len))

        for row in self.currState:
            print("  ".join(["{:<{mx}}".format(ele, mx=mx) for ele in row]))
        # print("\n")


class Node(object):

    def __init__(self, puzzle, direction, parent=None):
        self.puzzle = puzzle 
        self.direction = direction
        self.parent = parent
        if parent == None:
            self.height = 0 # g of n
        else:
            self.height = parent.height + 1
    
    def fn1(self):
        return self.misplacedTiles() + self.height
    
    def fn2(self):
        return self.manhattanDist() + self.height
    
    def fn3(self):
        return self.euclideanDist() + self.height

    def __lt__(self, other): 
        return 0

    def empty(self):
        for i in range(size):
            for j in range(size):
                if self.puzzle[i][j] == 0:
                    return i, j
    
    def misplacedTiles(self):
        if size == 3:
            goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        elif size == 4: 
            goalState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        elif size == 5: 
            goalState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        
        mismatch = 0
        for i, j in zip(self.puzzle, goalState):
            for m, n in zip(i, j):               
                if m != n and m != 0:
                    mismatch += 1
        # print("Mismatch: ", mismatch)
        return mismatch
    
    def manhattanDist(self):
        t = 0
        for i in range(size):
            for j in range(size):
                r = int(self.puzzle[i][j] / size)
                c = int(self.puzzle[i][j] % size)
                t += abs(i - r) + abs(j - c)
        return t
    
    def euclideanDist(self):
        t = 0
        for i in range(size):
            for j in range(size):
                r = int(self.puzzle[i][j] / size)
                c = int(self.puzzle[i][j] % size)
                t += sqrt(((i - r) * (i - r)) + ((j - c) * (j - c)))
        return t

    def getChildren(self):
        emptySpace = self.empty()
        puzzle = self.puzzle 
        nodes = []
        if not emptySpace[1] - 1 < 0:  # check to see if the node can be shifted to the right
            puzzle_left = deepcopy(puzzle)
            puzzle_left[emptySpace[0]][emptySpace[1]] = puzzle_left[emptySpace[0]][emptySpace[1] - 1]  # puts a value of the node above to the place, where zero was.
            puzzle_left[emptySpace[0]][emptySpace[1] - 1] = 0
            puzzle_left_node = Node(puzzle_left, 'right', self)
            nodes.append(puzzle_left_node)
        if emptySpace[1] + 1 < size:  # check to see if the node can be shifted to the left
            puzzle_right = deepcopy(puzzle)
            puzzle_right[emptySpace[0]][emptySpace[1]] = puzzle_right[emptySpace[0]][emptySpace[1] + 1]  # puts a value of the node above to the place, where zero was.
            puzzle_right[emptySpace[0]][emptySpace[1] + 1] = 0 
            puzzle_right_node = Node(puzzle_right, 'left', self)
            nodes.append(puzzle_right_node)
        if not emptySpace[0] - 1 < 0:  # check to see if the node can be shifted downwards
            puzzle_up = deepcopy(puzzle) 
            puzzle_up[emptySpace[0]][emptySpace[1]] = puzzle_up[emptySpace[0] - 1][emptySpace[1]] 
            puzzle_up[emptySpace[0] - 1][emptySpace[1]] = 0 
            puzzle_up_node = Node(puzzle_up, 'down', self) 
            nodes.append(puzzle_up_node)  # check to see if the node can be shifted upwards
        if emptySpace[0] + 1 < size:  
            puzzle_down = deepcopy(puzzle)
            puzzle_down[emptySpace[0]][emptySpace[1]] = puzzle_down[emptySpace[0] + 1][emptySpace[1]]  # puts a value of the node above to the place, where zero was.
            puzzle_down[emptySpace[0] + 1][emptySpace[1]] = 0 
            puzzle_down_node = Node(puzzle_down, 'up', self)
            nodes.append(puzzle_down_node)
        return nodes

    def path(self):  # returns a list of objects.
        p = []
        p.append((self.direction, self.puzzle))
        n = self.parent
        if n != None:
            while n.parent is not None:
                p.append((n.direction, n.puzzle))
                n = n.parent
            p.append((n.direction, n.puzzle))
            p.reverse()
        return p


def h1Algo(start_node):
    PQueue = PriorityQueue() 
    visited = []
    expanded = 0
    display(start_node.puzzle)
    print()
    PQueue.put((start_node.fn1(), start_node)) 
    # print(start_node.fn1())
    if size == 3:
        goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    elif size == 4: 
        goalState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    elif size == 5: 
        goalState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
    while not PQueue.empty():  
        fn, n = PQueue.get() 
        if n.puzzle in visited:   
            continue
        if goalState == n.puzzle:  
            print('Misplaced Tiles Heuristic: ')
            print('Expanded nodes:', expanded)
            steps = (len(n.path())) - 1
            print('Moves:', (len(n.path())) - 1)
            print('-------------------------------')
            board = start_node.puzzle
            board2 = list(itertools.chain(*board))
            results = [board2, expanded, steps]
            heuristic1.append(results)
            # draw_path(n.path())
            # display(start_node.b)
            return
       
        visited.append(n.puzzle)
       
        expanded += 1
       
        for nnode in n.getChildren(): 
            PQueue.put((nnode.fn1(), nnode))


def h2Algo(start_node):
    PQueue = PriorityQueue() 
    visited = []
    expanded = 0
    PQueue.put((start_node.fn2(), start_node))
    if size == 3:
        goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    elif size == 4: 
        goalState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    elif size == 5: 
        goalState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
    while not PQueue.empty():  
        fn, n = PQueue.get() 
        if n.puzzle in visited:   
            continue
        if goalState == n.puzzle:  
            print('Manhattan Distance Heuristic:')
            print('Expanded nodes:', expanded)
            steps = (len(n.path())) - 1
            print('Moves:', (len(n.path())) - 1)
            print('-------------------------------')
            board = start_node.puzzle
            board2 = list(itertools.chain(*board))
            results = [board2, expanded, steps]
            heuristic2.append(results)
            # draw_path(n.path())
            # display(start_node.b)
            return
       
        visited.append(n.puzzle)
       
        expanded += 1
       
        for nnode in n.getChildren(): 
            PQueue.put((nnode.fn2(), nnode))     


def h3Algo(start_node):
    PQueue = PriorityQueue() 
    visited = []
    expanded = 0
    PQueue.put((start_node.fn3(), start_node)) 
    if size == 3:
        goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    elif size == 4: 
        goalState = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    elif size == 5: 
        goalState = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
    while not PQueue.empty():  
        fn, n = PQueue.get() 
        if n.puzzle in visited:   
            continue
        if goalState == n.puzzle:  
            print('Euclidean Distance Heuristic:')
            print('Expanded nodes:', expanded)
            steps = (len(n.path())) - 1
            print('Moves:', (len(n.path())) - 1)
            print('-------------------------------')
            board = start_node.puzzle
            board2 = list(itertools.chain(*board))
            results = [board2, expanded, steps]
            heuristic3.append(results)
            # draw_path(n.path())
            # display(start_node.b)
            return
       
        visited.append(n.puzzle)
       
        expanded += 1
       
        for nnode in n.getChildren(): 
            PQueue.put((nnode.fn3(), nnode))   


def display(puzzle):
        
        mx = len(max((str(i[0]) for i in puzzle), key=len))
        for row in puzzle:
            print("  ".join(["{:<{mx}}".format(ele, mx=mx) for ele in row]))
        # print("\n")

'''
---------------------------------------------------------
---------------         Testing      --------------------
---------------------------------------------------------
'''
'''

print("8 Puzzle")
size = 3
iterations = 5
for i in range (0, iterations):
    board = puzzle8()
    board.generateRand()
    initial_node = Node(board.currState, 'start')
    h1Algo(initial_node)
    h2Algo(initial_node)
    h3Algo(initial_node)
    
print()
print("Table")
print("----------------------------------------")
print("Puzzle | H1 Expanded Nodes | H1 Moves | H2 Expanded Nodes | H2 Moves | H3 Expanded Nodes | H3 Moves")
for i in range(0, iterations):
    print(heuristic1[i][0], heuristic1[i][1], heuristic1[i][2], heuristic2[i][1], heuristic2[i][2], heuristic3[i][1], heuristic3[i][2])

print()
print("15 Puzzle")
size = 4
iterations = 5
for i in range (0, iterations):
    board = puzzle15()
    board.generateRand()
    initial_node = Node(board.currState, 'start')
    h1Algo(initial_node)
    h2Algo(initial_node)
    h3Algo(initial_node)
    
print()
print("Table")
print("----------------------------------------")
print("Puzzle | H1 Expanded Nodes | H1 Moves | H2 Expanded Nodes | H2 Moves | H3 Expanded Nodes | H3 Moves")
for i in range(0, iterations):
    print(heuristic1[i][0], heuristic1[i][1], heuristic1[i][2], heuristic2[i][1], heuristic2[i][2], heuristic3[i][1], heuristic3[i][2])

print()
print("24 Puzzle")
size = 5
iterations = 5
for i in range (0, iterations):
    board = puzzle24()
    board.generateRand()
    initial_node = Node(board.currState, 'start')
    h1Algo(initial_node)
    h2Algo(initial_node)
    h3Algo(initial_node)
    
print()
print("Table")
print("----------------------------------------")
print("Puzzle | H1 Expanded Nodes | H1 Moves | H2 Expanded Nodes | H2 Moves | H3 Expanded Nodes | H3 Moves")
for i in range(0, iterations):
    print(heuristic1[i][0], heuristic1[i][1], heuristic1[i][2], heuristic2[i][1], heuristic2[i][2], heuristic3[i][1], heuristic3[i][2])  
    
