# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    fringe = util.Stack()
    fringe.push( (problem.getStartState(), []) )
    visited = []
    
    while not fringe.isEmpty():
        currentCoor, listActions = fringe.pop()
        for coor, action, cost in problem.getSuccessors(currentCoor):
            if problem.isGoalState(coor):
                return listActions + [action]
            elif coor not in visited:
                fringe.push( (coor, listActions + [action]) )
                visited.append(coor)
            else:
                pass
    return 0

def breadthFirstSearch(problem):
    fringe = util.Queue()
    fringe.push( (problem.getStartState(), []) )
    visited = []
    # visitedSet = set()

    while not fringe.isEmpty():
        currentCoor, listActions = fringe.pop()
        # print currentCoor
        for coor, action, cost in problem.getSuccessors(currentCoor):
            # xy = tuple()
            # grid = tuple()
            # xy, grid = coor
            # print "xy", xy
            # print "--coor", coor
            # print "xy ", xy
            # print "grid ", grid
            if problem.isGoalState(coor):
                print "*****i found it!"
                # print "length of visiited: ", len(visited)
                return listActions + [action]
            elif coor not in visited:
                fringe.push( (coor, listActions + [action]))
                visited.append(coor)
                print listActions + [action]
            else:
                pass
    return 0

# def breadthFirstSearch(problem):
#     fringe = util.Queue()
#     fringe.push( (problem.getStartState(), []) )
#     visited = []
#     visitedSet = set()
#     xy = tuple()
#     grid = tuple()
#     while not fringe.isEmpty():
#         currentNode, listActions = fringe.pop()
#         # print currentCoor
#         currentCoor, visitedCorners = currentNode
#         # print "currentNode: ", currentNode
#         # print "visitedCorners: ", visitedCorners
#         for coor, action, cost in problem.getSuccessors(currentNode):
#             # xy = tuple()
#             # grid = tuple()
#             # print "xy: ", xy
#             # print "grid: ", grid
#             xy, grid = coor
#             # print "xy", xy
#             # print "coor", coor
#             # print "xy ", xy
#             # print "grid ", grid
#             if problem.isGoalState(coor):
#                 print "*****i found it!"
#                 # print "actions: ", listActions + [action]
#                 return listActions + [action]
#             elif xy not in visitedSet:
#                 fringe.push( (coor, listActions + [action]))
#                 visited.append(coor)
#                 visitedSet.add(xy)
#                 # print listActions + [action]
#             else:
#                 pass
#     return 0

def uniformCostSearch(problem):
    fringe = util.PriorityQueue()
    fringe.push( (problem.getStartState(), []), 0 )
    visited = []
    
    while not fringe.isEmpty():
        currentCoor, listActions = fringe.pop()
        for coor, action, cost in problem.getSuccessors(currentCoor):
            newListActions = listActions + [action]
            if problem.isGoalState(coor):
                return newListActions
            elif coor not in visited:
                fringe.push( (coor, newListActions), problem.getCostOfActions(newListActions) )
                visited.append(coor)
            else:
                pass
    return 0

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    fringe = util.PriorityQueue()
    fringe.push( (problem.getStartState(), []), 0 )
    visited = []
    # visitedSet = set()
    while not fringe.isEmpty():
        currentCoor, listActions = fringe.pop()
        for coor, action, cost in problem.getSuccessors(currentCoor):
            newListActions = listActions + [action]
            if problem.isGoalState(coor):
                # print "length of visited list: ", len(visited)
                # print "visited: ", visited
                # print "length of visited set: ", len(visitedSet)
                return newListActions
            elif coor not in visited:
                fringe.push( (coor, newListActions), \
                problem.getCostOfActions(newListActions) + heuristic(coor,problem))
                visited.append(coor)
                # visitedSet.add(coor[0])
                # print "coor[0]: ", coor[0]
                # print "coor: ", coor
            else:
                pass
    return 0

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
