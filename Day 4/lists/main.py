# This is a sample Python script.
import random
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
    if choice == 0:
        print("You chose rock")
    elif choice == 1:
        print("You chose paper")
    elif choice == 2:
        print("You chose scissors")

    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print("Computer chose rock")
    elif computer_choice == 1:
        print("Computer chose paper")
    elif computer_choice == 2:
        print("Computer chose scissors")

    # if you choose rock
    if choice == 0 and computer_choice == 1:
        print("You lose!")
    elif choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 0 and computer_choice == 0:
        print("DRAW!")

    if choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 1 and computer_choice == 2:
        print("You lose!")
    elif choice == 1 and computer_choice == 1:
        print("DRAW!")

    if choice == 2 and computer_choice == 0:
        print("You lose!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    elif choice == 2 and computer_choice == 2:
        print("DRAW!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
