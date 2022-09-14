from turtle import Screen, Turtle
import time
from player import Player
from car_manager import Car
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Car()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move()

    # Collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            score.game_over()

    # Next Level
    if player.is_finished():
        player.go_to_start()
        cars.level_up()
        score.increase()

screen.exitonclick()