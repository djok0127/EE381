# Dong Jae Shin
# 014579836
# start date 9-5-18
# Finish date
#------------------------------------------------------------------------------
# In this project we'll make our own random number generator, (rng).
# We'll solve a probability problem with our rng and simulation.
#------------------------------------------------------------------------------

# Declaring Constants
N = 10000 # The norm.
A = 4857 # The adder.
M = 8601 # The multiplier.

# A seed is required.
S = 0
Counter = 0 # Accumulator Initial Value

#for n in range(99):
#       S = (S * M + A) % N
#       r = S/N
#       print("%.4f"%r)

import math # for floor function
# ---------------------------------------------------------------------------
# Below is the simulation of the probabilty problem.      
# ---------------------------------------------------------------------------

Ball = [0, 0, 0] # The balls are not in the cans.

E = int(input('How many experiments are to be performed? '))

for j in range(E):
    
    # This inner loop is the experiment
    
    for i in range(3): # 0 to 2
        S = (S * M + A) % N # our rng
        r = S/N             # Numbwers on interval [0,1)
        
        Can_Number = math.floor(r * 5 + 1)
        Ball[i] = Can_Number 
    if((Ball[0] != Ball[1] ) and (Ball[1] != Ball[2]) and (Ball[2] != Ball[0])):
        Counter = Counter + 1 # Count the number of the desired outcomes
        
p = Counter / E

print(" The probability that three balls landing in different can is ", p,".")