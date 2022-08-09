import random

rock ="""
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

img = [rock, paper, scissor]
print("Welcome to Rock Paper Scissor Game")


is_game = True
while is_game:
    player = int(input("""Select 1 - rock, 2 - paper, and 3 - scissor: """))
    computer = random.randint(1,3)
    if player >=3 and player < 0:
        print("Enter valid number")
    else:
        print("Player: ")
        print(img[player-1])
        print("Computer: ")
        print(img[computer-1])
        if player == 1 and computer == 3:
            print("You Win :)")
        elif player > computer:
            print("You Win :)")
        elif player == computer:
            print("Draw : | ")
        else:
            print("You lose :( ")
    print("Play again. Yes or no: ", end=" ")
    if input().lower() == "no":
        is_game = False
