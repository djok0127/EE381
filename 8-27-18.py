# Dong Jae Shin
# 014579836
#start date 8-27-18
# Finish date 8-29-18
#-------------------------------------------------------------
# In this project we’ll only be considering population data.
# Brief programs for determining summary statistics of inputted data are written
#--------------------------------------------------------------------
L = [] # Empty list for data
v = 1 # initialize a variable

print("you’ll be prompted to enter nonnegative integers. \n")
print('when you want to stop enter the word stop.')

while v == 1:
    try:
        l = int(input('Enter a nonnegative integer.'))
        L.append(l)
    except ValueError:
        print('input halted.')
        print('\n')
        v = 0
        
print('you inputted the numbers listed', L)
print('\n')
#------------------------------------------------------

# below is the calculation of the mean.
s = sum(L) # The sum of the inputed numbers.
N = len(L) # The number of the numbers entered.

mean = s/N # The arithmetic average

print('The mean of the numbers is', mean , '.')

#---------------------------------------------------------

# Below is the calculation of the median.
# The numbers need to be sorted.
L.sort()
# Further it is relevant whether there is an odd number of numbers or an even numbers
if N % 2 == 0: # The even case
    m1 = N/2
    m2 = (N/2) + 1 # The two middle positions
    
    m1 = int(m1)
    m2 = int(m2) # Casting as integers
    
    m1 = m1 - 1
    m2 = m2 - 1 # Correct one off error
    
    median = (L[m1] + L[m2])/2

else: # the odd case
    
    m = (N + 1)/2
    m = int(m) - 1
    median  = L[m]
    
print('The median of the numbers is ', median, '.')
print('\n')
#------------------------------------------------------------------------------

from collections import Counter

c = Counter(L) # Creates tuples list (element, frequency)
freq = c.most_common() # most common method
max_occur = freq[0][1] # The largest frequency assigned to max_occur

if max_occur != 1:
    modes = [] # Empty List
    for m in freq:
        if m[1] == max_occur: # looking for all frequencies the same as max_occur
            modes.append(m[0])
    print('The mode(s) are: ', modes)
else:
    print('There is no mode.')
print('\n')
#------------------------------------------------------------------------------

# Below is the calculation of the range.
highest = max(L)
lowest = min(L)

Range = highest - lowest
print('The range is. ', Range, '.')
print('\n')

#------------------------------------------------------------------------------
# Below is the calculation of the variance.
S = 0 # initial value of accumulator.
for n in L:
    x = (n - mean)**2
    S = S + x
    
variance = S/N

print('The variance is. ', variance, '.')
print('\n')
#------------------------------------------------------------------------------

# Below is the calculation of the standard deviation

import math
standard_deviation = math.sqrt(variance)
print('The standard deviation is. ', standard_deviation, '.')
#------------------------------------------------------------------------------