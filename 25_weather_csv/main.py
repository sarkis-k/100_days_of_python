# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp_list = []
    for row in data:
        if row[1]!="temp":
            temp_list.append(int(row[1]))
    print(temp_list)