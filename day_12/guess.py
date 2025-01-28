def check_guess(guess, number_to_guess):
    if guess > number_to_guess:
        print("Too high.")
        return False
    elif guess < number_to_guess:
        print("Too low.")
        return False
    elif guess == number_to_guess:
        print(f"You got it! the answer was {number_to_guess}")
        return True