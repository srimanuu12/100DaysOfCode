from turtle import Screen, Turtle, colormode
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

pen = Turtle()
pen.pensize(1)
pen.speed("fastest")
colormode(255)

def spirograph(gap):
    for i in range(int(360/gap)):
        pen.color(random_color())
        pen.circle(50)
        pen.setheading(pen.heading()+gap)

spirograph(8)
    

screen = Screen()
screen.exitonclick()
