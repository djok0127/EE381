# EE 381 fall 2018 Project 3
# Dong Jae Shin
# 014579836
# start date 9-19-18
# Finish date 9-19-18
#------------------------------------------------------------------------------

import random

while(1):
    # Enter spec.'s
    p = float(input("Enter the probability of going from 0 to 1. "))
    q = float(input("Enter the probability of going from 1 to 0. "))
    
    S = random.randint(0,1) # S is assigned either 0 or 1
    
    
    print(S, end = '') # print original location
    
    for i in range(24):
        
        r = random.uniform(0,1) # r is a random decimal number between 0 and 1
        
        # Markov Model
        if S == 0 and r < p:
            S = 1
        elif S == 1 and r < q:
            S = 0
        print(S, end = '') # print steps