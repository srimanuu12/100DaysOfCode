from operator import is_
from turtle import Turtle, Screen
import random

is_gameon = False
screen = Screen()
screen.setup(width = 500, height = 400)
# Pop Up message
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for pos in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[pos])
    new_turtle.goto(x = -230, y = y_positions[pos])
    turtles.append(new_turtle)

if user_bet:
    is_gameon = True

while is_gameon:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_gameon = False
            win_color = turtle.pencolor()
            if win_color == user_bet:  
                print(f"You Won! The {win_color} turtle is winner!")
            else:
                print(f"You lost. The winner is {win_color} turtle. ")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()