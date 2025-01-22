class Quest:
    ques_list = {
            'What is the abbreviation of CPU? ':'Central Processing Unit',
            'What is the abbreviation of CU? ':'Control Unit',
            'What is abbreviation of GK? ':'General Knowledge'
        }
    score = 0
    count = 0

def participate():
    print("Welcome to the quiz game!")
    isPlay = input('Are you ready to play(Yes/No)?')
    if isPlay == 'Yes':
        play()
        
                
def play_again():
    play_again = input('Do you want to play again? (Yes/No): ')
    if play_again == 'Yes':
        participate()
        

def play():
    q1 = Quest()
    total_score = len(q1.ques_list)
    
    for item in q1.ques_list:
        q1.count = q1.count + 1
        print(f'Question {q1.count}: ')
        ans = input(item)
        if ans == q1.ques_list[item]:
            print('Corrent Answer.')
            q1.score += 1
        else:
            print('Wrong Answer. Try next question.')
    score(total_score, q1.score)

def score(total_score, score):
    if score == total_score:
        print('Congratulations! You won the game!')
        play_again()
    else:
        print(f'Total Score = {score}. Better luck next time!')
        play_again()
        

            
# sourcery skip: use-named-expression
participate()

print('Thanks for playing. Hope you enjoyed the game!')