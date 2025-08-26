#5Questions & Answers
#user_input on answers
#Calculate Marks
#Print Results

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


def score_calculate(marks):
    total = len(ques.keys())
    
    if marks == total:
        print('Congratulations! You won the game')
    else: 
        print('You Lose! Better luck next time')
        
    is_play()
    

def play():
    marks = 0
    global game_count
    game_count += 1
    
    for item in ques:
        print(f'Question: {item}')
        
        if ques[item] == input('Answer: ').lower():
            print('Correct')
            marks += 1
        else:
            print('Incorrect')
            
    score_calculate(marks)
    
    
# Variables:
game = 'Quiz Game!'
game_count = 0
ques = {
     'Ques1': 'a'
    ,'Ques2': 'b'
    ,'Ques3': 'c'
    ,'Ques4': 'd'
    ,'Ques5': 'e'
    ,'Ques6': 'f'
}

welcome(game)
