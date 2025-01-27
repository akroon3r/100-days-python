# This is a sample Python script.
from math_functions import add, subtract, multiply, divide

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from cipher import encrypt, decrypt, caesar
from bid import add_bidder, compute_winner
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO add 4 functions from math_functions into a dict, keys being their math operators
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }
    # TODO: Use the dictionary operations to perform the calculations
    # Multiple 4 * 8
    first_number = float(input("What's the first number? "))
    for key in  operations:
        print(key)
    continue_calc = True
    while continue_calc:
        operation = input("Pick an operation: ")
        if operation not in ["+", "-", "*", "/" ]:
            print("Operation not +, -, *, /. Please enter an operation. ")
            operation = input("Pick an operation: ")
        else:
            second_number = float(input("What's the next number?: "))
            output = operations[operation](a = first_number, b = second_number)
            print(f'{first_number} {operation} {second_number} = {output}')
            string_output = str(output)
            continue_string = "Type 'y' to continue calculating with " + string_output + " or 'n' to start a new calculation\n"
            continue_input = input(continue_string)
            if continue_input == 'n':
                continue_calc = False
            else:
                first_number = output

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
