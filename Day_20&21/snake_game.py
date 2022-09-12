from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # Collision with the wall

    if snake.head.xcor() > 290 or snake.head.ycor() > 300 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Collision with the tail

    for s in snake.snakes[1:]:
        if snake.head.distance(s) < 10:
            is_game_on = False
            score.game_over()
        
    
screen.exitonclick()