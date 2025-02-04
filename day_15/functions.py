
def print_report(resources):
    """
    Function requires resource data from coffee machine and loops through to print a formatted string of how much
    of that item exists in the machine
    """
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item.title()}: {resources[item]}ml")
        elif item == "coffee":
            print(f"{item.title()}: {resources[item]}g")
        elif item == "money":
            print(f"{item.title()}: ${resources[item]}")

def check_ingredients(resources, drink):
    """
    Function requires the resources available dictionary and the requirements for the drink to be made and checks to see
    if there is enough of each item available to make the drink. If there is enough of each item, the function returns
    True, else returns False
    """
    for item in resources:
        if resources[item] >= drink['ingredients'][item]:
            return True
        else:
            print(f"Sorry, there is not enough {item}")
            return False

def calculate_change_total(change_given):
    """
    Function requires the number of quarters, dimes, nickels and pennies that the user has entered to make a drink, multiply
    them by their monetary value and sum each amount, and return that amount as a float ex// 1.50
    """
    sum = 0
    for item in change_given:
        if item == 'quarters':
            sum += int(change_given['quarters']) * 0.25
        elif item == 'dimes':
            sum += int(change_given['dimes']) * 0.10
        elif item == 'nickels':
            sum += int(change_given['nickels']) * 0.05
        elif item == 'pennies':
            sum += int(change_given['pennies']) * 0.01
    return sum

def make_drink(resources, drink):
    """
    Function requires the ingredients for the drink to be made, and will subtract the requirements from the total amount of
    resources present.
    """
    for item in drink['ingredients']:
        difference = int(resources[item] - drink['ingredients'][item])
        resources[item] = difference
    return resources

def ask_for_change(change_given):
    """
    Function streamlines asking for change required to make a drink, and returns a dictionary with the updated values for each
    coin given to the machine
    """
    for item in change_given:
        change_given[item] = input(f'How many {item}?: ')
    return change_given


def calculate_change_difference(change_given, drink_cost):
    """
    Function requires change given in the form of a dictionary of coins provided by the user, and the cost of the drink they
    want to purchase. The function prints the difference (change) given back to the user rounded to two decimal places
    """
    change_total = 0
    for item in change_given:
        if item == 'quarters':
            change_total += int(change_given['quarters']) * 0.25
        elif item == 'dimes':
            change_total += int(change_given['dimes']) * 0.10
        elif item == 'nickels':
            change_total+= int(change_given['nickels']) * 0.05
        elif item == 'pennies':
            change_total += int(change_given['pennies']) * 0.01
    difference = change_total - drink_cost
    rounded_difference = round(difference, 2)
    print(f"Your change is ${rounded_difference}")

def add_profit(resources, drink_cost):
    """
    Function requires the resources dictionary and the cost of the drink completed. If money doesn't exist in the dictionary,"
    it sets the initial profit to the price of the drink just made, otherwise, it adds the drink cost to profit and returns
    the resources dictionary
    """
    if 'money' in resources:
        current_profit = resources['money']
        updated_profit = current_profit + drink_cost
        resources['money'] = updated_profit
    else:
        resources['money'] = drink_cost
    return resources