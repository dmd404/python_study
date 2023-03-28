from menu import MenuItem, Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    options = menu.get_items()
    is_on = True
    while is_on:
        choice = input(f'What do you want? ({options}): ')
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)



if __name__ == '__main__':
    main()