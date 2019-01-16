# ENEKO HERRERO TABOADA - XAVIER RODRIGUEZ HERNANDEZ
# MOBILE ROBOT NAVIGATION BASED IN Q-LEARNING
# UPDATING ENVIRONMENT FUNCTION - update_env.py

# Importing dependencies
import environment
import numpy as np
import scipy.io as sci

# Defining functions
def update_env(cells_free,cell_final,env):
    # Defining parameters - num actions, orientations, states and grid size
    num_actions = 3
    num_orientations = 4
    num_states = 196
    gs = 7

    # Updating T1 matrix
    T1_aux = np.zeros((num_states/num_orientations,num_states,num_orientations))
    for i in range(num_orientations):
        if i==0:
            for j in cells_free:
                s = j - gs
                if s in cells_free:
                    T1_aux[j-1,s+gs*gs*0-1,i] = 1
        elif i==1:
            for j in cells_free:
                s = j + gs
                if s in cells_free:
                    T1_aux[j-1,s+gs*gs*1-1,i] = 1
        elif i==2:
            for j in cells_free:
                s = j + 1
                if s in cells_free:
                    T1_aux[j-1,s+gs*gs*2-1,i] = 1
        elif i==3:
            for j in cells_free:
                s = j - 1
                if s in cells_free:
                    T1_aux[j-1,s+gs*gs*3-1,i] = 1
    T1 = np.append(T1_aux[:,:,0],T1_aux[:,:,1],axis = 0)
    T1 = np.append(T1,T1_aux[:,:,2],axis = 0)
    T1 = np.append(T1,T1_aux[:,:,3],axis = 0)

    # Updating T2 matrix
    T2_aux = np.zeros((num_states/num_orientations,num_states,num_orientations))
    for i in range(num_orientations):
        if i==0:
            for j in cells_free:
                T2_aux[j-1,num_states/num_orientations*2+j-1,i] = 1
        elif i==1:
            for j in cells_free:
                T2_aux[j-1,num_states/num_orientations*3+j-1,i] = 1
        elif i==2:
            for j in cells_free:
                T2_aux[j-1,num_states/num_orientations*1+j-1,i] = 1
        elif i==3:
            for j in cells_free:
                T2_aux[j-1,num_states/num_orientations*0+j-1,i] = 1
    T2 = np.append(T2_aux[:,:,0],T2_aux[:,:,1],axis = 0)
    T2 = np.append(T2,T2_aux[:,:,2],axis = 0)
    T2 = np.append(T2,T2_aux[:,:,3],axis = 0)

    # Updating T3 matrix
    T3_aux = np.zeros((num_states/num_orientations,num_states,num_orientations))
    for i in range(num_orientations):
        if i==0:
            for j in cells_free:
                T3_aux[j-1,num_states/num_orientations*3+j-1,i] = 1
        elif i==1:
            for j in cells_free:
                T3_aux[j-1,num_states/num_orientations*2+j-1,i] = 1
        elif i==2:
            for j in cells_free:
                T3_aux[j-1,num_states/num_orientations*0+j-1,i] = 1
        elif i==3:
            for j in cells_free:
                T3_aux[j-1,num_states/num_orientations*1+j-1,i] = 1
    T3 = np.append(T3_aux[:,:,0],T3_aux[:,:,1],axis = 0)
    T3 = np.append(T3,T3_aux[:,:,2],axis = 0)
    T3 = np.append(T3,T3_aux[:,:,3],axis = 0)

    # Updating R matrix
    R_aux = -500*np.ones((num_states/num_orientations,num_actions,num_orientations))
    for i in cells_free:
        left = i - 1
        if left in cells_free:
            R_aux[left-1,0,2] = -10
        top = i - gs
        if top in cells_free:
            R_aux[top-1,0,1] = -10
        right = i + 1
        if right in cells_free:
            R_aux[right-1,0,3] = -10
        bottom = i + gs
        if bottom in cells_free:
            R_aux[bottom-1,0,0] = -10

    for i in range(num_orientations):
        for j in cells_free:
            R_aux[j-1,1,i] = -10
            R_aux[j-1,2,i] = -10

    for i in cell_final:
        R_aux[i-1,1,0] = 500
        R_aux[i-1,2,0] = 500
        R_aux[i-1,1,1] = 500
        R_aux[i-1,2,1] = 500
        R_aux[i-1,1,2] = 500
        R_aux[i-1,2,2] = 500
        R_aux[i-1,1,3] = 500
        R_aux[i-1,2,3] = 500
        left = i - 1
        left_2 = i - 2
        for j in cells_free:
            if left in cells_free:
                R_aux[left-1,0,2] = 500
            if left_2 in cells_free:
                R_aux[left_2-1,0,2] = 100
        top = i - gs
        top_2 = i - 2*gs
        for j in cells_free:
            if top in cells_free:
                R_aux[top-1,0,1] = 500
            if top_2 in cells_free:
                R_aux[top_2-1,0,1] = 100
        right = i + 1
        right_2 = i + 2
        for j in cells_free:
            if right in cells_free:
                R_aux[right-1,0,3] = 500
            if right_2 in cells_free:
                R_aux[right_2-1,0,3] = 100
        bottom = i + gs
        bottom_2 = i + 2*gs
        for j in cells_free:
            if bottom in cells_free:
                R_aux[bottom-1,0,0] = 500
            if bottom_2 in cells_free:
                R_aux[bottom_2-1,0,0] = 100
    R = np.append(R_aux[:,:,0],R_aux[:,:,1],axis = 0)
    R = np.append(R,R_aux[:,:,2],axis = 0)
    R = np.append(R,R_aux[:,:,3],axis = 0)

    # Updating environment
    env.T1 = T1
    env.T2 = T2
    env.T3 = T3
    env.R = R

    # Saving results (only for testing)
    # sci.savemat('ret_update.mat',{'T1':T1,'T2':T2,'T3':T3,'R':R})

    return env
