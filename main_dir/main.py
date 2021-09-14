def new_game():
    guesses = []
    correct_answer = 0
    for key in question_answer:
        print("--------------------")
        print(key)
        for i in options:
            print(i)
        choice = input("Enter (A, B, C, D): ")
        choice = choice.upper()
        guesses.append(choice)
        correct_answer += check_answer(question_answer.get(key),choice)
    display_value(correct_answer, guesses)

def check_answer(answer,choice):
    if answer == choice:
        print('CORRECT')
        return 1
    else:
        print('WRONG!')
        return 0

def display_value(correct_answer,guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")

    print("Answer: ", end="")
    for key in question_answer:
        print(question_answer[key], end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int(correct_answer/len(question_answer)*100)
    print("Your grade: " + str(score) + " %")

def play_again():
    answer_play = input("You want to play again? (no or yes): ")
    answer_play = answer_play.upper()
    if answer_play == "YES":
        return True
    else:
        return False



question_answer = {"Capital of Russia?:": "C", "Capital of Ukraine?:": "D",
                   "Capital of USA?:": "A", "Capital of Japan?": "B"}
options = ["A. Washington","B. Tokyo","C. Moskow","D. Kiev"]

new_game()
while play_again():
    new_game()
print("Good bye!")