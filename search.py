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

    #the series of actions to be taken to get to the successor
    actionsToVisit = []

    #startState
    startState = problem.getStartState()

    #set of states that have been visited
    visited = set() 

    """ check if startState is goal state """
    if problem.isGoalState(startState) == True:
        return None
    
    currentSuccessors = problem.getSuccessors(startState)
    # print "currentSuccessors: ", currentSuccessors

    
    """ initialize nodesToVisit """
    nodesToVisit = util.Stack()
    # nodesToVisit.push(startState)

    for successor, action, cost in currentSuccessors:
        nodesToVisit.push(successor)
        actionsToVisit.append([action])

        # print "nodesToVisit: ", successor
        # print "action to nodes to visit", action
    # print "actions to visit: ", actionsToVisit
    visited.add(startState)
    currentAction = []
    tempAction = []

    """ Main DFS Logic"""
    while not nodesToVisit.isEmpty():
        # print "********* inside while loop **********"

        """
        pop the top node to be visited and the full series of action it takes
        to get to that node from start state
        """
        currentState = nodesToVisit.pop()
        currentAction = actionsToVisit.pop()
        
        # print "-- action taken: ", currentAction
        # print " -- remaining actions in actionsToVisit", actionsToVisit
        #actions.append(currentState[1])
        # set currentState to never visted node popped from nodesToVisit

        if currentState not in visited:
            # print "currentState: ", currentState
            # print "visited before loop: ", visited
            if problem.isGoalState(currentState) == True:
                print "the goal state is: ", currentState
                return currentAction
            # problem.getSuccessors(currentState)

            elif problem.getSuccessors(currentState):
                for Successor, successorAction, cost in problem.getSuccessors(currentState):
                    if Successor not in visited:
                        nodesToVisit.push(Successor)
                        # print "-- old current action: ", currentAction
                        # print "--- currentAction: ", currentAction
                        tempAction = list(currentAction) # creating explicit copy
                        tempAction+=[successorAction]
                        # print "--- Successor: ", Successor
                        # print "--- tempAction to append to get to the successor: ", tempAction
                        actionsToVisit.append(tempAction)
                        # print "--- currentAction end of elif: ", currentAction
                    # 
                    #print "nodes visited: ", visited
            else:
                print "**** it is WRONG ****"
                return False

            visited.add(currentState) # add current state to visited
            # print "nodes visited after loop: ", visited
            # print "nodes to visit: ", nodesToVisit
    # print "********************outside of while loop ********************"
            
    print "final state: ", currentState
    util.raiseNotDefined()
    return currentAction

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    Modified directly from DFS above, except only using Queue for
    actionsToVisit and nodesToVisit
    """
    
    #the series of actions to be taken to get to the successor
    actionsToVisit = util.Queue()

    #startState
    startState = problem.getStartState()
    print "startState: ", startState

    #set of states that have been visited
    visited = set() 

    """ check if startState is goal state """
    if problem.isGoalState(startState) == True:
        return None
    
    print "????here?"

    currentSuccessors = problem.getSuccessors(startState)
    # print "currentSuccessors: ", currentSuccessors
    # print "currentSuccessors x: ", currentSuccessors[0][0][0]
    # print "walls at [27][16]?", problem.walls[27][16]
    # print "walls at [28][16]?", problem.walls[28][16]
    # print "walls at [29][16]?", problem.walls[29][16]
    # print "walls at [1][1   ]?", problem.walls[1][1]
    # print "walls at [1][2]?", problem.walls[1][2]
    # print "walls at [29][16]?", problem.walls[30][13]
    # print "walls at [29][16]?", problem.walls[29][13]
    # print "walls at [29][16]?", problem.walls[31][13]
    # print "cost of actions: West ", problem.getCostOfActions(['West','West','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East','East','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East'])
    # print "cost of actions: North ", problem.getCostOfActions(['South','North'])
    # print "cost of actions: South ", problem.getCostOfActions(['South'])

    """ initialize nodesToVisit """
    nodesToVisit = util.Queue()
    # nodesToVisit.push(startState)

    for successor, action, cost in currentSuccessors:
        nodesToVisit.push(successor)
        actionsToVisit.push([action])
        # print "successor[0]", successor[0]
        # print "wall at successor: ", problem.walls[successor[0][0]][successor[0][1]]

        print "nodesToVisit: ", successor
        print "action to nodes to visit: ", action
    # print "actions to visit: ", actionsToVisit
    visited.add(startState)
    currentAction = []
    tempAction = []

    """ Main BFS Logic"""
    while not nodesToVisit.isEmpty():
        # print "********* inside while loop **********"

        """
        pop the top node to be visited and the full series of action it takes
        to get to that node from start state
        """
        currentState = nodesToVisit.pop()
        currentAction = actionsToVisit.pop()

        while currentState in visited:
            currentState = nodesToVisit.pop()
            currentAction = actionsToVisit.pop()

        print "currentState: ", currentState
        print "-- action taken: ", currentAction
        print " -- remaining actions in actionsToVisit", actionsToVisit
        #actions.append(currentState[1])
        # set currentState to never visted node popped from nodesToVisit

        # if currentState not in visited:
            # print "currentState: ", currentState
            # print "currentAction: ", currentAction
            # print "visited before loop: ", visited
        if problem.isGoalState(currentState) == True:
            print "the goal state is: ", currentState
            print "currentAction: ", currentAction
            return currentAction
        elif problem.getSuccessors(currentState):
            for Successor, successorAction, cost in problem.getSuccessors(currentState):
                # if Successor not in visited:
                nodesToVisit.push(Successor)
                # print "-- old current action: ", currentAction
                # print "--- currentAction: ", currentAction
                tempAction = list(currentAction) # creating explicit copy
                tempAction+=[successorAction]
                # print "--- Successor: ", Successor
                # print "--- tempAction to append to get to the successor: ", tempAction
                actionsToVisit.push(tempAction)
                # print "--- currentAction end of elif: ", currentAction
                # 
                #print "nodes visited: ", visited
                # pr    int "here?"
        else:
            print "**** it is WRONG ****"
            return False

        visited.add(currentState) # add current state to visited
            # print "nodes visited after loop: ", visited
            # print "nodes to visit: ", nodesToVisit
    # print "********************outside of while loop ********************"
    print "is it empty? ", nodesToVisit.isEmpty()        
    print "final state: ", currentState
    # util.raiseNotDefined()
    return currentAction

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #the series of actions to be taken to get to the successor
    actionsToVisit = util.PriorityQueue()       

    print "cost of actions: West ", problem.getCostOfActions(['West','West','East','East'])
    print "cost of actions: East ", problem.getCostOfActions(['East','East','East','East'])
    print "cost of actions: East ", problem.getCostOfActions(['East','East','East'])
    print "cost of actions: East ", problem.getCostOfActions(['East'])
    print "cost of actions: North ", problem.getCostOfActions(['South','North'])
    print "cost of actions: South ", problem.getCostOfActions(['South'])
    #startState
    startState = problem.getStartState()
    print "startState: ", startState

    #set of states that have been visited
    visited = set() 

    """ check if startState is goal state """
    if problem.isGoalState(startState) == True:
        return None
    
    currentSuccessors = problem.getSuccessors(startState)
    # print "currentSuccessors: ", currentSuccessors
    
    """ initialize nodesToVisit """
    nodesToVisit = util.PriorityQueue()
    # nodesToVisit.push(startState)

    for successor, action, cost in currentSuccessors:
        nodesToVisit.push(successor,cost)
        actionsToVisit.push([action],cost)

        print "nodesToVisit: ", successor
        print "action to nodes to visit", action

    print "actions to visit: ", actionsToVisit
    visited.add(startState)
    currentAction = []
    tempAction = []

    """ Main UCS Logic"""
    while not nodesToVisit.isEmpty():
        # print "********* inside while loop **********"

        """
        pop the top node to be visited and the full series of action it takes
        to get to that node from start state
        """
        currentState = nodesToVisit.pop()
        currentAction = actionsToVisit.pop()

        # print "oooo newly popped currentState : ", currentState
        # print "-- action taken: ", currentAction
        # print " -- remaining actions in actionsToVisit", actionsToVisit
        #actions.append(currentState[1])
        # set currentState to never visted node popped from nodesToVisit

        if currentState not in visited:
            # print "*** current state not visited ***"
            # print "currentState: ", currentState
            # print "currentAction: ", currentAction
            # print "visited before loop: ", visited
            if problem.isGoalState(currentState) == True:
                # print "the goal state is: ", currentState
                # print "currentAction: ", currentAction
                print "final cost: ", problem.getCostOfActions(currentAction)
                return currentAction
            # problem.getSuccessors(currentState)
            #self.walls[nextx][nexty]
            elif problem.getSuccessors(currentState):
                for Successor, successorAction, cost in problem.getSuccessors(currentState):
                    # print "Successor (including visited): ", Successor
                    # print "successorAction (including visited): ", successorAction
                    if problem.walls[Successor[0]][Successor[1]]:
                        break

                    if Successor not in visited and problem.walls[Successor[0]][Successor[1]] == False:
                        # print "-------- not visited ----------"
                        # print "-- old current action: ", currentAction
                        # print "--- currentAction: ", currentAction
                        tempAction = list(currentAction) # creating explicit copy
                        tempAction+=[successorAction]
                        # print "--- Successor: ", Successor
                        # print "--- tempAction to append to get to the successor: ", tempAction
                        actionsToVisit.push(tempAction,problem.getCostOfActions(tempAction))
                        # print "--- currentAction end of elif: ", currentAction
                        # print "priority (cost of tempAction): ", problem.getCostOfActions(tempAction) 
                        nodesToVisit.push(Successor, problem.getCostOfActions(tempAction))
                    # 
                    #print "nodes visited: ", visited
            else:
                print "**** it is WRONG ****"
                return False

            visited.add(currentState) # add current state to visited
            # print "nodes visited after loop: ", visited
            # print "nodes to visit: ", nodesToVisit
    # print "********************outside of while loop ********************"
            
    print "~~~~~~~~final state: ", currentState
    print "final cost: ", problem.getCostOfActions(currentAction)
    util.raiseNotDefined()
    return currentAction

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """Search the node of least total cost first."""
          

    # print "cost of actions: West ", problem.getCostOfActions(['West','West','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East','East','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East','East','East'])
    # print "cost of actions: East ", problem.getCostOfActions(['East'])
    # print "cost of actions: North ", problem.getCostOfActions(['South','North'])
    # print "cost of actions: South ", problem.getCostOfActions(['South'])
    #startState
    startState = problem.getStartState()
    print "startState: ", startState

    #set of states that have been visited
    visited = set() 

    """ check if startState is goal state """
    if problem.isGoalState(startState) == True:
        return None
    
    currentSuccessors = problem.getSuccessors(startState)
    # print "currentSuccessors: ", currentSuccessors
    
    #the series of actions to be taken to get to the successor
    actionsToVisit = util.PriorityQueue() 

    """ initialize nodesToVisit """
    nodesToVisit = util.PriorityQueue()

    for Successor, action, cost in currentSuccessors:
        nodesToVisit.push(Successor,cost+heuristic(Successor,problem))
        actionsToVisit.push([action],cost+heuristic(Successor,problem))

        print "nodesToVisit: ", Successor
        print "action to nodes to visit", action
    # print "actions to visit: ", actionsToVisit
    visited.add(startState)
    currentAction = []
    tempAction = []

    """ Main A* Logic"""
    while not nodesToVisit.isEmpty():
        # print "********* inside while loop **********"

        """
        pop the top node to be visited and the full series of action it takes
        to get to that node from start state
        """
        currentState = nodesToVisit.pop()
        currentAction = actionsToVisit.pop()

        # print "oooo newly popped currentState : ", currentState
        # print "-- action taken: ", currentAction
        # print " -- remaining actions in actionsToVisit", actionsToVisit
        #actions.append(currentState[1])
        # set currentState to never visted node popped from nodesToVisit


        if problem.isGoalState(currentState) == True:
            # print "the goal state is: ", currentState
            # print "currentAction: ", currentAction
            print "final cost: ", problem.getCostOfActions(currentAction)
            return currentAction
        # problem.getSuccessors(currentState)
        #self.walls[nextx][nexty]
        elif problem.getSuccessors(currentState):
            for Successor, successorAction, cost in problem.getSuccessors(currentState):
                # print "Successor (including visited): ", Successor
                # print "successorAction (including visited): ", successorAction
                # if problem.walls[Successor[0]][Successor[1]]:
                #     break

                if Successor not in visited and problem.walls[Successor[0]][Successor[1]] == False:
                    # print "-------- not visited ----------"
                    # print "-- old current action: ", currentAction
                    # print "--- currentAction: ", currentAction
                    tempAction = list(currentAction) # creating explicit copy
                    tempAction+=[successorAction]
                    # print "--- Successor: ", Successor
                    # print "--- tempAction to append to get to the successor: ", tempAction
                    actionsToVisit.push(tempAction, problem.getCostOfActions(tempAction)+heuristic(Successor,problem))
                    # print "--- currentAction end of elif: ", currentAction
                    # print "priority (cost of tempAction): ", problem.getCostOfActions(tempAction) 
                    nodesToVisit.push(Successor, problem.getCostOfActions(tempAction)+heuristic(Successor,problem))
                # 
                #print "nodes visited: ", visited

        visited.add(currentState) # add current state to visited
        # print "nodes visited after loop: ", visited
        # print "nodes to visit: ", nodesToVisit

    # print "********************outside of while loop ********************"            
    print "final state: ", currentState
    print "final cost: ", problem.getCostOfActions(currentAction)
    util.raiseNotDefined()
    return currentAction

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
