
import random
winning_numbers = [
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100)]

balance = 0

rounds_played = 10

spent = 0

def num_matches(winning_numbers,balance,rounds_played,spent):
    winners = 0
    while rounds_played > 0:
        winning_numbers = [
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100)]
        balance = balance - 2
        spent = spent + 2
        ticket = [
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100),
        random.randint(1,100)]
        
        if winners == 1:
            balance = balance + 4
        elif winners == 2: 
            balance = balance + 7
        elif winners == 3: 
            balance == balance + 100
        elif winners == 4: 
            balance = balance + 50000
        elif winners == 5: 
            balance = balance + 1000000
        elif winners == 6: 
            balance = balance + 25000000

        winners = 0 
        
        for i in ticket:
            if i in winning_numbers:   
                winners += 1
        rounds_played -= 1
    return balance


balance = num_matches(winning_numbers,balance,rounds_played,spent)    
roi = int(balance / (rounds_played * 2) * 100)
print(f'You played {rounds_played} games and earned {balance}\nThat gives you an roi of {roi}%')
if roi < 0:
    print('What did it cost you?\nEverything')
