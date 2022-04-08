# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temp_list = []
# #     for row in data:
# #         if row[1]!="temp":
# #             temp_list.append(int(row[1]))
# #     print(temp_list)
#
# import pandas as pd
#
# # data = pd.read_csv("weather_data.csv")
# # # print(data)
# # # print(data[data.temp == data["temp"].max()])
#
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(data["Primary Fur Color"])
#
# # # worked as intended but complexity is O(n) x2
# # data_dict = {
# # }
# #
# # for x in data["Primary Fur Color"]:
# #     data_dict[x]=0
# #
# # for x in data["Primary Fur Color"]:
# #     data_dict[x] +=1
#
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("color count.csv")
#
# print(df)

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