from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision with wall

    if ball.ycor() > 270 or ball.ycor() <-270:
        ball.bounce_y()
    
    # COllision with paddle

    right = ball.distance(r_paddle) < 50 and ball.xcor() > 330
    left = ball.distance(l_paddle) < 50 and ball.xcor() < -330

    if right or left :
        ball.bounce_x()

    # Detect when ball misses the paddle
    #r_paddle
    if ball.xcor() > 380:
        ball.reset()
        score.l()
    
    #l_padd
    if ball.xcor() < -380:
        ball.reset()
        score.r()

screen.exitonclick()