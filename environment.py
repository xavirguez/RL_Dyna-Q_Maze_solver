# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# ENVIRONMENT CLASS - environment.py

# Importing dependencies
import numpy as np

# Defining class
class Environment:
    def __init__(self,data): # Initial parameters
        # Matrices R and T
        self.R = data.get('R')
        self.T1 = data.get('T1')
        self.T2 = data.get('T2')
        self.T3 = data.get('T3')
        # Number of states and number of actions
        self.num_states = len(self.R)
        self.num_actions = 3
        # Initializing Q matrix to zeros
        self.Q = np.zeros((self.num_states,self.num_actions))

    def isGoal(self,state,action): # Checking goal method
        if self.R[state-1][action-1] == 500:
            return 1
        else:
            return 0
