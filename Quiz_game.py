
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("enter (A, B, C, or D) :")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
# --------------------------------


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT ANSWER")
        return 1
    else:
        print("INCORRECT ANSWER")
        return 0


# --------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULT :")
    print("----------------------------")
    print("Answers :", end="")

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses :", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is :", str(score), "%")
# --------------------------------


def play_again():
    response = input("Do you want to play again ?? :(yes or No) :")
    response = response.upper()

    if response == "yes":
        return True
    else:
        return False


# --------------------------------

questions = {
    "who created Python? :": "A",
    "what year was Python created? :": "B",
    "Python is tribute to which comedy group? : ": "C",
    "Is the Earth round ?": "A"
}

options = [["A. Guido an Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smash", "C. Monty Python", "D. Snl"],
           ["A. True", "B. False", "C. Sometimes", "D. Triangle"]]

new_game()
while play_again():
    new_game()

print("Game Over")
