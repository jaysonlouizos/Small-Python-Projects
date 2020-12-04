import random

computer_number = random.randint(1,100)

guess = random.randint(1,100)

high = 101
    
low = 0

attempts = 0

def computer_guess(high,low,computer_number,guess):
    
    while guess != computer_number:
        
        guess = int((low + high)/2)
        
        if computer_number > guess:
            guess = int((high + guess)/2)
            print (guess)
            
            if computer_number > guess:
                low = guess
            
            elif computer_number < guess:
                high = guess

        elif computer_number < guess:
            guess = int((low + guess)/2)
            print (guess)
            
            if computer_number > guess:
                low = guess
            
            elif computer_number < guess:
                high = guess


computer_guess(high,low,computer_number,guess)
