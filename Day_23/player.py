from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISHED_YCOR = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - MOVE_DISTANCE
        self.goto(x_cor, y_cor)
    
    def is_finished(self):
        if self.ycor() > FINISHED_YCOR:
            return True
        else:
            return False