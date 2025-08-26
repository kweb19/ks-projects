import random

def result(dice1, dice2):
    print(f'({dice1},{dice2})')
    isplay()

def play():
    global gameCount
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    gameCount += 1
    #print(f'({dice1},{dice2})')
    result(dice1, dice2)
    
def welcome(game):
    print(f'Welcome to {game}!')
    isplay()
    
def quit():
    print('Thanks for playing. Hope to see you soon. Bye for now!')
    
def isplay():
    global gameCount
    if gameCount == 0:
        isPlay = input('Do you want to play the game (Y/N): ?').upper()
    else:
        isPlay = input('Do you want to play again (Y/N): ?').upper()
        
    if isPlay == 'Y':
        play()
    elif isPlay == 'N':
        quit()
    else:
        print('Invalid Choice')
        isplay()
        
    
game = 'Roll the Dice'
gameCount = 0
welcome(game)