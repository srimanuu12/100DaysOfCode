from hangman_art import logo, stages
from hangman_words import word_list
import random

print(logo)

correct_answer = random.choice(word_list)
count = len(stages) - 1
guessed_answer = ['_' for i in correct_answer]

is_game = True
chance = 0
print("Guess a word: ", ''.join(guessed_answer))
print(stages[count])
while is_game:

    letter = input("Guess a word: ").lower()
    if letter in guessed_answer:
        print(f"You already guessed {letter}")

    for k,v in enumerate(correct_answer):
        if v == letter:
            guessed_answer[k] = letter
    print("Word:",''.join(guessed_answer))
    if letter not in correct_answer:
        print(f"you guessed {letter}, that's not a word. You lost a life")
        count -=1
        if count == 0:
            is_game = False
            print("You lost")
    
    if "_" not in guessed_answer:
        is_game = False
        print("You win")

    print(stages[count])