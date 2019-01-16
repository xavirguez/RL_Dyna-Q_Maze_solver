# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# CREATE LEVEL FUNCTION - create_level.py

# Defining function
def create_level(name_file): # Opening .txt file, reading it and returning its characters
    file = open(name_file,'r')
    level = file.readlines()
    for i in range(len(level)):
        level[i] = level[i][0:len(level[i])-1]
    file.close()
    return(level)
