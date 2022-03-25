import random
import time
from turtle import Screen
from player import Player
from car_manage import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []
car_generator = 6

player = Player()
score = Scoreboard()

level = 1


screen.listen()
screen.onkey(player.up_move, "Up")


game_is_on = True
while game_is_on:

    if car_generator % 3 == 0:
        car = CarManager()
        for x in range(0, level):
            car.level_up()
        cars.append(car)
    car_generator += 1

    screen.update()
    time.sleep(0.1)

    for car in cars:
        car.move()
        # collision with car => game over
        if player.distance(car) < 20:
            game_is_on = False

    if player.ycor() > 280:
        level += 1
        score.score += 1
        score.update()
        car_generator = 0
        player.level_up()




