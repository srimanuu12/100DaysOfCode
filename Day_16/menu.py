class MenuItem():
    def __init__(self, drink, cost, water, milk, coffee):
        self.drink = drink
        self.cost = cost 
        self.ingredients = {
            "water" : water,
            "milk" : milk,
            "coffee" : coffee
        }

class Menu():

    def __init__(self):
        self.menu = [
            MenuItem(drink="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(drink="espresso", water=50, milk=0, coffee=18, cost=2.5),
            MenuItem(drink="cappuccino", water=250, milk=50, coffee=24, cost=3.5)
        ]

    def get_items(self):
        choice = ""
        for item in self.menu:
            choice += f"{item.drink}/"
        return choice
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.drink == order_name:
                return item
        print("Sorry that item is not found")