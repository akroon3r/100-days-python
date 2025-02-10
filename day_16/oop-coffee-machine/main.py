from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    maker = CoffeeMaker()
    menu = Menu()
    moneyMachine = MoneyMachine()
    power = True
    # TODO -1: Prompt User by asking "What would you like? (espresso/latte/cappuccino):"

    while power:
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if drink_choice == 'off':
            print("Shutting down machine...")
            power = False
        elif drink_choice == 'report':
            print(maker.report())
        elif drink_choice == 'espresso' or drink_choice == 'latte' or drink_choice == 'cappuccino':
            drink = menu.find_drink(drink_choice)
            if maker.is_resource_sufficient(drink):
                print(f"The cost of your {drink.name} is ${drink.cost}")
                moneyMachine.make_payment(drink.cost)
                maker.make_coffee(drink)
            elif not maker.is_resource_sufficient(drink):
                power = False


