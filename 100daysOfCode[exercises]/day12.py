from random import choice
level=str(input("Welcome to Guess the number\nI'm thinking of a number between 1 and 100.\nWhat level do you prefer 'easy' or 'hard'? ")).lower()
attempts=10 if level=='easy' else 5

print(f'You have {attempts} attempts')
number=choice(range(1,101))
guess=int(input('Enter a number\n'))
while attempts>-1:
    if attempts==0:
        print('You run out of attempts')
        break
    elif guess==number:
        print(f'That is right the number is {guess}')
        break
    elif guess>number:
        print('Too Hot')
        attempts-=1
        guess=int(input(f'Attempts left:{attempts}\nEnter a number\n'))
    elif guess<number:
        print('Too Cold')
        attempts-=1
        guess=int(input(f'Attempts left:{attempts}\nEnter a number\n'))
        
    
