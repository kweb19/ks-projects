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
        print('Kudos! Lets get started\n')
        play()
    else:
        quit()
        
def score_calculate(comp_win,user_win):
    if user_win == comp_win:
        print('Ahh! Its a tie')
    elif user_win >comp_win:
        print('Congratulations! You Won the game.')
    else:
        print('You Lose the game.')
    
    is_play()
        
        
def play():
    global game_count
    game_count += 1
    comp_win = 0
    user_win = 0
    count = 0
    
    while (count < best_of):
        comp_choice = items[random.randint(1,3)]
        user_choice  = input('User Choice: ').lower()
        print(f'Computer Choice: {comp_choice}')
        
        if comp_choice == user_choice:
            print('Result: Its a Tie')
            print('\n****************')
            continue
        elif rules[comp_choice] == user_choice:
            comp_win += 1
            count += 1
            print('You Lose!')
        elif rules[user_choice] == comp_choice:
            user_win += 1
            count += 1
            print('You Won!')
        print('\n****************')
    
    score_calculate(comp_win,user_win)
            

#Variables
game = 'Rock Paper Scissor Game!'
game_count = 0
best_of = 3
items = {
     1: 'rock'
    ,2: 'paper'
    ,3: 'scissor'
}
rules = {
     'rock': 'scissor'
    ,'scissor': 'paper'
    ,'paper': 'rock'
}
welcome(game)
