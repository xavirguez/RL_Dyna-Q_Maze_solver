# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# POSSIBLE ACTIONS FUNCTION - possible_actions.py

# Defining function
def possible_actions(state,env):
    # Rotating actions will be always available in free cells
    # It is only needed to check if "GOING FORWARD" action is possible
    for i in range(len(env.T1[state-1])):
        if env.T1[state-1][i] == 1:
            return [1,2,3]
    return [2,3]
