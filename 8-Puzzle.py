'''
Created 2020 M10 14
Author: Group IDs?
'''

from queue import PriorityQueue as pq
from copy import deepcopy
import random
from random import randint

"""Creates a class called Node"""
class Node(object):
    
    """Constractor of the class. b = board, m = move, p = parent"""
    def __init__(self, b, m,parent=None):
        self.b = b  
        self.m = m  
        self.p = parent
        
    """Special method,which makes it possible for the classes to be compared. Used for PQueue."""
    def __lt__(self,other): 
        return 0
    
    """Returns the position of the empty block. """
    def empty_position(self):
        for i in range(3):
            for j in range(3):
                if self.b[i][j] == 0:
                    return i,j
                
    """Returns the manhattan distance."""
    def calcmanhattan_distance(self):
        t = 0
        for i in range(3):
            for j in range(3):
                r = int(self.b[i][j]/3)
                c = int(self.b[i][j]%3)
                t += abs(i-r)+abs(j-c)
        return t
    
    """The function generates and returns nodes."""
    def create_nodes(self):
        empty_position = self.empty_position()
        b = self.b 
        nodes = []
        if not empty_position[0]-1<0: #check to see if the node can be shifted downwards
            b_up = deepcopy(b) 
            b_up[empty_position[0]][empty_position[1]] = b_up[empty_position[0]-1][empty_position[1]] 
            b_up[empty_position[0]-1][empty_position[1]] = 0 
            b_up_node = Node(b_up,'down',self) 
            nodes.append(b_up_node) #check to see if the node can be shifted upwards
        if empty_position[0]+1<3:  
            b_down = deepcopy(b)
            b_down[empty_position[0]][empty_position[1]] = b_down[empty_position[0]+1][empty_position[1]] #puts a value of the node above to the place, where zero was.
            b_down[empty_position[0]+1][empty_position[1]] = 0 
            b_down_node = Node(b_down, 'up',self)
            nodes.append(b_down_node)
        if not empty_position[1]-1<0: #check to see if the node can be shifted to the right
            b_left = deepcopy(b)
            b_left[empty_position[0]][empty_position[1]] = b_left[empty_position[0]][empty_position[1]-1] #puts a value of the node above to the place, where zero was.
            b_left[empty_position[0]][empty_position[1]-1] = 0
            b_left_node = Node(b_left,'right',self)
            nodes.append(b_left_node)
        if empty_position[1]+1<3: #check to see if the node can be shifted to the left
            b_right = deepcopy(b)
            b_right[empty_position[0]][empty_position[1]] = b_right[empty_position[0]][empty_position[1]+1] #puts a value of the node above to the place, where zero was.
            b_right[empty_position[0]][empty_position[1]+1] = 0 
            b_right_node = Node(b_right,'left',self)
            nodes.append(b_right_node)
        
        return nodes
    
    """Stores all the parents "traceback" of a node. """
    def node_traceback(self):# returns a list of objects.
        p = []
        p.append((self.m,self.b))
        n = self.p
        while n.p is not None:
            p.append((n.m,n.b))
            n = n.p
        p.append((n.m,n.b))
        p.reverse()
        return p
  

    
    
class puzzle:

    def __init__(self): 
        self.goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.moves = 0
        self.empty = [0, 0]
        self.currState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
    def generateRand(self):
        

        randNum = random.randint(0, 50)
        for i in range(randNum):
            self.slide()
            #self.print()
            #print()
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
                print(self.currState[i][j],end='\t')
            print()
        return
        


"""Actual A star fucntion."""    

def Astar_algo(start_node):
    PQueue = pq() 
    visited = []
    explored = 0
    PQueue.put((start_node.calcmanhattan_distance(),start_node)) 
    while not PQueue.empty():  
        h, n = PQueue.get() 
        if n.b in visited:   
            continue
        if h==0: 
            print('Congratulations!')
            print('The number of explored nodes:%d'%explored)
            print('The number of steps taken:',len(n.node_traceback()))
            draw_path(n.node_traceback())
            return
       
        visited.append(n.b)
       
        explored+=1
       
        for nnode in n.create_nodes(): 
            PQueue.put((nnode.calcmanhattan_distance(),nnode))

           
"""Prints the board."""         
def draw_board(board):
    print('___________')
    for i in board:
        print('|%d|%d|%d|'%(i[0],i[1],i[2]))
        print('___________') 
        
"""Draws the path."""   
def draw_path(path):
    for b in path:
        print(b[0])
        draw_board(b[1])
    print('END')
    print()

'''
---------------------------------------------------------
---------------         Testing      --------------------
---------------------------------------------------------
'''
    
board = puzzle()

for i in range (0,3):
    board.generateRand()
    initial_node = Node(board.currState,'start')
    Astar_algo(initial_node)