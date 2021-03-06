from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)

    def up_move(self):
        self.forward(20)

    def level_up(self):
        self.goto(0, -280)
