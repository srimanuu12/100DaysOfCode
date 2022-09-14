from turtle import Turtle

FONT = ("Courier",18,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-260,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Level {self.level}", align="left", font= FONT)
    
    def increase(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)