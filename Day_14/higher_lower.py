import random
from game_data import data

def check_answer(a, b, guess):

    option_a_count = a["follower_count"]
    option_b_count = b["follower_count"]
    if option_a_count > option_b_count:
        return guess == "a"
    else:
        return guess == "b"

def play_game():

    a = random.choice(data)
    b = random.choice(data)
    score = 0
    is_done = False
    
    while not is_done:
        print(f'Option A: {a["name"]}, a {a["description"]}, from {a["country"]}')
        print(vs)
        print(f'Option B: {b["name"]}, a {b["description"]}, from {b["country"]}')
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(a, b, guess)
        a = b        
        b = random.choice(data)
        while a == b:
            b = random.choice(data)
        
        if is_correct:
            score += 1
            print(f"You're right!. Current score is {score}")
        else:
            is_done = True
            print(f"Sorry, that's wrong. Final score is {score}")

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)
while input("Do you want to play Higher vs Lower Game? Type 'y' or 'n': ").lower() == 'y':
    play_game()
