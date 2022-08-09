print("Welcome to Tip Calculator")

amount = float(input("Enter amount: "))
people = int(input("How many members? "))
tip = int(input("Please opt tip 10, 15, 20:" ))
tip_amount = amount * (tip/100)
total_amount = amount + tip_amount
each_person = total_amount/people
print(f"Each person has to pay: {each_person}")