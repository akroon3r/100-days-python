# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from cipher import encrypt, decrypt, caesar
from bid import add_bidder, compute_winner
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    other_bidders = 'yes'
    while other_bidders == 'yes':
        name = input('What is your name?\n').lower()
        bid = int(input('What is your bid for the item?\n$'))
        other_bidders = input('Are there other bidders? yes/no\n').lower()
        if other_bidders == 'no':
            # call function to add the last winner
            add_bidder(name = name, amount = bid)
            # call function to compute winner
            winner = compute_winner()
        elif other_bidders == 'yes':
            # call function to append name, bid into dictionary
            # clear screen
            add_bidder(name = name, amount = bid)
            print('\n'*20)
        else:
            print('You did not enter "yes" or "no", try again')
            other_bidders = input('Are there other bidders? yes/no\n').lower()
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
