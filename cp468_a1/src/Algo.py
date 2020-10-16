'''
Created on 2020 M10 14

@author: Danni
'''

import generate_puzzle


class algo(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def h1(self, currState, goalState):
        
        mismatch = 0
        for i, j in zip(currState, goalState):
            for m, n in zip(i, j):               
                if m != n and m != 0:
                    mismatch += 1
        print("Mismatch: ", mismatch)
                
        return mismatch
    
    def h2(self):
        
        initial_state = [1, 5, 3, 4, 2, 6, 7, 8, 0]
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        def calculateManhattan(initial_state):
            initial_config = initial_state
            manDict = 0
            for i, item in enumerate(initial_config):
                prev_row, prev_col = int(i / 3) , i % 3
                goal_row, goal_col = int(item / 3), item % 3
                manDict += abs(prev_row - goal_row) + abs(prev_col - goal_col)
            return manDict
        
    # open list
    # contains all the nodes that are being generated and don't exist in closed list
    # initially holds the start node
    # next node chosen from the open list is based on its f score (heuristic); node with the least f score is explored
    
    # closed list
    # after a node is explored, it's put in the closed list and its neighbors are put in the open list
    # each node has a pointer to its parent so that at any given point it can retrace the path to the parent
        
