# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# GET INITIAL POINT FUNCTION - get_init_point.py

# Importing dependencies
import create_level

# Defining function
def get_init_state(name_file): # Finding AGENT and GOAL in the level
    level = create_level.create_level(name_file) # Getting characters of the txt file
    goal_list = []
    starting_point = 0
    c = 0
    for y in range(len(level)): # Going through the characters and finding AGENT and GOAL
        for x in range(len(level[0])):
            c = c + 1
            character = level[y][x]
            if character == "P":
                starting_state = c
            elif character == "G":
                goal_list.append(c)
                goal_list.append(c + 49)
                goal_list.append(c + 49*2)
                goal_list.append(c + 49*3)
    d = {'starting_state': starting_state, 'goal_points': goal_list} # Joining data
    return d
