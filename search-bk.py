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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    testSuccessor = problem.getSuccessors(problem.getStartState());
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", testSuccessor
    print "Start's first successor:", testSuccessor[0]
    print "Start's first successor direction:", testSuccessor[0][1]
    print "Start's first successor position:", testSuccessor[0][0]
    print "Start's first successor x-position:", testSuccessor[0][0][0]
    print "***********************************************"

    """ initialize actions """
    actions = [s, s]

    exploredNodes = util.Stack();


    if problem.isGoalState(problem.getStartState()) == True:
        return None
    else:
        exploredNodes.push(problem.getStartState())
    #testStack.push(1);
    #print "testStack: ", testStack;

    # if problem.isGoalState(exploredNodes.pop()) == True:
    #     print "actions: ", actions
    #     return actions
    # else:
        #currentSuccessors = problem.getSuccessors(currentState);
        #exploredNodes.pop()
    #currentState = exploredNodes.pop()
    i = 0
    #print "currentState: ", currentState # (5, 5)
    #print "exploredNodes: ", exploredNodes # 
    #print "successor of currentState: ", problem.getSuccessors(currentState) #[((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #print "is it none? ", problem.getSuccessors(currentState) is not None # True
    

    # visited = set(currentState)
    # currentSuccessors = problem.getSuccessors(currentState)
    # currentState = currentSuccessors[0]
    # print "new currentState: ", currentState
    # visited.add(currentState)
    # exploredNodes.push(currentState)
    # print "current successor: ", currentSuccessors[0]
    #print "new currentSuccessors to be set: ", problem.getSuccessors(currentState)
    #currentSuccessors = problem.getSuccessors(currentState)

    startState = problem.getStartState()
    print "startState: ", startState
    visited = set()
    visited.add(startState)
    print "visited: ", visited
    currentSuccessors = problem.getSuccessors(problem.getStartState())
    print "currentSuccessors: ", currentSuccessors

    while currentSuccessors is not None:
        print "i: ", i
        #print "currentState: ", currentState
        print "currentSuccessors: ", currentSuccessors
        print "visited: ", visited
        print "exploredNodes: ", exploredNodes

        if currentSuccessors[i][0] not in visited:
            currentState = currentSuccessors[i]
            visited.add(currentState[0])
            exploredNodes.push(currentState)
            currentSuccessors = problem.getSuccessors(currentState[0])
            i=0
        #else:
        i=i+1         

    print "exploredNodes: ", exploredNodes

    "*** YOUR CODE HERE ***"
    return actions
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
