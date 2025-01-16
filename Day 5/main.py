# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Password Generator Project
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    level = input("Which level would you like to use? Easy or Hard:\n").lower()
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = ""
    hard_password_array = []
    hard_password = ""

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    if level == "easy":
        for number in range(1, nr_letters+1):
            password += random.choice(letters)
            #print(password)
        for number in range(1, nr_symbols+1):
            password += random.choice(numbers)
            #print(password)
        for number in range(1, nr_numbers+1):
            password += random.choice(symbols)
            #print(password)
        print(f"FINAL EASY PASSWORD: {password}")
    elif level == "hard":
        for number in range(1, nr_letters+1):
            hard_password_array.append(random.choice(letters))
            #print(hard_password_array)
        for number in range(1, nr_numbers+1):
            hard_password_array.append(random.choice(numbers))
            #print(hard_password_array)
        for number in range(1, nr_symbols+1):
            hard_password_array.append(random.choice(symbols))
            #print(hard_password_array)
        length = len(hard_password_array)
        print(f"length of hard password array: {length}")
        for number in range(1,length+1):
            character = random.choice(hard_password_array)
            hard_password += character
            hard_password_array.remove(character)
            #print(f"HARD PASSWORD: {hard_password}")

        print(f"FINAL HARD PASSWORD: {hard_password}" )


    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
