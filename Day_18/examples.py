from turtle import Screen, Turtle, colormode
import random

turtle = Turtle()
pen = Turtle()

turtle.shape("triangle")
turtle.color("orange")

# Draw a Square
for i in range(0,4):
    turtle.right(90)
    turtle.forward(100)

turtle.clear()

# Dashed line
for _ in range(10):
    pen.forward(10)
    pen.pendown()
    pen.forward(10)
    pen.up()

#Different Shapes
def diff_shapes(sides):
    angle = 360 / sides
    for a in range(sides):
        pen.speed("fastest")
        pen.down()
        pen.shape("turtle")
        pen.color("blue")
        pen.forward(50)
        pen.right(angle)


for i in range(3,11):
    diff_shapes(i)

pen.clear()
# Random Walk

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle_pen = Turtle()
turtle_pen.pensize(5)
turtle_pen.speed("fastest")

for _ in range(100):
    turtle_pen.color(random.choice(colours))
    turtle_pen.forward(25)
    turtle_pen.setheading(random.choice(directions))


# Random RGB Colors:

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

colormode(255)
for _ in range(100):
    turtle_pen.color(random_color())
    turtle_pen.forward(25)
    turtle_pen.setheading(random.choice(directions))

turtle_pen.clear()

screen = Screen()
screen.exitonclick()
