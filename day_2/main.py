# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the tip calculator")
    bill = float(input("How much was your bill? $"))
    tip = int(input("What percentage would you like to tip? (10, 12, 15, 18)"))
    people = int(input("How many people are splitting the bill?"))

    tip_total = bill * (tip / 100)
    total_bill = bill + tip_total
    per_person = total_bill / people
    rounded_per_person = round(per_person, 2)

    print(f"Each person should pay ${rounded_per_person}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
