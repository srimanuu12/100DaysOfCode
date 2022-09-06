from secrets import choice
from ssl import Options
from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_True = True

while is_True:
    options = menu.get_items()
    choice = input(f"What would you like ({options}) : ")
    if choice == "off":
        is_True = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
