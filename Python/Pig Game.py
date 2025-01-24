import random

class Player:
    dice = 0
    name = ''
    score = 0
    win_score = 20
    
def create_player():
    player = Player()
    player.name = input('Enter the player name: ')
    return player

def quit():
    print('Thanks for playing. Hope you enjoyed the game!')

def roll(dice):
    dice = random.randint(1,6)
    return dice

def score_board(name,score):
    print(f'{name} Score: {score} \n')
    
def play_game(players):  # sourcery skip: assign-if-exp, hoist-similar-statement-from-if, hoist-statement-from-if
    count = 1
    while count == 1:
        for object in players:
            roll_dice = input(f'{object.name}. Want to roll a dice? [Y/N]').lower()
            if roll_dice == 'y':
                object.dice = roll(object.dice)
                if object.dice != 1:
                    object.score = object.score + object.dice
                    score_board(object.name,object.score)
                else: 
                    object.score = 0
                    score_board(object.name,object.score)
            else: 
                score_board(object.name,object.score)
            if object.score >= object.win_score:
                print(f'Congratulations {object.name}!You have achieved the winning score: {object.score} \n')
                count = 0
                quit()
                break
        
        
def participate():
    print('Welcome to the PIG GAME!')
    num_player = int(input('Enter the number of players: '))
    players = []
    while num_player != 0:
        player = create_player()
        players.append(player)
        print(players)
        num_player -= 1
    
    play_game(players) 
        
        
participate()
        
        

    