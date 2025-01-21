# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello, world!")
    # TODO - Randomly choose a word from the word_list array
    word_list = ['aardvark', 'baboon', 'camel']
    placeholder = list('')

    user_lives = 6
    letters_guessed = []

    hangman_word = random.choice(word_list)
    length_of_word = len(hangman_word)

    # TODO Create placeholder with underscores for each letter in the hangman word
    for letter in hangman_word:
        placeholder += '_'

    not_solved = True
    while not_solved:
        # TODO - Ask use to guess a letter and assign their value to a variable
        letter_guessed = input('Guess a letter: ').lower()
        if letter_guessed not in letters_guessed:
            letters_guessed.append(letter_guessed)
            # TODO - Check if the letter the user guessed is in the word, "Right", or "Wrong" if it is not
            if letter_guessed not in hangman_word:
                user_lives -= 1
                print('HANGMAN PICTURE GOES HERE')
                print('Incorrect guess, try again.')
                print(f'Lives remaining: {user_lives}')
            else:
                for letter in range(length_of_word):
                    if hangman_word[letter] == letter_guessed:
                        placeholder[letter] = letter_guessed
                        print('Correct guess!')
        else:
            print("HANGMAN PICTURE GOES HERE")
            print("You've guessed that letter already, try again")
            print(f'Lives remaining: {user_lives}')
        print("".join(placeholder))
        if user_lives == 0:
            print('Game over!')
            not_solved = False
        if '_' in placeholder:
            print('word is not solved yet')
        else:
            print('Congrats! The word is solved.')
            not_solved = False

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
