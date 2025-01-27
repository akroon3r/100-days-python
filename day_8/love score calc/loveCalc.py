# loveCalc.py

def calculate_love_score(name_one, name_two):
    lower_one = name_one.lower()
    lower_two = name_two.lower()
    true_list = ['t', 'r', 'u', 'e']
    true_sum_score = 0
    for letter in true_list:
        score = lower_one.count(letter) + lower_two.count(letter)
        true_sum_score += score
        upper_letter = letter.upper()
        #print(f'{upper_letter} occurs {score} times')
    #print(f'Total = {true_sum_score}')
    love_list = ['l', 'o', 'v', 'e']
    love_sum_score = 0
    for letter in love_list:
        score = lower_one.count(letter) + lower_two.count(letter)
        love_sum_score += score
        upper_letter = letter.upper()
        #print(f'{upper_letter} occurs {score} times')
    #print(f'Total = {love_sum_score}')
    concat_score_string = int(str(true_sum_score) + str(love_sum_score))
    print(f'{concat_score_string}')