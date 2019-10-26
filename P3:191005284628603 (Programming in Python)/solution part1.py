#!/usr/bin/env python3
## doprofessional order3 of task 1
def winner(Chevy, Ford): 
    if(len(Chevy)==8 and len(Ford)==8): # validation check for 8 input for both
        print('And the winners are:')
        c,f=0,0 # winning count initialization
        
        for j in range(8): # to check the winning for 8 iteration
            
            if(Chevy[j]>Ford[j]): # checking condition for Ford winning
                print('Ford by',(Chevy[j]*10 - Ford[j]*10)/10,'sec' )
                f+=1 # Ford winning count increment
                
            elif(Chevy[j]==Ford[j]): print('Tie!') # Tie Condition checking
            
            else: # checking condition for Chevy winning
                print('Chevy by',(Ford[j]*10 - Chevy[j]*10) / 10,'sec' ) 
                c+=1
                
        if(c>f): print('And the winning team is: C H E V E !') # Chevy winning check
        elif(c==f):print('Tie!') # Tie check
        else: print('And the winning team is: F O R D !') # Ford winning check 
        
    else: pass # return nothing just pass the condition. 
    
#-------------- Taking user input for 8 cars of Chevy and Ford--------------------   
Chevy=[]; Ford=[]
try:
    print('---Input Chevy Times---')
    # takes user input for 8 times
    for i in range(1,8+1): Chevy.append(float(input('Enter time for Chevy Car %d:' %i)))
    print('---Input Ford Times---')
    for i in range(1,8+1): Ford.append(float(input('Enter time for Ford Car %d:' %i)))
except: print('Invalid Input!!')

winner(Chevy, Ford)  # call the function  

