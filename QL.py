# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# Q-LEARNING ALGORITHM FUNCTION - QL.py

# Importing dependencies
import possible_actions
import numpy as np

# Defining function
def QL(env,initial_state):
    # Defining parameters
    print("Starting new QL algorithm with initial state " + str(initial_state) + ' ...')
    env.Q = np.zeros((env.num_states,env.num_actions)) # Reseting Q matrix of the enviroment to zeros
    gamma = 0.8
    alpha = 0.7
    fut_state = -1
    episode = 500

    # Training the agent
    print("Starting training part...")
    for e in range(int(episode)): # Main loop - episodes
        finish = False
        actual_state = initial_state
        fut_state = actual_state
        action_sequence = []
        while not finish: # Secondary loop - while not arriving to goal, training
            # print('Epoch: ', i)
            # print("We are in state:", actual_state + 1)
            pos_actions = possible_actions.possible_actions(actual_state,env) # Getting possible actions in the current state
            action = np.random.choice(pos_actions) # EXPLORATION - Getting randomly 1 of the possible actions
            # print('We execute action: ',action)
            # Getting future state
            if action == 1:
                fut_state = env.T1[actual_state-1,:].argmax() + 1
            elif action == 2:
                fut_state = env.T2[actual_state-1,:].argmax() + 1
            elif action == 3:
                fut_state = env.T3[actual_state-1,:].argmax() + 1
            # print('The future state will be: ', fut_state + 1)
            # Updating Q matrix
            env.Q[actual_state-1,action-1] = env.Q[actual_state-1,action-1] + alpha*(env.R[actual_state-1,action-1] + gamma * max(env.Q[fut_state-1,:]) - env.Q[actual_state-1,action-1])
            # Checking if goal is achieved
            if env.isGoal(actual_state,action): # If goal is achieved, starting another episode
                actual_state = fut_state # Updating current state
                finish = True
                # print("We arrived to Goal!")
            else: # If not, going through the episode
                actual_state = fut_state # Updating current state
    print("Finished training " + str(episode) + " episodes!")
    # Validation part
    print("Starting validation part...")
    actual_state = initial_state
    fut_state = actual_state
    action_sequence = []
    goal = False
    while not goal: # Main loop - While not arriving to goal, validating
        # Getting action to apply and updating to the action sequence list
        action = np.argmax(env.Q[actual_state-1,:]) + 1
        action_sequence.append(action)
        # Getting future state
        if action == 1:
            fut_state = env.T1[actual_state-1,:].argmax() + 1
        elif action == 2:
            fut_state = env.T2[actual_state-1,:].argmax() + 1
        elif action == 3:
            fut_state = env.T3[actual_state-1,:].argmax() + 1
        # Checking if goal is achieved
        if env.isGoal(actual_state,action): # If goal is achieved, finishing validation
            goal = True
        actual_state = fut_state # Updating current state
    print("New action sequence founded!")
    return action_sequence # Returning action sequence
