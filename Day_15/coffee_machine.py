MENU = {
    "espresso": {
        "ingredients":{
            "water": 100,
            "coffee": 10,
        },"cost" : 2.5  
    },
    "latte":{
        "ingredients":{
            "water": 150,
            "milk": 100,
            "coffee": 8
        },"cost": 2.5
    },
    "cappuccino":{
        "ingredients":{
            "water": 120,
            "milk": 100,
            "coffee": 9
        }, "cost": 3.5
    }  
}
RESOURCES = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}

def isresource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > RESOURCES[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(coins, drinkcost):
    if coins >= drinkcost:
        global profit
        change = round(coins - drinkcost, 2)
        print(f"Here is ${change} dollars in change")
        profit += drinkcost
        RESOURCES["Money"] = profit 
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(choice, order_ingredients):
    for i in order_ingredients:
        RESOURCES[i] -= order_ingredients[i]
    print(f"Here is your {choice}. Enjoy!")
    
profit = 0
is_over = True
while is_over:
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        s_over = False
    elif choice == "report":
        for k,v in RESOURCES.items():
            if k == "water" or k == "milk":
                print(f"{k}: {v} ml")
            elif k == "Money":
                print(f"{k}: ${v}")
            else:
                print(f"{k}: {v} g")
    else:
        drink = MENU[choice]
        if isresource_sufficient(drink["ingredients"]):
            coins = process_coins()
            if is_transaction_successful(coins, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


