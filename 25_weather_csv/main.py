# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     for row in data:
#         if row[1]!="temp":
#             temp_list.append(int(row[1]))
#     print(temp_list)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data)
# # print(data[data.temp == data["temp"].max()])

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

# # worked as intended but complexity is O(n) x2
# data_dict = {
# }
#
# for x in data["Primary Fur Color"]:
#     data_dict[x]=0
#
# for x in data["Primary Fur Color"]:
#     data_dict[x] +=1

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("color count.csv")

print(df)