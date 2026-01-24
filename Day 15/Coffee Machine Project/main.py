from data import MENU, resources, money
profit = 0
machine_on = True
can_make_drink = True

def check_resources(chosen_drink):
    """
        Checks if there are enough ingredients in resources for the chosen drink.
        :param chosen_drink: The name of the drink the user wants.
        :return: True if resources are sufficient, False otherwise.
        """
    for resource, amount in MENU[chosen_drink]["ingredients"].items():
        if amount > resources[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    else:
        return True

def print_report():
    for resource, amount in resources.items():
        unit = "ml" if resource != "coffee" else "g"
        print(f"{resource.title()}: {amount}{unit}")
    print(f"Money: ${profit: .2f}")

def process_coins(chosen_drink):
    """
        Prompts user for coins and calculates if payment is sufficient.
        :param chosen_drink: The name of the drink to check the cost against.
        :return: The cost of the drink if payment successful, otherwise 0.
        """
    print("Please insert coins")
    cost_drink = MENU[chosen_drink]["cost"]
    total_inserted = 0
    for coin, value in money.items():
        try:
            count = int(input(f"how many {coin}?: "))
            total_inserted += count * value
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0

    change = total_inserted - cost_drink

    if total_inserted < cost_drink:
        print("Sorry, that's not enough money")
        return 0
    else:
        if change > 0:
            print(f"Here's ${round(change, 2)} in change")
        return cost_drink

def update_resources(chosen_drink):
    """
        Deducts the required ingredients from the machine's resources.
        :param chosen_drink: The name of the drink whose ingredients should be deducted.
        :return: None
        """
    for resource, amount in MENU[chosen_drink]["ingredients"].items():
         resources[resource] -= amount
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
       print_report()
    elif user_input == "off":
        machine_on = False

    elif user_input in MENU:
        can_make_drink = check_resources(user_input)
        if can_make_drink:
            payment = process_coins(user_input)
            if payment > 0:
                profit += payment
                update_resources(user_input)
                print(f"here's your {user_input} ☕, Enjoy!")
