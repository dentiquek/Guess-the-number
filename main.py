

import random

print("Welcome to the game baby! Let's have some fun tonight.")

high_score = float('inf')  # Initial score

while True: #difficulty level
    level = str(input("\nChoose level (easy/medium/hard): ")).lower()
    if level == "easy":
        n = random.randint(1,50)

    elif level == "medium":
        n = random.randint(1,100)

    elif level == "hard":
        n = random.randint(1,500)

    else:
        print("Invalid input. difficulty set to medium")
        n = random.randint(1,100)

    a = -1
    guesses = 0
    while a != n:
        guesses += 1
        a = int(input("Guess the number: "))
        if a > n:
            print("Guess lower number please")
        elif a < n:
            print("Guess higher number please")
        else:
            print("You guessed it right, Baby! In {} attempts".format(guesses))

    if guesses < high_score:
        high_score = guesses
        print(" New High Score!, You're unstoppable baby.")

    play_again = str(input("Do you want to play again? (yes/no): ")).lower()
    if play_again != 'yes':
        print("Thanks for playing! Your best score was {} attempts ".format(high_score))
        break
