MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

DRINK_MENU = ['espresso', 'latte', 'cappuccino']

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

METRICS = ['ml', 'ml', 'g', '$']


# prints resources report
def print_report():
    for i, r in enumerate(resources):
        if r == 'money':
            print(f"{r.title()}: {METRICS[i]}{resources[r]}")
        else:
            print(f"{r.title()}: {resources[r]}{METRICS[i]}")
    # print(f"Money: ${money}")


def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def resources_sufficient(user_choice):
    for i in resources:
        if i != 'money' and resources[i] < user_choice['ingredients'][i]:
            print(f'Sorry there is not enough {i}.')


def transaction(user_choice):
    profit = 0
    print('Please insert coins.')
    coins_inserted = process_coins()
    if coins_inserted < user_choice['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        profit += user_choice['cost']
        change = coins_inserted - user_choice['cost']
        print(f"Here's ${change:.2f} in change.")
        return profit


# loops until the user input is 'off'
def main():
    money = 0
    should_continue = True
    while should_continue:
        choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice == 'off':
            should_continue = False
        elif choice in DRINK_MENU:
            drink = MENU[choice]
            resources_sufficient(drink)  # check resource sufficiency
            money += transaction(drink)  # process coin and return profit to money
            resources['money'] = "%.2f" % round(money, 2)  # round to 2 decimal places
            
            # update resources
            for i in drink['ingredients']:
                resources[i] -= drink['ingredients'][i]
            print(f"Here's your {choice}. Enjoy!")
        elif choice == 'report':
            print_report()
        else:
            print('invalid menu')
            continue


if __name__ == "__main__":
    main()
