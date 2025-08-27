import random

def result(count):
    print(f'Congratulations! You guessed it right in {count} turns')
    
def play():
    count = 0
    global gameCount
    gameCount += 1
    guessNum = random.randint(1,100)
    while (True):
        count += 1
        userChoice = int(input('Guess the number between 1 and 100: '))
        if userChoice == guessNum:
            result(count)
            break
        elif userChoice > guessNum:
            print('Too High!')
        elif userChoice < guessNum:
            print('Too Low!')
    isplay()
    
def isplay():
    if gameCount == 0:
        choice = input('Do you want to play the game (Y /N)? ').upper()
    else:
        choice = input('Do you want to play again (Y /N)? ').upper()
        
    if choice =='Y':
        print("Let's get started!")
        play()
    elif choice == 'N':
        exit_game()
    else:
        print('Invalid Choice!')
        isplay()
        
def exit_game():
    print('Thanks for paticipating, Bye for now!')

def welcome():
    print('Welcome to Number Guessing Game!')
    isplay()
    
    

gameCount = 0
welcome()