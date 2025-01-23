
bidders = {}
# Function should append the name and value that person bid for the item to a dictionary
def add_bidder(name, amount):
    bidders[name] = amount
# Function should find the max bid in the diction
def compute_winner():
    max_bid = 0
    winner = ''
    for person in bidders:
        if bidders[person] > max_bid:
            max_bid = bidders[person]
            winner = person.upper()
    print(f'The winner is {winner} with a bid of ${max_bid}')
    #print(f'Compute winner: {bidders}')