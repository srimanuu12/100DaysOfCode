import random

print("Welcome to Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X', 'W', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+" , "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",  "[",  "]", "^",  "_", "{", "|", "}", "~"]

no_letter = int(input("How many letters would you like in your password? "))
no_num =  int(input("How many numbers would you like? "))
no_symbol = int(input("How many symbols would you like? "))

password = []
total_chars = no_letter + no_num + no_symbol

for i in range(0,no_letter):
    password.append(random.choice(letters))

for i in range(0,no_num):
    password.append(random.choice(numbers))

for i in range(0,no_symbol):
    password.append(random.choice(symbols))

#random.choice - when you want to choose multiple random items from iterable (here it is list) including duplicates
#random.sample - when you want to choose multiple random items from iterable (here it is list) without including duplicates
secr_password = ''.join(random.sample(password,total_chars))
print(f"Here is your password: {secr_password}")