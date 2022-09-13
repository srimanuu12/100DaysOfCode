from turtle import Turtle, position


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 40
        self.goto(new_x, new_y)

    def down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 40
        self.goto(new_x, new_y)