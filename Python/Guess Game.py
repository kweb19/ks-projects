import random

def play_again():
    play_more = input('Do you want to play again (Yes/No)?').lower()
    if play_more == 'yes':
        participate()
    else:
        quit()
        
        
def play_game():  # sourcery skip: move-assign
    guess_count=0
    num = random.randint(0,10)
    while True:
        guess_count = guess_count + 1
        guess = int(input('Guess the number btw 0 and 10: '))
        if guess == num:
            print(f'Congrats! You guessed it right at {guess_count}th place!')
            break
        elif guess < num:
            print('You guess too low. Try Again!')
        elif guess > num:
            print('You guess too far. Try Again!')
        else:
            print('Enter a valid number!')
    play_again()

def participate():
    isPlay = input('Welcome to the Guessing Game!\nAre you ready to play (Yes/No)').lower()
    if isPlay == 'yes':
        play_game()


def quit():
    print('Thanks for playing. Hope you enjoyed the game!')


participate()

