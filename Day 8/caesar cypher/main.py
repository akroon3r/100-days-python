# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from cipher import encrypt, decrypt, caesar

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keep_using = 'yes'
    while keep_using == 'yes':
        direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n").lower()
        text = input('Type in your message:\n').lower()
        shift = int(input("Type in the shift number:\n"))
        caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
        keep_using = input('Would you like to continue? Type yes or no\n').lower()

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
