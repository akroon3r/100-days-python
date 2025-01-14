# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    cheese = input ("Do you want extra cheese? Y or N: ")

    bill = 0
    # todo work out how much they need to pay based on their size choice

    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25
    # todo work out how much to add to their bill based on their pepperoni choice

    if pepperoni == "Y" and size == "S":
        bill += 2
    elif pepperoni == "Y" and size == "M" or size == "L":
        bill += 3
    # todo work out their final amount based on whether if they want extra cheese

    if cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
