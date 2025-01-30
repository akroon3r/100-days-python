from data import menu, resources
from functions import (print_report, check_ingredients, calculate_change_total, make_drink, ask_for_change,
                       calculate_change_difference, add_profit)

if __name__ == '__main__':

    """
    TODO 1 - Prompt user by asking "What would you like? (espresso/latte/cappuccino): 
    a. check the user's input to decide what to do next
    b. The prompt should show every time an action has completed ex// once the drink is dispensed
       the prompt should show again to serve the next customer
    """
    """
    TODO 2 - Turn off Coffee Machine my entering "off" prompt
    a. for maintainers of the coffee machine they can use "off" as the secret work to turn off the machine.
       Your code should end execution when this happens
    """

    """
    TODO 3 - Print report
    a. when the user enters "report" to the prompt, a report should be generated that shows what the 
       current resource values are. ex//
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
    """
    power = True
    while power:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "espresso":
            drink = menu['espresso']
            if check_ingredients(resources, drink):
                # Ask for change to make drink
                print(f"The price for espresso is ${drink['cost']}")
                change_given = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
                ask_for_change(change_given)
                # Check that change entered is enough to make drink
                if calculate_change_total(change_given) >= drink['cost']:
                    make_drink(resources = resources, drink = drink)
                    add_profit(resources, drink['cost'])
                    if calculate_change_total(change_given) > drink['cost']:
                        calculate_change_difference(change_given, drink['cost'])
                    print("Enjoy your espresso!")
                else:
                    print("Sorry, not enough money to make your espresso")
                # Make drink - update the resources dictionary
                # dispense drink
            else:
                power = False
        elif order == "latte":
            drink = menu['latte']
            if check_ingredients(resources, drink):
                # Ask for change to make drink
                print(f"The price for espresso is ${drink['cost']}")
                change_given = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
                ask_for_change(change_given)
                # Check that change entered is enough to make drink
                if calculate_change_total(change_given) >= drink['cost']:
                    make_drink(resources=resources, drink=drink)
                    add_profit(resources, drink['cost'])
                    if calculate_change_total(change_given) > drink['cost']:
                        calculate_change_difference(change_given, drink['cost'])
                    print('Enjoy your latte!')
                else:
                    print("Sorry, not enough money to make your espresso")
                # Make drink - update the resources dictionary
                # dispense drink
            else:
                power = False
        elif order == "cappuccino":
            drink = menu['cappuccino']
            if check_ingredients(resources, drink):
                # Ask for change to make drink
                print(f"The price for espresso is ${drink['cost']}")
                change_given = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
                ask_for_change(change_given)
                # Check that change entered is enough to make drink
                if calculate_change_total(change_given) >= drink['cost']:
                    make_drink(resources=resources, drink=drink)
                    add_profit(resources, drink['cost'])
                    if calculate_change_total(change_given) > drink['cost']:
                        calculate_change_difference(change_given, drink['cost'])
                    print("Enjoy your cappuccino!")
                else:
                    print("Sorry, not enough money to make your espresso")
                # Make drink - update the resources dictionary
                # dispense drink
            else:
                power = False
        elif order == "report":
            print_report(resources)
        elif order == "off":
            print("Turning coffee machine off...")
            exit()
        else:
            order = input("Please enter a drink choice from the menu. (espresso/latte/cappuccino): ")

    """
    TODO 4 -Check resources sufficient
    a. when the user chooses a drink, the program should check if there are enough resources to make that drink
    b. if latte requires 200ml water but there is only 100ml left in the machine, it should not continue and print
       "Sorry there is not enough water."
    c. The same should happen if another resource is depleted ex// milk, coffee
    """

    """
    TODO 5 - Process coins
    a. if there are sufficient resources to make the drink selected, then the program should prompt the user to insert
       coins
    b. Remember that quarters = $0.25, dimes = $0.10, nickels = $0.05 and pennies = $0.01
    c. Calculate the monetary value of the coins inserted ex// 1 quarter, 2 dimes, 1 nickel, 2 pennies 
       = 0.25 + 0.1 + 0.05 + 0.01*2 = $0.52
    """

    """
    TODO 6 - Check transaction is successful
    a. Check that the user has inserted enough money to purchase the drink they selected
    b. If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this
       will be reflected the next time "report" is triggered ex//
       ...
       Money: $2.50
    c. if the user has inserted too much money, the machine should offer change
       ex// "Here is [VALUE] in change. Change is rounded to 2 decimal places
    """

    """
    TODO 7 - Make Coffee
    a. if the transaction is successful and there are enough resource to make the drink that the user has selected, then
    the ingredients to make the drink should be deducted from the coffee machine resources.
    
    ex// report before purchasing a latte
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0.00
    
    Report after purchasing latte:
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.50
    
    b. once all resources have been deducted, tell the user "Here is your [DRINK]. Enjoy!"
    """
