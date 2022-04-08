
import turtle
import pandas as pd
from turtle import Turtle, Screen

screen = turtle.Screen()
screen.title("U.S. States Guess Game")
image = "states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("states_game/50_states.csv")
states_list = data.state.to_list()

guessed_num = 0
while guessed_num < 50:
    answer_state = screen.textinput(title=f"{guessed_num}/50 guessed", prompt="what else?").title()
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_num += 1

print(data[data.state == "Ohio"])

turtle.mainloop()