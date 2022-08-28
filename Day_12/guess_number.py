import random

EASY = 8
HARD = 4

def check_answer(guess,correct_answer,turns):
    
    if guess > correct_answer:
        print("Too High")
        return turns-1
    elif guess < correct_answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You guessed right. The answer was {correct_answer}")

def choose_level():
    level = input("Which level do you want to play? Type 'e' for Easy or 'h' for Hard: ").lower()
    if level == "e":
        return EASY
    else:
        return HARD

def play_game():
    turns = choose_level()
    correct_answer = random.randint(1,100)
    guess = 0
    while guess != correct_answer:
        print(f"You have {turns} attempts remaning to guess the number.")
        guess = int(input("Guess a Number: "))
        turns = check_answer(guess, correct_answer, turns)
        if turns == 0:
            print(f"You ran out of attempts. You lost!. Answer was {correct_answer}")
            return
        elif guess != correct_answer:
            print("Guess Again")

logo = '''


 ____                                       __  __                      __                              
/\  _`\                                    /\ \/\ \                    /\ \                             
\ \ \L\_\  __  __     __    ____    ____   \ \ ` \\ \  __  __    ___ ___\ \ \____     __   _ __          
 \ \ \L_L /\ \/\ \  /'__`\ /',__\  /',__\   \ \ , ` \/\ \/\ \ /' __` __`\ \ '__`\  /'__`\/\`'__\        
  \ \ \/, \ \ \_\ \/\  __//\__, `\/\__, `\   \ \ \`\ \ \ \_\ \/\ \/\ \/\ \ \ \L\ \/\  __/\ \ \/         
   \ \____/\ \____/\ \____\/\____/\/\____/    \ \_\ \_\ \____/\ \_\ \_\ \_\ \_,__/\ \____\\ \_\         
    \/___/  \/___/  \/____/\/___/  \/___/      \/_/\/_/\/___/  \/_/\/_/\/_/\/___/  \/____/ \/_/         
                                                                                                        
                                                                                                        
'''
print(logo)

while input("Do you want to play Guess Number? Type 'y' or 'n': ").lower() == "y":
    play_game()
