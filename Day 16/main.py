from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
machine_on = True
print(my_money_machine.report())
while machine_on:
    user_input = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif user_input == "off":
        machine_on = False
    elif my_menu.find_drink( user_input):
        drink=my_menu.find_drink( user_input)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)

