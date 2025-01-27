# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to Treasure Island. Your missing is to find the treasure")
    first = input("Will you go left or right?\n")
    if first == "right":
        print("Game over!")
        exit()
    second = input("Will you swim or wait?\n")
    if second == "swim":
        print("Game over!")
        exit()
    third = input("Which door? red, blue or yellow:\n")
    if third == "red" or third == "blue":
        print("Game over!")
        exit()
    elif third == "yellow":
        print("You found the treasure!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
