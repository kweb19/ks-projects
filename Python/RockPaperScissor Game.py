import random      
#def score_calc(user_count,computer_count):
def quit():
    print('Thanks for playing. Hope you enjoyed the game!')
    
def participate():
    print('Welcome to Rock, Paper and Scissors Game!')
    try:
        best_of = int(input('How many games you wish to play(1/3/5)?'))
        play(best_of)
    except ValueError:
        print('Enter a valid choice!')
        participate()    
    
def play_again():
    play_again = input('Do you want to play again? (Yes/No): ').lower()
    if play_again == 'yes':
        participate()
    else:
        quit()
    
def score_calc(user_count,computer_count):
    if user_count > computer_count:
        print(f'User wins by {user_count - computer_count} rounds')
    else:
        print(f'Computer wins by {computer_count - user_count} rounds')
    play_again()
    
def play(best_of):  # sourcery skip: move-assign
    rule_book = {
    'rock':'scissor',
    'paper':'rock',
    'scissor':'paper'
    }
    user_count = 0
    computer_count = 0
    while best_of > 0:
        computer_choice = random.choice(list(rule_book.keys()))
        user_choice = input('Choose btw rock, paper and scissor!').lower()
        
        if user_choice not in list(rule_book.keys()):
            print('Enter a valid choice!')
            continue
        
        if user_choice == computer_choice:
            print('Its a tie')
        elif  rule_book[user_choice] == computer_choice:
            print(f'Computer Choice: {computer_choice}\nUserChoice: {user_choice}\n User Wins!')
            user_count += 1
            best_of -= 1
        else:
            print(f'Computer Choice: {computer_choice}\nUserChoice: {user_choice}\n Computer Wins!')
            computer_count += 1
            best_of -= 1
    score_calc(user_count,computer_count)
    

participate()