def cal(choice,n1,n2):
    if choice == "+":
        return n1 + n2
    elif choice == "-":
        return n1 - n2
    elif choice == "*":
        return n1 * n2
    else:
        return n1 / n2


def calculator():
    logo = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
    print(logo)
    again = True
    n1 = float(input("Enter first number: "))
    while again:        
        print("+\n-\n*\n/")
        choice = input("Pick an operator: ")
        n2 = float(input("Enter next number: "))
        ans = cal(choice,n1,n2)
        print(f"{n1} {choice} {n2} = {ans}")

        again = input(f"Type 'y' to continue calculation with {ans} or Type 'n' to start new calculation: ").lower()

        if again == "y":
            n1 = ans
            again = True

        elif again == "n":
            calculator()
        else:
            print("Invalid input")

calculator()

