# This is a sample Python script.
from math_functions import add, subtract, multiply, divide
from cards import initialize_hands, hit, sum_of_hand, ace_is_one
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from cipher import encrypt, decrypt, caesar
from bid import add_bidder, compute_winner
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    while start_game == 'y':
        # Initialize hands for dealer and player, scores set to 0 and boolean to indicate the game is proceeding
        hands = initialize_hands()
        dealers_cards = hands['dealer']
        dealers_first_card = dealers_cards[0]
        players_cards = hands['player']
        game_over = False
        # Sum the values in the player and dealers hands to calculate their scores
        players_current_score = sum_of_hand(players_cards)
        dealers_current_score = sum_of_hand(dealers_cards)
        # Tell the player their hand and their score
        print(f'Your cards are: {players_cards}, and your current score is: {players_current_score}')
        print(f"Dealer's first card is: {dealers_first_card}")
        # Ask the player if they want another card (hit) or to end their turn
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while another_card == 'y' and game_over == False:
            # Add a new card to the players hand
            new_card = hit()
            players_cards.append(new_card)
            # Update their score
            players_current_score = sum_of_hand(players_cards)
            # Update the player of the new card in their hand and their score
            print(f"Player's updated hand: {players_cards}, and your current score is: {players_current_score}")
            # Check the players score to see if they busted, but also if they hold an ace (11) in their hand
            # If they do, set the value of the ace to 1
            if players_current_score > 21 and 11 in players_cards:
                print(f"Your score is greater than 21, and you hold an ace.")
                players_cards = ace_is_one(players_cards)
                players_current_score = sum_of_hand(players_cards)
                print(f"Your new hand is: {players_cards}")
                print(f"Your new score is: {players_current_score}")
            # If the players score is greater than 21, they've lost and end the game
            elif players_current_score > 21:
                print("You've busted! Game over.")
                game_over = True
            # If the game is not over (ie// score < 21, ask them if they wish to continue
            # Adding cards to their hand, if not, exit while loop
            if not game_over:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # If the game is not over, update the player of the cards in the dealers hand
        if not game_over:
            print(f"Dealer's hand is: {dealers_cards}")

        # Check to see if the dealers hand is less than 17 to add cards to their hand
        while dealers_current_score < 17 and game_over == False:
            print("Dealer deciding what to do...")
            new_card = hit()
            print(f"Dealer hits {new_card}")
            # Add new card to their hand, update their score
            dealers_cards.append(new_card)
            dealers_current_score = sum_of_hand(dealers_cards)
            # If the dealers score is over 21, check to see if they hold an ace, and
            # then set the value to 1, update their score
            if dealers_current_score > 21 and 11 in dealers_cards:
                print(f"The dealer's score is greater than 21, and they hold an ace.")
                dealers_cards = ace_is_one(dealers_cards)
                dealers_current_score = sum_of_hand(dealers_cards)
                print(f"The dealer's new score is {dealers_current_score}")
            # If the dealer hits and their score is greater than 21, the game is over
            elif dealers_current_score > 21:
                print("The dealer has busted! Game over, You win!")
                game_over = True
        # After both the player and deal have finished adding cards to their hand and neither has busted
        # Check scores to see if the player has won, lost or tied against the dealer
        if players_current_score > dealers_current_score and players_current_score <= 21 and game_over == False:
            print(f"You've beaten the dealer with a score of {players_current_score}! Congratulations!")
            game_over = True
        elif players_current_score == dealers_current_score and players_current_score <= 21 and game_over == False:
            print(f"Draw! You've tied the score with the dealer")
            game_over = True
        elif players_current_score < dealers_current_score and game_over == False:
            game_over = True
            print(f"You've lost to the dealers score of {dealers_current_score}")
        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    else:
        print("Thanks for playing!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
