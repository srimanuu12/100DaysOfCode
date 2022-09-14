from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MAKE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    
    def create_snake(self):
        
        for position in STARTING_POSITION:
            self.add_snake(position)
    
    def add_snake(self, position):
        new_s = Turtle("square")
        new_s.color("white")
        new_s.penup()
        new_s.goto(position)
        self.snakes.append(new_s)
    
    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):

        for snake in range(len(self.snakes)-1,0,-1):
            x_cor = self.snakes[snake -1].xcor()
            y_cor = self.snakes[snake -1].ycor()
            self.snakes[snake].goto(x_cor, y_cor)
        self.head.forward(MAKE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)