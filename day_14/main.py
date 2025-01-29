from random import randrange

from art import higher_lower, vs
from data import data
from functions import compare

if __name__ == '__main__':
    # get length of the data dictionary
    length_of_data = len(data)
    # generate a random number between 0 and length of dictionary
    random_index_A = randrange(0, 49)
    random_index_B = randrange(0, 49)
    # make sure the random indexes aren't the same
    index_not_same = False
    while not index_not_same:
        if random_index_A == random_index_B:
            random_index_B = randrange(0, 49)
        else:
            index_not_same = True
    # create a score integer variable, set to zero
    score = 0
    game_over = False
    data_A = data[random_index_A]
    data_B = data[random_index_B]
    # print the higher lower logo
    print(higher_lower)
    while not game_over:
        # create a dictionary A and dictionary B to store data from provided data object
        # print out "Compare A: {name_A}, a {profession_A} from {location_A}"
        print(f"Compare A: {data_A['name']} is a {data_A['description']} from {data_A['country']}")
        print(vs)
        # print out "Compare B{ {name_B}, a {profession_B from {location_B}"
        print(f"Compare B: {data_B['name']} is a {data_B['description']} from {data_B['country']}")
        # ask for input "Who has more followers? Type 'A' or 'B': --> use upper
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        # create/call compare function with followers_A and followers_B as parameters, return the greater
        answer = compare(data_A = data_A, data_B = data_B)

        # if guess A or B is correct, increment score, inform user
        if guess == 'A' and answer == 'A' or guess == 'B' and answer == 'B':
            score += 1
            print(f"You're right! Current score: {score}")
            if guess == 'A':
                random_index_B = randrange(0, 49)
                data_B = data[random_index_B]
            elif guess == 'B':
                data_A = data[random_index_B]
                random_index_B = randrange(0, 49)
                data_B = data[random_index_B]
            print(higher_lower)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
