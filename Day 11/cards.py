import random

def hit():
    """
    Cards: Ace is 11 until it's required to be 1, then all numeric cards up to 10, and Jack,
    Queen, King are valued as 10 as well.

    This function, when called, should return the dealers hand (2 cards) and the players hand
    (2 cards)
    :return:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def initialize_hands():
    hands = {
        'dealer':  [],
        'player': []
    }
    # Cards are dealt like at a table, one to player, one to dealer, one to player, one to dealer
    hands['player'].append(hit())
    hands['dealer'].append(hit())
    hands['dealer'].append(hit())
    hands['player'].append(hit())
    return hands

def sum_of_hand(hand):
    return sum(hand)

def ace_is_one(hand):
    position_of_eleven = hand.index(11)
    hand[position_of_eleven] = 1
    return hand
