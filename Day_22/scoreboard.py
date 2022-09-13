from ast import alias
from turtle import Turtle

ALIGN = "center" 
SCORE_FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align=ALIGN, font=SCORE_FONT)
        self.goto(100,200)
        self.write(self.r_score, align=ALIGN, font=SCORE_FONT)

    def l(self):
        self.l_score += 1
        self.update_score()

    def r(self):
        self.r_score += 1
        self.update_score()

    