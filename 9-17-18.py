# EE 381 fall 2018 Project 3
# Dong Jae Shin
# 014579836
# start date 9-17-18
# Finish date 9-17-18
#------------------------------------------------------------------------------
import random

print('Program simulates Bernoulli random variables.')

p = float(input('Enter the probability of success.'))

t = int(input('Enter the number of trials.'))

for i in range(t):
    r = random.uniform(0,1) # include 0 not 1
    
    if r < p:
        print('1', end = ' ')
    else:
        print('0', end = ' ')
        
        