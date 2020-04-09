#Quiz Game
#Created by Jonathan Lawrence
#4/9/2020

TOTAL_QUESTIONS = 5

QUESTION_1 = " There are 7 days in a week"
QUESTION_1_ANSWER = 'true'

QUESTION_2 = " There are 40 states in the USA"
QUESTION_2_ANSWER = 'false'

QUESTION_3 = " The square root of 36 is 6"
QUESTION_3_ANSWER = 'true'

QUESTION_4 = ' The word "run" is a noun'
QUESTION_4_ANSWER = 'false'

QUESTION_5 = ' The opposite of "up" is "down"'
QUESTION_5_ANSWER = 'true'

ANSWER_PROMPT = (" True or false? (T/F):  ")
incorrect_answers = 0
correct_answers = 0
play_again = ''

#Compare user's answer with the real answer and increment correct/incorrect total by 1
def calculate_answer(attempt, answer):
    global correct_answers
    global incorrect_answers
    if attempt.lower() in answer:
        correct_answers += 1
    else:
        incorrect_answers += 1    

while 'n' not in play_again.lower():

    #Welcome user and explain how the quiz works
    print(" Hello! Welcome to the quiz game! You will be asked {} true or false questions. Your score will be displayed at the end. Good luck!\n\n".format(TOTAL_QUESTIONS))


    #Begin quiz and get user input
    answer_1 = input("{}. {}".format(QUESTION_1 ,ANSWER_PROMPT))  
    calculate_answer(answer_1, QUESTION_1_ANSWER)

    answer_2 = input("{}. {}".format(QUESTION_2 ,ANSWER_PROMPT))
    calculate_answer(answer_2, QUESTION_2_ANSWER)

    answer_3 = input("{}. {}".format(QUESTION_3 ,ANSWER_PROMPT))
    calculate_answer(answer_3, QUESTION_3_ANSWER) 

    answer_4 = input("{}. {}".format(QUESTION_4 ,ANSWER_PROMPT))
    calculate_answer(answer_4, QUESTION_4_ANSWER)

    answer_5 = input("{}. {}".format(QUESTION_5 ,ANSWER_PROMPT))
    calculate_answer(answer_5, QUESTION_5_ANSWER)

    #Calculate percentage of correct answers
    percent =  int((correct_answers / TOTAL_QUESTIONS) * 100)

    print ("\n\n Correct answers: {}\n Incorrect answers: {}\n".format(correct_answers, incorrect_answers))
    print(" You scored {}% on this quiz.\n\n".format(percent))

    incorrect_answers = 0
    correct_answers = 0

    play_again = input(" Would you like to play again? (Answer Y/N): ")