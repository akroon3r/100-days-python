# This is a sample Python script.
from guess import check_guess
from random import randint
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number_to_guess = randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    choose_difficulty = False
    # define attempt number
    while not choose_difficulty:
        if difficulty == 'easy':
            attempts = 10
            choose_difficulty = True
        elif difficulty == 'hard':
            attempts = 5
            choose_difficulty = True
        else:
            difficulty = input("You did not choose a difficulty. Type 'easy' or 'hard': ").lower()

    print(f"You have {attempts} attempts remaining to guess the number.")

    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        if check_guess(guess = guess, number_to_guess = number_to_guess):
            game_over = True
        else:
            attempts -= 1
            if attempts == 1:
                print(f"You have {attempts} attempt remaining to guess the number")
            elif attempts == 0:
                print(f"Game over! The number was {number_to_guess}.")
                game_over = True
            else:
                print(f"You have {attempts} attempts remaining to guess the number")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/