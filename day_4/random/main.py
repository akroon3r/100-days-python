# This is a sample Python script.
import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello, world!")
    random_number = random.random() * 10
    print(random_number)

    random_float = random.uniform(1,10)
    print(random_float)

    heads_or_tails = random.randint(0,1)
    if heads_or_tails == 0:
        print("heads")
    elif heads_or_tails == 1:
        print("tails")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
