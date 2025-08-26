import random


def welcome(game):
    print(f'Welcome to the {game}')
    is_play()
    
    
def quit():
    print('Thanks for playing. See you next time!')


def is_play():
    if game_count == 0:
        is_play = input('Do you want to play? Y/N: ').upper()
    else: 
        is_play = input('Do you want to play again? Y/N: ').upper()
        
    if is_play == 'Y':
        print('Kudos! Lets get started')
        play()
    else:
        quit()
        
def score_calculate(count):
    if count <= chances:
        print(f'Congratulations! You won the game in {count} turns')
    else:
        print('You Lose! Better luck next time')
    
    is_play()
        

def play():
    global game_count
    game_count += 1
    count = 0
    number  = random.randint(1,100)
    while (count <= chances):
        guess = int(input('Guess the number: '))
        if number == guess:
            count += 1
            print(f'You guessed it right!')
            break
        
        elif number > guess:
            count += 1
            print('You are way too low! Try a higher number.')
        elif number < guess:
            count += 1
            print('You are way too far! Try a smaller number.')
    
    score_calculate(count)
        

#Variables
game = 'Number Guessor Game!'
game_count = 0
chances = 7

welcome(game)
