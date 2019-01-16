# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# MAIN PROGRAM - dynaQ.py

# Importing dependencies
import nxt_class, create_level, environment, get_init_point, QL,update_env
import numpy as np
import scipy.io as sci
import time

# Connecting to NXT BRICK
print("Pairing to brick...")
b = nxt_class.NXT_BRICK('00:16:53:0E:76:6C')
print("Brick paired!")

# Loading matrices R and T from an empty level and creating an environment
data = sci.loadmat('initial_level.mat')
env = environment.Environment(data)

# Getting initial state of the agent and all the possible goal states
d = get_init_point.get_init_state('initial_level.txt')
starting_state = d.get('starting_state')
goal_list = d.get('goal_points')

# Defining list of free cells and goal cell in the 7x7 grid
cells_free = [9,10,11,12,13,16,17,18,19,20,23,24,25,26,27,30,31,32,33,34,37,38,39,40,41]
cell_goal = [16]

# Defining distance threshold to detect an obstacle
threshold = 13

# Starting main loop
actual_state = starting_state # Defining actual state
finish = False
print("Starting the algorithm...")
while not finish: # Loop
    action_sequence = QL.QL(env,actual_state) # Applying QL and finding the action sequence to apply
    print("Sequence to apply is: " + str(action_sequence))
    for i in action_sequence: # Iterating in the action sequence
        if i==1: # If the action to apply is "GOING FORWARD", checking for obstacles
            distance = b.ultrasonic.get_sample() # Getting a sample of the ultrasonic sensor
            # print("Distance detected: " + str(distance))
            fut_state = env.T1[actual_state-1,:].argmax() + 1 # Getting possible future state (if no obstacles)
            if distance <= threshold: # If an obstacle is detected, finding cell of the obstacle and updating the environment
                if 1 <= actual_state <= 49: # North orientation
                    orientation = 0
                    obstacle = actual_state - 7
                elif 50 <= actual_state <= 98: # South orientation
                    orientation = 1
                    obstacle = actual_state + 7 - 49
                elif 99 <= actual_state <= 147: # East orientation
                    orientation = 2
                    obstacle = actual_state + 1 - 49*2
                elif 148 <= actual_state <= 196: # West orientation
                    orientation = 3
                    obstacle = actual_state - 1 - 49*3
                cells_free.remove(obstacle) # Removing the obstacle cell from the free cells list
                print("Obstacle detected! Updating environment")
                env = update_env.update_env(cells_free,cell_goal,env) # Updating environment
                # env = update_R_T.update_R_T(actual_state,env)
                break # Returning to the main loop
            else: # If an obstacle is not detected, applying action to the robot
                print("Going forward!")
                b.move_tile(70,1.5) # "GOING FORWARD" action
        elif i==2: # If the action to apply is "ROTATE 90 RIGHT", finding future state and applying action
            fut_state = env.T2[actual_state-1,:].argmax() + 1 # Getting future state
            print("Rotating 90 right!")
            b.rotate(65,1.2) # "ROTATE 90 RIGHT" action
        elif i==3: # If the action to apply is "ROTATE 90 LEFT", finding future state and applying action
            fut_state = env.T3[actual_state-1,:].argmax() + 1 # Getting future state
            print("Rotating 90 left!")
            b.rotate(-65,1.2) # "ROTATE 90 LEFT" action

        time.sleep(5) # Applying a time delay
        if env.isGoal(actual_state,i): # If the agent has arrived to the goal, finishing the main loop
            print("Goal has been achieved!")
            finish = True
            actual_state = fut_state # Updating the actual state
            break
        actual_state = fut_state # Updating the actual state

print("Disconnecting brick...")
b.disconnect() # When the goal has been achieved, disconnect from the NXT BRICK
print("Brick disconnected!")
