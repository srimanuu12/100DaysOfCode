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
        },"cost": 3
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

def isenough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] < RESOURCES[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins. ")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickles = float(input("How many nickles? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    return quarters+dimes+nickles+pennies

def is_transaction_successful(process, drinkcost):


is_over = True
while is_over:
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        s_over = False
    elif choice == "report":
        for k,v in RESOURCES.items():
            if k == "water" or k == "milk":
                print(f"{k}: {v} ml")
            else:
                print(f"{k}: {v} g")
    else:
        drink = MENU[choice]
        if isenough_resources(drink["ingredients"]):
            is_transaction_successful(process_coins(), drink["cost"]):



