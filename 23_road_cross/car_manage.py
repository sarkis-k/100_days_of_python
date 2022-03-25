from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.setheading(180)
        self.penup()
        self.goto(280, random.randint(-260, 260))
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
