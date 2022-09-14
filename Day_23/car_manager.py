from turtle import Turtle
import random

COLORS = ["blue", "red", "orange", "purple", "yellow", "green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 0.8, stretch_len= 1.8)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-240,240)
            new_car.goto(280,y_cor)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    
    

    
    
    
