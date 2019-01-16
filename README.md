# RL_Dyna-Q_Maze_solver
This is the code development of all the implementation of a Dyna-Q algorithm for navigation purposes developed by Eneko Herrero Taboada and Xavier Rodríguez Hernández for the subject Robot Learning.

Master in Automatic Control & Robotics (MUAR), ETSEIB (UPC), Barcelona, 2019.

Instructions to use:
1) Check for the MAC address of the NXT brick you want to connect and write at the beginning of the "dynaq.py" program.
2) Modify the text file "initial_level.txt" to include a N x N empty grid with walls as obstacles. Put also the initial position of the agent with an "P" and the goal position with a "G".
3) Run in MATLAB the function expressed in "create_environment.m" giving as input the name of the text file mentioned above. This will save the initial matrices R, T1, T2, T3 in a ".mat" file.
4) Check the free cells of the empty environment and modify the variable "cells_free" of "dynaq.py", as well as the the cell of the goal in the variable "cell_goal" .
5) Get the robot ready in the real environment.
6) Turn on Bluetooth settings and run "dynaq.py" program in Python 2.7.
7) Enjoy!
