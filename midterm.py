# EE 381 fall 2018 Midterm
# Dong Jae Shin
# 014579836
# start date 10-17-18
# Finish date 10-17-18
#------------------------------------------------------------------------------
import random
total = 0.0
x = -1
frequency = 0.0
range_r = int(input("Enter number of trials for this experiment100: "))

while(x < range_r):
    x = x+1
    print("trial ", x)
    
    # reset sum every iteration
    sum = 0
    
    # run until either one of the sum becomes 3 or 7
    while((sum != 7) and (sum != 3)):
        
        # r is a random decimal number between 0 and 1
        r_1 = random.randint(1,6) 
        r_2 = random.randint(1,6)
            
        #find the sum of two random die
        sum = r_1 + r_2
        
        if sum == 7:
            total = total
        if sum == 3:
            total = total + 1
    
        print(sum, " ")
    
    

frequency = (1.0*total)/(range_r*1.0)
print("probability: ",frequency)