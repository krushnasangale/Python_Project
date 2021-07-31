import random

choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer = random.choice(choices)

while True:

    player = 'none'
    while player not in choices:
        player = int(input("enter value between 0 to 10 :"))
    print("player input :", player)

    if player != computer:
        print("lets Try Again... Better luck next Time????")

        if computer <= 3:
            print("number is too small")
        elif 4 <= computer < 7:
            print("number is medium")
        else:
            print("number is too big")

    if player == computer:
        print("Ohh .... Congrats!!!, You won this Match..")
        break
