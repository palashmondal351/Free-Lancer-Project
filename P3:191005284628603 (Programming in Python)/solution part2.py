#!/usr/bin/env python3
#doprofessional task 2
# This is a guess the number game.
import random # import the random module to generate the random number
print('Welcome to my Guess the number program!') 
num=random.randint(1,10) # geneating the random number
count=0 # counter initialization

while True: #contineu the while loop untill it's become true. 
    try:
        guss=int(input('Please guess a number between 1 and 10:')) # to check integer 
        if (guss>0 and guss<11): # to check user input range of the number
            if(guss>num): # guss number is greater than actual
                print('Too high')
                count+=1
            elif(guss<num): # guss number is smaller than actual
                print('Too low')
                count+=1
            else: # guss number is equal with actual
                print('You guessed it! It took you',count, 'attempts')
                break # when number is found break the statement. 
        else: pass           
    except: print('Numbers only!')